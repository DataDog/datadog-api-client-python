"""
Create a new Opsgenie account returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.opsgenie_integration_api import OpsgenieIntegrationApi
from datadog_api_client.v2.model.opsgenie_account_create_attributes import OpsgenieAccountCreateAttributes
from datadog_api_client.v2.model.opsgenie_account_create_data import OpsgenieAccountCreateData
from datadog_api_client.v2.model.opsgenie_account_create_request import OpsgenieAccountCreateRequest
from datadog_api_client.v2.model.opsgenie_account_type import OpsgenieAccountType
from datadog_api_client.v2.model.opsgenie_service_region_type import OpsgenieServiceRegionType

body = OpsgenieAccountCreateRequest(
    data=OpsgenieAccountCreateData(
        attributes=OpsgenieAccountCreateAttributes(
            api_key="00000000-0000-0000-0000-000000000000",
            region=OpsgenieServiceRegionType.US,
        ),
        type=OpsgenieAccountType.OPSGENIE_ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OpsgenieIntegrationApi(api_client)
    response = api_instance.create_opsgenie_account(body=body)

    print(response)
