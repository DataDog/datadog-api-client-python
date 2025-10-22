"""Tests for delegated authentication functionality."""

import json
import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock, patch

from datadog_api_client.delegated_auth import (
    DelegatedTokenCredentials,
    DelegatedTokenConfig,
    DelegatedTokenProvider,
    get_delegated_token,
    parse_delegated_token_response,
    get_delegated_token_url,
)
from datadog_api_client.configuration import Configuration
from datadog_api_client.exceptions import ApiValueError


class TestDelegatedTokenCredentials:
    """Test DelegatedTokenCredentials class."""

    def test_init(self):
        """Test initialization of DelegatedTokenCredentials."""
        org_uuid = "test-org-uuid"
        token = "test-token"
        proof = "test-proof"
        expiration = datetime.now() + timedelta(minutes=15)

        creds = DelegatedTokenCredentials(org_uuid, token, proof, expiration)

        assert creds.org_uuid == org_uuid
        assert creds.delegated_token == token
        assert creds.delegated_proof == proof
        assert creds.expiration == expiration

    def test_is_expired_false(self):
        """Test is_expired returns False for non-expired token."""
        expiration = datetime.now() + timedelta(minutes=15)
        creds = DelegatedTokenCredentials("org", "token", "proof", expiration)

        assert not creds.is_expired()

    def test_is_expired_true(self):
        """Test is_expired returns True for expired token."""
        expiration = datetime.now() - timedelta(minutes=1)
        creds = DelegatedTokenCredentials("org", "token", "proof", expiration)

        assert creds.is_expired()


class TestDelegatedTokenConfig:
    """Test DelegatedTokenConfig class."""

    def test_init(self):
        """Test initialization of DelegatedTokenConfig."""
        org_uuid = "test-org-uuid"
        provider = "aws"
        provider_auth = Mock(spec=DelegatedTokenProvider)

        config = DelegatedTokenConfig(org_uuid, provider, provider_auth)

        assert config.org_uuid == org_uuid
        assert config.provider == provider
        assert config.provider_auth == provider_auth


class TestGetDelegatedTokenUrl:
    """Test get_delegated_token_url function."""

    def test_get_delegated_token_url(self):
        """Test URL construction."""
        config = Configuration()
        config.host = "https://api.datadoghq.com"

        url = get_delegated_token_url(config)

        assert url == "https://api.datadoghq.com/api/v2/delegated-token"


class TestParseDelegatedTokenResponse:
    """Test parse_delegated_token_response function."""

    def test_parse_valid_response(self):
        """Test parsing valid token response."""
        org_uuid = "test-org-uuid"
        proof = "test-proof"
        token = "test-access-token"
        expires = str(int((datetime.now() + timedelta(minutes=15)).timestamp()))

        response_data = json.dumps({"data": {"attributes": {"access_token": token, "expires": expires}}})

        creds = parse_delegated_token_response(response_data, org_uuid, proof)

        assert creds.org_uuid == org_uuid
        assert creds.delegated_token == token
        assert creds.delegated_proof == proof
        assert isinstance(creds.expiration, datetime)

    def test_parse_invalid_json(self):
        """Test parsing invalid JSON response."""
        with pytest.raises(ApiValueError, match="Failed to parse token response"):
            parse_delegated_token_response("invalid json", "org", "proof")


class TestGetDelegatedToken:
    """Test get_delegated_token function."""

    @patch("datadog_api_client.delegated_auth.rest.RESTClientObject")
    def test_get_delegated_token_success(self, mock_rest_client_class):
        """Test successful token retrieval."""
        mock_rest_client = Mock()
        mock_rest_client_class.return_value = mock_rest_client

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = json.dumps({"data": {"attributes": {"access_token": "test-token"}}}).encode("utf-8")
        mock_rest_client.request.return_value = mock_response

        org_uuid = "test-org-uuid"
        proof = "test-proof"
        config = Configuration()

        creds = get_delegated_token(org_uuid, proof, config)

        assert creds.org_uuid == org_uuid
        assert creds.delegated_token == "test-token"
        assert creds.delegated_proof == proof

    @patch("datadog_api_client.delegated_auth.rest.RESTClientObject")
    def test_get_delegated_token_http_error(self, mock_rest_client_class):
        """Test token retrieval with HTTP error."""
        mock_rest_client = Mock()
        mock_rest_client_class.return_value = mock_rest_client

        mock_response = Mock()
        mock_response.status = 401
        mock_rest_client.request.return_value = mock_response

        config = Configuration()

        with pytest.raises(ApiValueError, match="Failed to get token: 401"):
            get_delegated_token("org", "proof", config)
