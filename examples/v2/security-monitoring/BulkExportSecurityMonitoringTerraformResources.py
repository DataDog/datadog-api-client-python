"""
Export security monitoring resources to Terraform returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_terraform_bulk_export_attributes import (
    SecurityMonitoringTerraformBulkExportAttributes,
)
from datadog_api_client.v2.model.security_monitoring_terraform_bulk_export_data import (
    SecurityMonitoringTerraformBulkExportData,
)
from datadog_api_client.v2.model.security_monitoring_terraform_bulk_export_request import (
    SecurityMonitoringTerraformBulkExportRequest,
)
from datadog_api_client.v2.model.security_monitoring_terraform_resource_type import (
    SecurityMonitoringTerraformResourceType,
)

# there is a valid "suppression" in the system
SUPPRESSION_DATA_ID = environ["SUPPRESSION_DATA_ID"]

body = SecurityMonitoringTerraformBulkExportRequest(
    data=SecurityMonitoringTerraformBulkExportData(
        attributes=SecurityMonitoringTerraformBulkExportAttributes(
            resource_ids=[
                SUPPRESSION_DATA_ID,
            ],
        ),
        type="bulk_export_resources",
    ),
)

configuration = Configuration()
configuration.unstable_operations["bulk_export_security_monitoring_terraform_resources"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.bulk_export_security_monitoring_terraform_resources(
        resource_type=SecurityMonitoringTerraformResourceType.SUPPRESSIONS, body=body
    )

    print(response.read())
