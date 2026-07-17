"""
Update an entity context sync configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_google_workspace_integration_config_update_attributes import (
    SecurityMonitoringGoogleWorkspaceIntegrationConfigUpdateAttributes,
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
from datadog_api_client.v2.model.security_monitoring_integration_config_update_data import (
    SecurityMonitoringIntegrationConfigUpdateData,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_update_request import (
    SecurityMonitoringIntegrationConfigUpdateRequest,
)
from datadog_api_client.v2.model.security_monitoring_integration_type_google_workspace import (
    SecurityMonitoringIntegrationTypeGoogleWorkspace,
)

body = SecurityMonitoringIntegrationConfigUpdateRequest(
    data=SecurityMonitoringIntegrationConfigUpdateData(
        attributes=SecurityMonitoringGoogleWorkspaceIntegrationConfigUpdateAttributes(
            domain="siem-test.com",
            enabled=True,
            integration_type=SecurityMonitoringIntegrationTypeGoogleWorkspace.GOOGLE_WORKSPACE,
            name="My GWS Integration (renamed)",
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
configuration.unstable_operations["update_security_monitoring_integration_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_security_monitoring_integration_config(
        integration_config_id="integration_config_id", body=body
    )

    print(response)
