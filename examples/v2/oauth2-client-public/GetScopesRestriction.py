"""
Get an OAuth2 client scopes restriction returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.o_auth2_client_public_api import OAuth2ClientPublicApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["get_scopes_restriction"] = True
with ApiClient(configuration) as api_client:
    api_instance = OAuth2ClientPublicApi(api_client)
    response = api_instance.get_scopes_restriction(
        client_uuid=UUID("fafa8e1c-36a5-11f0-a83d-da7ad0900001"),
    )

    print(response)
