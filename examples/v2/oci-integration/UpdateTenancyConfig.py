"""
Update tenancy config returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.oci_integration_api import OCIIntegrationApi
from datadog_api_client.v2.model.oci_metrics_config import OCIMetricsConfig
from datadog_api_client.v2.model.update_tenancy_config import UpdateTenancyConfig
from datadog_api_client.v2.model.update_tenancy_config_data import UpdateTenancyConfigData
from datadog_api_client.v2.model.update_tenancy_config_data_attributes import UpdateTenancyConfigDataAttributes
from datadog_api_client.v2.model.update_tenancy_config_data_type import UpdateTenancyConfigDataType

# there is a valid "oci_tenancy" resource in the system
OCI_TENANCY_DATA_ID = environ["OCI_TENANCY_DATA_ID"]

body = UpdateTenancyConfig(
    data=UpdateTenancyConfigData(
        attributes=UpdateTenancyConfigDataAttributes(
            home_region="us-sanjose-1",
            metrics_config=OCIMetricsConfig(
                compartment_tag_filters=[
                    "datadog:true",
                    "env:prod",
                ],
                enabled=False,
                excluded_services=[],
            ),
            resource_collection_enabled=False,
            user_ocid="ocid1.user.test_updated",
        ),
        id=OCI_TENANCY_DATA_ID,
        type=UpdateTenancyConfigDataType.OCI_TENANCY,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OCIIntegrationApi(api_client)
    response = api_instance.update_tenancy_config(tenancy_ocid=OCI_TENANCY_DATA_ID, body=body)

    print(response)
