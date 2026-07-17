"""
Validate entity context sync credentials returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_integration_config_resource_type import (
    SecurityMonitoringIntegrationConfigResourceType,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_secrets import (
    SecurityMonitoringIntegrationConfigSecrets,
)
from datadog_api_client.v2.model.security_monitoring_integration_credentials_validate_attributes import (
    SecurityMonitoringIntegrationCredentialsValidateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_integration_credentials_validate_data import (
    SecurityMonitoringIntegrationCredentialsValidateData,
)
from datadog_api_client.v2.model.security_monitoring_integration_credentials_validate_request import (
    SecurityMonitoringIntegrationCredentialsValidateRequest,
)
from datadog_api_client.v2.model.security_monitoring_integration_type import SecurityMonitoringIntegrationType

body = SecurityMonitoringIntegrationCredentialsValidateRequest(
    data=SecurityMonitoringIntegrationCredentialsValidateData(
        attributes=SecurityMonitoringIntegrationCredentialsValidateAttributes(
            domain="siem-test.com",
            integration_type=SecurityMonitoringIntegrationType.GOOGLE_WORKSPACE,
            secrets=SecurityMonitoringIntegrationConfigSecrets([("admin_email", "test@example.com")]),
        ),
        type=SecurityMonitoringIntegrationConfigResourceType.INTEGRATION_CONFIG,
    ),
)

configuration = Configuration()
configuration.unstable_operations["validate_security_monitoring_integration_credentials"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.validate_security_monitoring_integration_credentials(body=body)
