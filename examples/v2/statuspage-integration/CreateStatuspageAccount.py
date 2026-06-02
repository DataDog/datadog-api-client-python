"""
Create the Statuspage account returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.statuspage_integration_api import StatuspageIntegrationApi
from datadog_api_client.v2.model.statuspage_account_create_attributes import StatuspageAccountCreateAttributes
from datadog_api_client.v2.model.statuspage_account_create_data import StatuspageAccountCreateData
from datadog_api_client.v2.model.statuspage_account_create_request import StatuspageAccountCreateRequest
from datadog_api_client.v2.model.statuspage_account_type import StatuspageAccountType

body = StatuspageAccountCreateRequest(
    data=StatuspageAccountCreateData(
        attributes=StatuspageAccountCreateAttributes(
            api_key="00000000-0000-0000-0000-000000000000",
        ),
        type=StatuspageAccountType.STATUSPAGE_ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatuspageIntegrationApi(api_client)
    response = api_instance.create_statuspage_account(body=body)

    print(response)
