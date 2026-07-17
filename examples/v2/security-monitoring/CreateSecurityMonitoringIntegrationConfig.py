"""
Create an entity context sync configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_google_workspace_integration_config_create_attributes import (
    SecurityMonitoringGoogleWorkspaceIntegrationConfigCreateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_create_data import (
    SecurityMonitoringIntegrationConfigCreateData,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_create_request import (
    SecurityMonitoringIntegrationConfigCreateRequest,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_google_workspace_secrets import (
    SecurityMonitoringIntegrationConfigGoogleWorkspaceSecrets,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_google_workspace_service_account import (
    SecurityMonitoringIntegrationConfigGoogleWorkspaceServiceAccount,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_resource_type import (
    SecurityMonitoringIntegrationConfigResourceType,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_settings import (
    SecurityMonitoringIntegrationConfigSettings,
)
from datadog_api_client.v2.model.security_monitoring_integration_type_google_workspace import (
    SecurityMonitoringIntegrationTypeGoogleWorkspace,
)

body = SecurityMonitoringIntegrationConfigCreateRequest(
    data=SecurityMonitoringIntegrationConfigCreateData(
        attributes=SecurityMonitoringGoogleWorkspaceIntegrationConfigCreateAttributes(
            domain="siem-test.com",
            integration_type=SecurityMonitoringIntegrationTypeGoogleWorkspace.GOOGLE_WORKSPACE,
            name="My GWS Integration",
            secrets=SecurityMonitoringIntegrationConfigGoogleWorkspaceSecrets(
                admin_email="admin@example.com",
                service_account_json=SecurityMonitoringIntegrationConfigGoogleWorkspaceServiceAccount(
                    client_email="svc@my-project.iam.gserviceaccount.com",
                    private_key="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----",
                    project_id="my-project",
                    type="service_account",
                ),
            ),
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
