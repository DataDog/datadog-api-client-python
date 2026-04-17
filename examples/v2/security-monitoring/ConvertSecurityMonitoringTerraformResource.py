"""
Convert security monitoring resource to Terraform returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_terraform_convert_attributes import (
    SecurityMonitoringTerraformConvertAttributes,
)
from datadog_api_client.v2.model.security_monitoring_terraform_convert_data import (
    SecurityMonitoringTerraformConvertData,
)
from datadog_api_client.v2.model.security_monitoring_terraform_convert_request import (
    SecurityMonitoringTerraformConvertRequest,
)
from datadog_api_client.v2.model.security_monitoring_terraform_resource_type import (
    SecurityMonitoringTerraformResourceType,
)

body = SecurityMonitoringTerraformConvertRequest(
    data=SecurityMonitoringTerraformConvertData(
        type="convert_resource",
        id="abc-123",
        attributes=SecurityMonitoringTerraformConvertAttributes(
            resource_json=dict(
                [
                    ("enabled", "True"),
                    ("name", "Example-Security-Monitoring"),
                    ("rule_query", "source:cloudtrail"),
                    ("suppression_query", "env:test"),
                ]
            ),
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["convert_security_monitoring_terraform_resource"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.convert_security_monitoring_terraform_resource(
        resource_type=SecurityMonitoringTerraformResourceType.SUPPRESSIONS, body=body
    )

    print(response)
