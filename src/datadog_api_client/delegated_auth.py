# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.

import json
from datetime import datetime, timedelta
from urllib.parse import urljoin

from datadog_api_client import rest
from datadog_api_client.configuration import Configuration
from datadog_api_client.exceptions import ApiValueError


TOKEN_URL_ENDPOINT = "/api/v2/delegated-token"
AUTHORIZATION_TYPE = "Delegated"
APPLICATION_JSON = "application/json"


class DelegatedTokenCredentials:
    """Credentials for delegated token authentication."""

    def __init__(self, org_uuid: str, delegated_token: str, delegated_proof: str, expiration: datetime):
        self.org_uuid = org_uuid
        self.delegated_token = delegated_token
        self.delegated_proof = delegated_proof
        self.expiration = expiration

    def is_expired(self) -> bool:
        """Check if the token is expired."""
        return datetime.now() >= self.expiration


class DelegatedTokenConfig:
    """Configuration for delegated token authentication."""

    def __init__(self, org_uuid: str, provider: str, provider_auth: "DelegatedTokenProvider"):
        self.org_uuid = org_uuid
        self.provider = provider
        self.provider_auth = provider_auth


class DelegatedTokenProvider:
    """Abstract base class for delegated token providers."""

    def __init__(self):
        self._rest_client = None

    def authenticate(self, config: DelegatedTokenConfig, api_config: Configuration) -> DelegatedTokenCredentials:
        """Authenticate and return delegated token credentials.

        :param config: Delegated token configuration
        :param api_config: API client configuration with host and other settings
        :return: DelegatedTokenCredentials object
        """
        raise NotImplementedError("Subclasses must implement authenticate method")


def get_delegated_token(
    org_uuid: str, delegated_auth_proof: str, config: Configuration, provider=None
) -> DelegatedTokenCredentials:
    """Get a delegated token from the Datadog API.

    :param org_uuid: Organization UUID
    :param delegated_auth_proof: Authentication proof string
    :param config: Configuration object with host and other settings
    :param provider: Optional provider instance that may have a cached REST client
    :return: DelegatedTokenCredentials object
    :raises: ApiValueError if the request fails
    """
    url = get_delegated_token_url(config)

    # Use provider's cached REST client if available, otherwise create a new one
    if provider and hasattr(provider, "_rest_client") and provider._rest_client is not None:
        rest_client = provider._rest_client
    else:
        rest_client = rest.RESTClientObject(config)
        # Cache it in the provider if provided
        if provider:
            provider._rest_client = rest_client

    headers = {
        "Content-Type": APPLICATION_JSON,
        "Authorization": f"{AUTHORIZATION_TYPE} {delegated_auth_proof}",
        "Content-Length": "0",
    }

    try:
        response = rest_client.request(method="POST", url=url, headers=headers, body="", preload_content=True)

        if response.status != 200:
            raise ApiValueError(f"Failed to get token: {response.status}")

        response_data = response.data.decode("utf-8")
        creds = parse_delegated_token_response(response_data, org_uuid, delegated_auth_proof)
        return creds

    except Exception as e:
        raise ApiValueError(f"Failed to get delegated token: {str(e)}")


def parse_delegated_token_response(
    response_data: str, org_uuid: str, delegated_auth_proof: str
) -> DelegatedTokenCredentials:
    """Parse the delegated token response.

    :param response_data: JSON response data as string
    :param org_uuid: Organization UUID
    :param delegated_auth_proof: Authentication proof string
    :return: DelegatedTokenCredentials object
    :raises: ApiValueError if parsing fails
    """
    try:
        token_response = json.loads(response_data)
    except json.JSONDecodeError as e:
        raise ApiValueError(f"Failed to parse token response: {str(e)}")

    # Get attributes from the response
    data_response = token_response.get("data")
    if not data_response:
        raise ApiValueError(f"Failed to get data from response: {token_response}")

    attributes = data_response.get("attributes")
    if not attributes:
        raise ApiValueError(f"Failed to get attributes from response: {token_response}")

    # Get the access token from the response
    token = attributes.get("access_token")
    if not token:
        raise ApiValueError(f"Failed to get token from response: {token_response}")

    # get expiration time from the response, defualt to 15 min
    expiration_time = datetime.now() + timedelta(minutes=15)
    expires_str = attributes.get("expires")
    if expires_str:
        try:
            expiration_int = int(expires_str)
            expiration_time = datetime.fromtimestamp(expiration_int)
        except (ValueError, TypeError):
            # Use default expiration if parsing fails
            pass

    return DelegatedTokenCredentials(
        org_uuid=org_uuid, delegated_token=token, delegated_proof=delegated_auth_proof, expiration=expiration_time
    )


def get_delegated_token_url(config: Configuration) -> str:
    """Get the URL for the delegated token endpoint.

    :param config: Configuration object
    :return: Full URL for the delegated token endpoint
    """
    base_url = config.host
    return urljoin(base_url, TOKEN_URL_ENDPOINT)
