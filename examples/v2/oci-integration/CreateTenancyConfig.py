"""
Create tenancy config returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.oci_integration_api import OCIIntegrationApi
from datadog_api_client.v2.model.auth_credentials import AuthCredentials
from datadog_api_client.v2.model.create_tenancy_config import CreateTenancyConfig
from datadog_api_client.v2.model.create_tenancy_config_data import CreateTenancyConfigData
from datadog_api_client.v2.model.create_tenancy_config_data_attributes import CreateTenancyConfigDataAttributes
from datadog_api_client.v2.model.create_tenancy_config_data_type import CreateTenancyConfigDataType
from datadog_api_client.v2.model.oci_logs_config import OCILogsConfig
from datadog_api_client.v2.model.oci_metrics_config import OCIMetricsConfig

body = CreateTenancyConfig(
    data=CreateTenancyConfigData(
        attributes=CreateTenancyConfigDataAttributes(
            auth_credentials=AuthCredentials(
                fingerprint="a7:b5:54:f2:da:a2:d7:b0:ed:f4:79:47:93:64:12:b1",
                private_key="-----BEGIN PRIVATE KEY-----\no9kEwoumo8yHVn5Ztp4F2cxaD6+MzSJ/I6WesPyePUD7sPeorXByg1UNOXyzqDub\n/aU4/sNo2f8epM9l7QGiCtY=\n-----END PRIVATE KEY-----",
            ),
            config_version=2,
            home_region="us-ashburn-1",
            logs_config=OCILogsConfig(
                compartment_tag_filters=[
                    "datadog:true",
                    "env:prod",
                ],
                enabled=True,
                enabled_services=[
                    "oacnativeproduction",
                ],
            ),
            metrics_config=OCIMetricsConfig(
                compartment_tag_filters=[
                    "datadog:true",
                    "env:prod",
                ],
                enabled=True,
                excluded_services=[
                    "oci_compute",
                ],
            ),
            resource_collection_enabled=True,
            user_ocid="ocid1.user.test",
        ),
        id="ocid1.tenancy.dummy_value",
        type=CreateTenancyConfigDataType.OCI_TENANCY,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OCIIntegrationApi(api_client)
    response = api_instance.create_tenancy_config(body=body)

    print(response)
