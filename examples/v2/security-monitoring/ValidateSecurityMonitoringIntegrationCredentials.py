"""
Validate entity context sync credentials returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_google_workspace_integration_credentials_validate_attributes import (
    SecurityMonitoringGoogleWorkspaceIntegrationCredentialsValidateAttributes,
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
from datadog_api_client.v2.model.security_monitoring_integration_credentials_validate_data import (
    SecurityMonitoringIntegrationCredentialsValidateData,
)
from datadog_api_client.v2.model.security_monitoring_integration_credentials_validate_request import (
    SecurityMonitoringIntegrationCredentialsValidateRequest,
)
from datadog_api_client.v2.model.security_monitoring_integration_type_google_workspace import (
    SecurityMonitoringIntegrationTypeGoogleWorkspace,
)

body = SecurityMonitoringIntegrationCredentialsValidateRequest(
    data=SecurityMonitoringIntegrationCredentialsValidateData(
        attributes=SecurityMonitoringGoogleWorkspaceIntegrationCredentialsValidateAttributes(
            domain="siem-test.com",
            integration_type=SecurityMonitoringIntegrationTypeGoogleWorkspace.GOOGLE_WORKSPACE,
            secrets=SecurityMonitoringIntegrationConfigGoogleWorkspaceSecrets(
                admin_email="admin@example.com",
                service_account_json=SecurityMonitoringIntegrationConfigGoogleWorkspaceServiceAccount(
                    client_email="svc@my-project.iam.gserviceaccount.com",
                    private_key="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----",
                    project_id="my-project",
                    type="service_account",
                ),
            ),
        ),
        type=SecurityMonitoringIntegrationConfigResourceType.INTEGRATION_CONFIG,
    ),
)

configuration = Configuration()
configuration.unstable_operations["validate_security_monitoring_integration_credentials"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.validate_security_monitoring_integration_credentials(body=body)
