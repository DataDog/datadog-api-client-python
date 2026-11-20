"""
Update the RUM configuration returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_config_api import RUMConfigApi
from datadog_api_client.v2.model.rum_config_type import RUMConfigType
from datadog_api_client.v2.model.rum_config_update_attributes import RUMConfigUpdateAttributes
from datadog_api_client.v2.model.rum_config_update_data import RUMConfigUpdateData
from datadog_api_client.v2.model.rum_config_update_request import RUMConfigUpdateRequest

body = RUMConfigUpdateRequest(
    data=RUMConfigUpdateData(
        attributes=RUMConfigUpdateAttributes(
            enforced_application_tags=True,
        ),
        type=RUMConfigType.RUM_CONFIG,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_rum_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMConfigApi(api_client)
    response = api_instance.update_rum_config(body=body)

    print(response)
