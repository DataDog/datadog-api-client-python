"""
Update an Opsgenie account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.opsgenie_integration_api import OpsgenieIntegrationApi
from datadog_api_client.v2.model.opsgenie_account_type import OpsgenieAccountType
from datadog_api_client.v2.model.opsgenie_account_update_attributes import OpsgenieAccountUpdateAttributes
from datadog_api_client.v2.model.opsgenie_account_update_data import OpsgenieAccountUpdateData
from datadog_api_client.v2.model.opsgenie_account_update_request import OpsgenieAccountUpdateRequest
from datadog_api_client.v2.model.opsgenie_service_region_type import OpsgenieServiceRegionType

body = OpsgenieAccountUpdateRequest(
    data=OpsgenieAccountUpdateData(
        attributes=OpsgenieAccountUpdateAttributes(
            api_key="00000000-0000-0000-0000-000000000000",
            region=OpsgenieServiceRegionType.US,
        ),
        id="596da4af-0563-4097-90ff-07230c3f9db3",
        type=OpsgenieAccountType.OPSGENIE_ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OpsgenieIntegrationApi(api_client)
    response = api_instance.update_opsgenie_account(account_id="account_id", body=body)

    print(response)
