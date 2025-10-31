"""Tests for AWS authentication functionality."""

import os
import pytest
from unittest.mock import Mock, patch

from datadog_api_client.aws import (
    AWSAuth,
    AWSCredentials,
    SigningData,
    PROVIDER_AWS,
)
from datadog_api_client.configuration import Configuration
from datadog_api_client.delegated_auth import DelegatedTokenConfig
from datadog_api_client.exceptions import ApiValueError


class TestAWSCredentials:
    """Test AWSCredentials class."""

    def test_init(self):
        """Test initialization of AWSCredentials."""
        access_key = "test-access-key"
        secret_key = "test-secret-key"
        session_token = "test-session-token"

        creds = AWSCredentials(access_key, secret_key, session_token)

        assert creds.access_key_id == access_key
        assert creds.secret_access_key == secret_key
        assert creds.session_token == session_token


class TestSigningData:
    """Test SigningData class."""

    def test_init(self):
        """Test initialization of SigningData."""
        headers_encoded = "encoded-headers"
        body_encoded = "encoded-body"
        url_encoded = "encoded-url"
        method = "POST"

        data = SigningData(headers_encoded, body_encoded, url_encoded, method)

        assert data.headers_encoded == headers_encoded
        assert data.body_encoded == body_encoded
        assert data.url_encoded == url_encoded
        assert data.method == method


class TestAWSAuth:
    """Test AWSAuth class."""

    def test_init_default_region(self):
        """Test initialization with default region."""
        auth = AWSAuth()
        assert auth.aws_region is None

    def test_init_custom_region(self):
        """Test initialization with custom region."""
        region = "us-west-2"
        auth = AWSAuth(aws_region=region)
        assert auth.aws_region == region

    @patch.dict(
        os.environ,
        {
            "AWS_ACCESS_KEY_ID": "test-access-key",
            "AWS_SECRET_ACCESS_KEY": "test-secret-key",
            "AWS_SESSION_TOKEN": "test-session-token",
        },
    )
    def test_get_credentials_success(self):
        """Test successful credential retrieval from environment."""
        auth = AWSAuth()
        creds = auth.get_credentials()

        assert creds.access_key_id == "test-access-key"
        assert creds.secret_access_key == "test-secret-key"
        assert creds.session_token == "test-session-token"

    @patch.dict(os.environ, {}, clear=True)
    def test_get_credentials_missing_access_key(self):
        """Test credential retrieval with missing access key."""
        auth = AWSAuth()

        with pytest.raises(ApiValueError, match="Missing AWS credentials"):
            auth.get_credentials()

    @patch.dict(os.environ, {"AWS_ACCESS_KEY_ID": "test-key"}, clear=True)
    def test_get_credentials_missing_secret_key(self):
        """Test credential retrieval with missing secret key."""
        auth = AWSAuth()

        with pytest.raises(ApiValueError, match="Missing AWS credentials"):
            auth.get_credentials()

    @patch.dict(
        os.environ, {"AWS_ACCESS_KEY_ID": "test-access-key", "AWS_SECRET_ACCESS_KEY": "test-secret-key"}, clear=True
    )
    def test_get_credentials_missing_session_token(self):
        """Test credential retrieval with missing session token."""
        auth = AWSAuth()

        with pytest.raises(ApiValueError, match="Missing AWS credentials"):
            auth.get_credentials()

    def test_get_connection_parameters_default_region(self):
        """Test connection parameters with default region."""
        auth = AWSAuth()
        url, region, host = auth._get_connection_parameters()

        assert url == "https://sts.amazonaws.com"
        assert region == "us-east-1"
        assert host == "sts.amazonaws.com"

    def test_get_connection_parameters_custom_region(self):
        """Test connection parameters with custom region."""
        auth = AWSAuth(aws_region="eu-west-1")
        url, region, host = auth._get_connection_parameters()

        assert url == "https://sts.eu-west-1.amazonaws.com"
        assert region == "eu-west-1"
        assert host == "sts.eu-west-1.amazonaws.com"

    @patch.dict(
        os.environ,
        {
            "AWS_ACCESS_KEY_ID": "AKIAIOSFODNN7EXAMPLE",
            "AWS_SECRET_ACCESS_KEY": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "AWS_SESSION_TOKEN": "test-session-token",
        },
    )
    def test_generate_aws_auth_data(self):
        """Test AWS authentication data generation."""
        auth = AWSAuth()
        org_uuid = "test-org-uuid"
        creds = auth.get_credentials()

        data = auth.generate_aws_auth_data(org_uuid, creds)

        assert isinstance(data, SigningData)
        assert data.method == "POST"
        assert data.headers_encoded  # Should be base64 encoded
        assert data.body_encoded  # Should be base64 encoded
        assert data.url_encoded  # Should be base64 encoded

    def test_generate_aws_auth_data_missing_org_uuid(self):
        """Test auth data generation with missing org UUID."""
        auth = AWSAuth()
        creds = AWSCredentials("key", "secret", "token")

        with pytest.raises(ApiValueError, match="Missing org UUID"):
            auth.generate_aws_auth_data("", creds)

    def test_generate_aws_auth_data_missing_credentials(self):
        """Test auth data generation with missing credentials."""
        auth = AWSAuth()

        with pytest.raises(ApiValueError, match="Missing AWS credentials"):
            auth.generate_aws_auth_data("org-uuid", None)

    def test_hmac256(self):
        """Test HMAC-SHA256 generation."""
        auth = AWSAuth()
        data = "test-data"
        key = b"test-key"

        result = auth._hmac256(data, key)

        assert isinstance(result, bytes)
        assert len(result) == 32  # SHA256 produces 32 bytes

    @patch("datadog_api_client.aws.get_delegated_token")
    @patch.dict(
        os.environ,
        {
            "AWS_ACCESS_KEY_ID": "test-access-key",
            "AWS_SECRET_ACCESS_KEY": "test-secret-key",
            "AWS_SESSION_TOKEN": "test-session-token",
        },
    )
    def test_authenticate_success(self, mock_get_delegated_token):
        """Test successful authentication."""
        # Mock the delegated token response
        mock_credentials = Mock()
        mock_get_delegated_token.return_value = mock_credentials

        auth = AWSAuth()
        config = DelegatedTokenConfig("test-org-uuid", PROVIDER_AWS, auth)
        api_config = Configuration()

        result = auth.authenticate(config, api_config)

        assert result == mock_credentials
        mock_get_delegated_token.assert_called_once()

    def test_authenticate_missing_org_uuid(self):
        """Test authentication with missing org UUID."""
        auth = AWSAuth()
        config = DelegatedTokenConfig("", PROVIDER_AWS, auth)
        api_config = Configuration()

        with pytest.raises(ApiValueError, match="Missing org UUID in config"):
            auth.authenticate(config, api_config)

    def test_authenticate_missing_config(self):
        """Test authentication with missing config."""
        auth = AWSAuth()
        api_config = Configuration()

        with pytest.raises(ApiValueError, match="Missing org UUID in config"):
            auth.authenticate(None, api_config)
