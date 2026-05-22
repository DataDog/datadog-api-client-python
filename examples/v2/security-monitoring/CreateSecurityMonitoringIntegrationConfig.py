"""
Create an entity context sync configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_integration_config_create_attributes import (
    SecurityMonitoringIntegrationConfigCreateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_create_data import (
    SecurityMonitoringIntegrationConfigCreateData,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_create_request import (
    SecurityMonitoringIntegrationConfigCreateRequest,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_resource_type import (
    SecurityMonitoringIntegrationConfigResourceType,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_secrets import (
    SecurityMonitoringIntegrationConfigSecrets,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_settings import (
    SecurityMonitoringIntegrationConfigSettings,
)
from datadog_api_client.v2.model.security_monitoring_integration_type import SecurityMonitoringIntegrationType

body = SecurityMonitoringIntegrationConfigCreateRequest(
    data=SecurityMonitoringIntegrationConfigCreateData(
        attributes=SecurityMonitoringIntegrationConfigCreateAttributes(
            domain="siem-test.com",
            integration_type=SecurityMonitoringIntegrationType.GOOGLE_WORKSPACE,
            name="My GWS Integration",
            secrets=SecurityMonitoringIntegrationConfigSecrets([("admin_email", "test@example.com")]),
            settings=SecurityMonitoringIntegrationConfigSettings([("setting1", "value1")]),
        ),
        type=SecurityMonitoringIntegrationConfigResourceType.INTEGRATION_CONFIG,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_security_monitoring_integration_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_integration_config(body=body)

    print(response)
