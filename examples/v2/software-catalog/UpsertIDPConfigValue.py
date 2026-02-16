"""
Create or update IDP configuration returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi
from datadog_api_client.v2.model.idp_config_request import IDPConfigRequest
from datadog_api_client.v2.model.idp_config_request_attributes import IDPConfigRequestAttributes
from datadog_api_client.v2.model.idp_config_request_data import IDPConfigRequestData
from datadog_api_client.v2.model.idp_config_type import IDPConfigType
from datadog_api_client.v2.model.idp_config_value_item import IDPConfigValueItem

body = IDPConfigRequest(
    data=IDPConfigRequestData(
        attributes=IDPConfigRequestAttributes(
            value=[
                IDPConfigValueItem([("displayName", "My Dashboard"), ("id", "dashboard-1")]),
            ],
        ),
        type=IDPConfigType.IDP_CONFIG,
    ),
)

configuration = Configuration()
configuration.unstable_operations["upsert_idp_config_value"] = True
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    api_instance.upsert_idp_config_value(config_name="idp_pinned_dashboards", body=body)
