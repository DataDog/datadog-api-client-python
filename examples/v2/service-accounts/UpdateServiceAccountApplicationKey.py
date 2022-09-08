"""
Edit an application key for this service account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi
from datadog_api_client.v2.model.application_key_update_attributes import ApplicationKeyUpdateAttributes
from datadog_api_client.v2.model.application_key_update_data import ApplicationKeyUpdateData
from datadog_api_client.v2.model.application_key_update_request import ApplicationKeyUpdateRequest
from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType

body = ApplicationKeyUpdateRequest(
    data=ApplicationKeyUpdateData(
        attributes=ApplicationKeyUpdateAttributes(
            name="Application Key for managing dashboards",
            scopes=[
                "dashboards_read",
                "dashboards_write",
                "dashboards_public_share",
            ],
        ),
        id="00112233-4455-6677-8899-aabbccddeeff",
        type=ApplicationKeysType.APPLICATION_KEYS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.update_service_account_application_key(
        service_account_id="00000000-0000-1234-0000-000000000000", app_key_id="app_key_id", body=body
    )

    print(response)
