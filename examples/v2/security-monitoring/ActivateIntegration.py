"""
Activate an entity context sync integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_integration_activate_attributes import (
    SecurityMonitoringIntegrationActivateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_integration_activate_data import (
    SecurityMonitoringIntegrationActivateData,
)
from datadog_api_client.v2.model.security_monitoring_integration_activate_request import (
    SecurityMonitoringIntegrationActivateRequest,
)
from datadog_api_client.v2.model.security_monitoring_integration_activate_resource_type import (
    SecurityMonitoringIntegrationActivateResourceType,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_settings import (
    SecurityMonitoringIntegrationConfigSettings,
)

body = SecurityMonitoringIntegrationActivateRequest(
    data=SecurityMonitoringIntegrationActivateData(
        attributes=SecurityMonitoringIntegrationActivateAttributes(
            domain="default",
            name="My Entra ID Integration",
            settings=SecurityMonitoringIntegrationConfigSettings([("setting1", "value1")]),
        ),
        type=SecurityMonitoringIntegrationActivateResourceType.ACTIVATE_ENTRA_ID_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["activate_integration"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.activate_integration(integration_type="entra_id", body=body)

    print(response)
