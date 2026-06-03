"""
Update the RUM configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_config_api import RumConfigApi
from datadog_api_client.v2.model.rum_config_type import RumConfigType
from datadog_api_client.v2.model.rum_config_update_attributes import RumConfigUpdateAttributes
from datadog_api_client.v2.model.rum_config_update_data import RumConfigUpdateData
from datadog_api_client.v2.model.rum_config_update_request import RumConfigUpdateRequest

body = RumConfigUpdateRequest(
    data=RumConfigUpdateData(
        attributes=RumConfigUpdateAttributes(
            enforced_application_tags=True,
        ),
        type=RumConfigType.RUM_CONFIG,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_rum_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumConfigApi(api_client)
    response = api_instance.update_rum_config(body=body)

    print(response)
