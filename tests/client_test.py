"""Client integration tests for delegated authentication functionality.

This test module provides comprehensive integration tests for the ApiClient
with delegated token authentication, similar to the Go client tests.
"""

import pytest
from datetime import datetime, timedelta
from unittest.mock import patch

from datadog_api_client.api_client import ApiClient
from datadog_api_client.configuration import Configuration
from datadog_api_client.delegated_auth import (
    DelegatedTokenCredentials,
    DelegatedTokenConfig,
    DelegatedTokenProvider,
)
from datadog_api_client.aws import AWSAuth
from datadog_api_client.exceptions import ApiValueError


FAKE_TOKEN = "fake-token"
FAKE_ORG_UUID = "1234"
FAKE_PROOF = "proof"


class MockDelegatedTokenProvider(DelegatedTokenProvider):
    """Mock delegated token provider for testing."""

    def __init__(self, token=FAKE_TOKEN, org_uuid=FAKE_ORG_UUID, proof=FAKE_PROOF, expiration_minutes=10):
        self.token = token
        self.org_uuid = org_uuid
        self.proof = proof
        self.expiration_minutes = expiration_minutes
        self.authenticate_calls = []

    def authenticate(self, config: DelegatedTokenConfig, api_config: Configuration) -> DelegatedTokenCredentials:
        """Mock authenticate method."""
        self.authenticate_calls.append(config)
        expiration = datetime.now() + timedelta(minutes=self.expiration_minutes)
        return DelegatedTokenCredentials(
            org_uuid=self.org_uuid, delegated_token=self.token, delegated_proof=self.proof, expiration=expiration
        )


