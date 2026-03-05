"""Tests for Personal Access Token (PAT) authentication support."""

import pytest
from datetime import datetime, timedelta
from unittest.mock import patch

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.delegated_auth import (
    DelegatedTokenCredentials,
    DelegatedTokenConfig,
    DelegatedTokenProvider,
)


class TestBearerTokenConfiguration:
    """Test access_token field on Configuration for bearer auth."""

    def test_bearer_token_stored(self):
        config = Configuration(access_token="ddpat_test123")
        assert config.access_token == "ddpat_test123"

    def test_bearer_token_default_none(self):
        config = Configuration()
        assert config.access_token is None

    @patch.dict("os.environ", {"DD_BEARER_TOKEN": "ddpat_from_env"})
    def test_bearer_token_env_var(self):
        config = Configuration()
        assert config.access_token == "ddpat_from_env"

    @patch.dict("os.environ", {"DD_BEARER_TOKEN": "ddpat_from_env"})
    def test_bearer_token_env_var_no_override(self):
        config = Configuration(access_token="ddpat_explicit")
        assert config.access_token == "ddpat_explicit"


class TestAuthSettingsWithBearerToken:
    """Test auth_settings() with access_token configured."""

    def test_auth_settings_includes_bearer(self):
        config = Configuration(access_token="ddpat_test123")
        auth = config.auth_settings()
        assert "bearerAuth" in auth
        assert auth["bearerAuth"]["type"] == "bearer"
        assert auth["bearerAuth"]["in"] == "header"
        assert auth["bearerAuth"]["key"] == "Authorization"
        assert auth["bearerAuth"]["value"] == "Bearer ddpat_test123"

    def test_auth_settings_without_bearer(self):
        config = Configuration()
        auth = config.auth_settings()
        assert "bearerAuth" not in auth


class TestUpdateParamsForAuthWithBearerToken:
    """Test that update_params_for_auth sends all configured auth headers."""

    def _make_endpoint(self, config, auth_schemes):
        """Helper to create an Endpoint with given auth schemes."""
        api_client = ApiClient(config)
        return _Endpoint(
            settings={
                "response_type": None,
                "auth": auth_schemes,
                "endpoint_path": "/api/v2/test",
                "operation_id": "test_op",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={"accept": ["application/json"]},
            api_client=api_client,
        )

    def test_all_auth_headers_sent_when_all_configured(self):
        """When all credentials are set, all auth headers are sent."""
        config = Configuration(
            api_key={"apiKeyAuth": "test-api-key", "appKeyAuth": "test-app-key"},
            access_token="ddpat_test_pat",
        )
        endpoint = self._make_endpoint(config, ["apiKeyAuth", "appKeyAuth", "bearerAuth"])
        headers = {}
        queries = []
        endpoint.update_params_for_auth(headers, queries)

        assert headers["Authorization"] == "Bearer ddpat_test_pat"
        assert headers["DD-API-KEY"] == "test-api-key"
        assert headers["DD-APPLICATION-KEY"] == "test-app-key"

    def test_bearer_only(self):
        """Bearer token works without any API keys configured."""
        config = Configuration(access_token="ddpat_test_pat")
        endpoint = self._make_endpoint(config, ["apiKeyAuth", "appKeyAuth", "bearerAuth"])
        headers = {}
        queries = []
        endpoint.update_params_for_auth(headers, queries)

        assert headers["Authorization"] == "Bearer ddpat_test_pat"
        assert "DD-API-KEY" not in headers
        assert "DD-APPLICATION-KEY" not in headers

    def test_api_keys_only(self):
        """Regular auth works without bearer token."""
        config = Configuration(
            api_key={"apiKeyAuth": "test-api-key", "appKeyAuth": "test-app-key"},
        )
        endpoint = self._make_endpoint(config, ["apiKeyAuth", "appKeyAuth", "bearerAuth"])
        headers = {}
        queries = []
        endpoint.update_params_for_auth(headers, queries)

        assert headers["DD-API-KEY"] == "test-api-key"
        assert headers["DD-APPLICATION-KEY"] == "test-app-key"
        assert "Authorization" not in headers

    def test_bearer_not_sent_when_not_in_endpoint_auth(self):
        """access_token set but endpoint doesn't declare bearerAuth."""
        config = Configuration(
            api_key={"apiKeyAuth": "test-api-key", "appKeyAuth": "test-app-key"},
            access_token="ddpat_test_pat",
        )
        endpoint = self._make_endpoint(config, ["apiKeyAuth", "appKeyAuth"])
        headers = {}
        queries = []
        endpoint.update_params_for_auth(headers, queries)

        assert headers["DD-API-KEY"] == "test-api-key"
        assert headers["DD-APPLICATION-KEY"] == "test-app-key"
        assert "Authorization" not in headers
