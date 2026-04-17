"""
Export security monitoring resource to Terraform returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_terraform_resource_type import (
    SecurityMonitoringTerraformResourceType,
)

# there is a valid "suppression" in the system
SUPPRESSION_DATA_ID = environ["SUPPRESSION_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["export_security_monitoring_terraform_resource"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.export_security_monitoring_terraform_resource(
        resource_type=SecurityMonitoringTerraformResourceType.SUPPRESSIONS,
        resource_id=SUPPRESSION_DATA_ID,
    )

    print(response)