class ExpiredMockProvider(MockDelegatedTokenProvider):
    """Mock provider that returns expired tokens."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expiration_minutes = -16  # Expired 16 minutes ago


class TestClientDelegatedAuthentication:
    """Test client integration with delegated authentication."""

    def test_delegated_pre_authenticate(self):
        """Test delegated token pre-authentication flow."""
        # Create mock provider
        mock_provider = MockDelegatedTokenProvider()

        # Create configuration with delegated auth
        config = Configuration()
        config.delegated_auth_provider = mock_provider
        config.delegated_auth_org_uuid = FAKE_ORG_UUID

        # Create API client
        api_client = ApiClient(config)

        headers = {}
        api_client.use_delegated_token_auth(headers)

        # Verify headers were set
        assert "Authorization" in headers
        assert headers["Authorization"] == f"Bearer {FAKE_TOKEN}"

        # Get the cached token
        token = api_client.configuration._delegated_token_credentials
        assert token is not None
        assert token.delegated_token == FAKE_TOKEN
        assert token.org_uuid == FAKE_ORG_UUID
        assert token.delegated_proof == FAKE_PROOF
        assert not token.is_expired()

        # Verify provider was called
        assert len(mock_provider.authenticate_calls) == 1
        assert mock_provider.authenticate_calls[0].org_uuid == FAKE_ORG_UUID

    def test_delegated_no_pre_authenticate(self):
        """Test delegated token authentication without pre-authentication."""
        # Create mock provider
        mock_provider = MockDelegatedTokenProvider()

        config = Configuration()
        config.delegated_auth_provider = mock_provider
        config.delegated_auth_org_uuid = FAKE_ORG_UUID

        # Create API client
        api_client = ApiClient(config)

        # Test use_delegated_token_auth (simulates API call header generation)
        headers = {}
        api_client.use_delegated_token_auth(headers)

        # Verify headers were set correctly
        assert "Authorization" in headers
        assert headers["Authorization"] == f"Bearer {FAKE_TOKEN}"

        # Verify provider was called once for token generation
        assert len(mock_provider.authenticate_calls) == 1

    def test_delegated_re_authenticate(self):
        """Test delegated token re-authentication when token expires."""
        # Create two mock providers - first with expired token, second with valid token
        expired_provider = ExpiredMockProvider()
        valid_provider = MockDelegatedTokenProvider()

        # Create configuration
        config = Configuration()
        config.delegated_auth_provider = expired_provider
        config.delegated_auth_org_uuid = FAKE_ORG_UUID

        # Create API client and get initial (expired) token
        api_client = ApiClient(config)

        # First call gets expired token
        headers = {}
        api_client.use_delegated_token_auth(headers)
        assert "Authorization" in headers
        assert headers["Authorization"] == f"Bearer {FAKE_TOKEN}"

        # Verify expired token was created
        assert api_client.configuration._delegated_token_credentials.is_expired()

        # Switch to valid provider for re-authentication
        config.delegated_auth_provider = valid_provider

        # Second call should re-authenticate due to expired token
        headers2 = {}
        api_client.use_delegated_token_auth(headers2)
        assert "Authorization" in headers2
        assert headers2["Authorization"] == f"Bearer {FAKE_TOKEN}"

        # Verify new token is not expired
        assert not api_client.configuration._delegated_token_credentials.is_expired()

        # Verify both providers were called
        assert len(expired_provider.authenticate_calls) == 1
        assert len(valid_provider.authenticate_calls) == 1

    def test_delegated_token_caching(self):
        """Test that delegated tokens are cached and reused when not expired."""
        # Create mock provider
        mock_provider = MockDelegatedTokenProvider()

        # Create configuration
        config = Configuration()
        config.delegated_auth_provider = mock_provider
        config.delegated_auth_org_uuid = FAKE_ORG_UUID

        # Create API client
        api_client = ApiClient(config)

        # Multiple calls to use_delegated_token_auth
        headers1 = {}
        api_client.use_delegated_token_auth(headers1)

        headers2 = {}
        api_client.use_delegated_token_auth(headers2)

        headers3 = {}
        api_client.use_delegated_token_auth(headers3)

        # All should have same token
        assert headers1["Authorization"] == headers2["Authorization"] == headers3["Authorization"]

        # Provider should only be called once (token cached)
        assert len(mock_provider.authenticate_calls) == 1

    @patch.dict(
        "os.environ",
        {
            "AWS_ACCESS_KEY_ID": "fake-access-key-id",
            "AWS_SECRET_ACCESS_KEY": "fake-secret-access-key",
            "AWS_SESSION_TOKEN": "fake-session-token",
        },
    )
    def test_delegated_with_aws_provider(self):
        """Test delegated authentication with real AWS provider (mocked token endpoint)."""
        # Create AWS auth provider
        aws_auth = AWSAuth()

        # Create configuration
        config = Configuration()
        config.delegated_auth_provider = aws_auth
        config.delegated_auth_org_uuid = FAKE_ORG_UUID

        # Mock the get_delegated_token function called by AWS provider
        mock_creds = DelegatedTokenCredentials(
            org_uuid=FAKE_ORG_UUID,
            delegated_token=FAKE_TOKEN,
            delegated_proof=FAKE_PROOF,
            expiration=datetime.now() + timedelta(minutes=15),
        )

        with patch("datadog_api_client.aws.get_delegated_token", return_value=mock_creds):
            # Create API client
            api_client = ApiClient(config)

            # Test header generation
            headers = {}
            api_client.use_delegated_token_auth(headers)
            assert headers["Authorization"] == f"Bearer {FAKE_TOKEN}"

            # Verify token was cached
            assert api_client.configuration._delegated_token_credentials.delegated_token == FAKE_TOKEN
            assert api_client.configuration._delegated_token_credentials.org_uuid == FAKE_ORG_UUID

    def test_api_key_authentication_comparison(self):
        """Test traditional API key authentication for comparison with delegated auth."""
        # Create configuration with API keys
        config = Configuration()
        config.api_key = {"apiKeyAuth": "test-api-key", "appKeyAuth": "test-app-key"}

        # Create API client
        api_client = ApiClient(config)

        # Test that no delegated auth is used when not configured
        headers = {}
        api_client.use_delegated_token_auth(headers)

        # Headers should be empty (no delegated token)
        assert "Authorization" not in headers

        # This simulates how API keys would be added in actual API calls
        # (API key authentication is handled separately in the client)

    def test_delegated_auth_error_handling(self):
        """Test error handling in delegated authentication."""
        # Test with no configuration - should simply not add auth header
        config = Configuration()
        api_client = ApiClient(config)

        headers = {}
        api_client.use_delegated_token_auth(headers)
        # Should not add Authorization header when no provider configured
        assert "Authorization" not in headers

        # Test with provider that raises an exception
        class FailingProvider(DelegatedTokenProvider):
            def authenticate(self, config, api_config):
                raise Exception("Authentication failed")

        config.delegated_auth_provider = FailingProvider()
        config.delegated_auth_org_uuid = FAKE_ORG_UUID

        api_client = ApiClient(config)
        with pytest.raises(ApiValueError, match="Failed to get delegated token"):
            headers = {}
            api_client.use_delegated_token_auth(headers)

    def test_multiple_api_clients_isolation(self):
        """Test that multiple API clients with different configs work independently."""
        # Create two different mock providers
        provider1 = MockDelegatedTokenProvider(token="token1", org_uuid="org1")
        provider2 = MockDelegatedTokenProvider(token="token2", org_uuid="org2")

        # Create two configurations
        config1 = Configuration()
        config1.delegated_auth_provider = provider1
        config1.delegated_auth_org_uuid = "org1"

        config2 = Configuration()
        config2.delegated_auth_provider = provider2
        config2.delegated_auth_org_uuid = "org2"

        # Create two API clients
        client1 = ApiClient(config1)
        client2 = ApiClient(config2)

        # Test header generation for both
        headers1 = {}
        client1.use_delegated_token_auth(headers1)

        headers2 = {}
        client2.use_delegated_token_auth(headers2)

        assert headers1["Authorization"] == "Bearer token1"
        assert headers2["Authorization"] == "Bearer token2"

        # Verify they have different cached tokens
        assert client1.configuration._delegated_token_credentials.delegated_token == "token1"
        assert client1.configuration._delegated_token_credentials.org_uuid == "org1"
        assert client2.configuration._delegated_token_credentials.delegated_token == "token2"
        assert client2.configuration._delegated_token_credentials.org_uuid == "org2"


class TestClientDelegatedAuthenticationWithRealMocks:
    """Test client integration with more realistic mocking scenarios."""

    def test_token_refresh_sequence(self):
        """Test the complete token refresh sequence over time."""
        # Create a provider that tracks call count
        call_count = 0

        class CountingProvider(DelegatedTokenProvider):
            def authenticate(self, config, api_config):
                nonlocal call_count
                call_count += 1

                # First call returns short-lived token, second call returns long-lived
                if call_count == 1:
                    expiration = datetime.now() + timedelta(seconds=1)  # Very short lived
                else:
                    expiration = datetime.now() + timedelta(minutes=30)  # Long lived

                return DelegatedTokenCredentials(
                    org_uuid=config.org_uuid,
                    delegated_token=f"token-{call_count}",
                    delegated_proof="proof",
                    expiration=expiration,
                )

        # Setup
        config = Configuration()
        config.delegated_auth_provider = CountingProvider()
        config.delegated_auth_org_uuid = FAKE_ORG_UUID

        api_client = ApiClient(config)

        # First call
        headers1 = {}
        api_client.use_delegated_token_auth(headers1)
        assert headers1["Authorization"] == "Bearer token-1"
        assert call_count == 1

        # Immediate second call should reuse token
        headers2 = {}
        api_client.use_delegated_token_auth(headers2)
        assert headers2["Authorization"] == "Bearer token-1"
        assert call_count == 1  # No new call

        # Force expiration by manipulating the cached token
        api_client.configuration._delegated_token_credentials.expiration = datetime.now() - timedelta(minutes=1)

        # Third call should refresh due to expiration
        headers3 = {}
        api_client.use_delegated_token_auth(headers3)
        assert headers3["Authorization"] == "Bearer token-2"
        assert call_count == 2  # New call made
