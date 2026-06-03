"""
Create the RUM configuration returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_config_api import RumConfigApi
from datadog_api_client.v2.model.rum_config_create_attributes import RumConfigCreateAttributes
from datadog_api_client.v2.model.rum_config_create_data import RumConfigCreateData
from datadog_api_client.v2.model.rum_config_create_request import RumConfigCreateRequest
from datadog_api_client.v2.model.rum_config_type import RumConfigType

body = RumConfigCreateRequest(
    data=RumConfigCreateData(
        attributes=RumConfigCreateAttributes(
            enforced_application_tags=True,
        ),
        type=RumConfigType.RUM_CONFIG,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_rum_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumConfigApi(api_client)
    response = api_instance.create_rum_config(body=body)

    print(response)
