"""
Update the Statuspage account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.statuspage_integration_api import StatuspageIntegrationApi
from datadog_api_client.v2.model.statuspage_account_type import StatuspageAccountType
from datadog_api_client.v2.model.statuspage_account_update_attributes import StatuspageAccountUpdateAttributes
from datadog_api_client.v2.model.statuspage_account_update_data import StatuspageAccountUpdateData
from datadog_api_client.v2.model.statuspage_account_update_request import StatuspageAccountUpdateRequest

body = StatuspageAccountUpdateRequest(
    data=StatuspageAccountUpdateData(
        attributes=StatuspageAccountUpdateAttributes(
            api_key="00000000-0000-0000-0000-000000000000",
        ),
        type=StatuspageAccountType.STATUSPAGE_ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatuspageIntegrationApi(api_client)
    response = api_instance.update_statuspage_account(body=body)

    print(response)
