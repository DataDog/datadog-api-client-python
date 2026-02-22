"""
Revoke personal access token returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["revoke_personal_access_token"] = True
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    api_instance.revoke_personal_access_token(
        pat_uuid=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )
