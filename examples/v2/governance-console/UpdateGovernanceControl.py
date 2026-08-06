"""
Update a control returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.governance_console_api import GovernanceConsoleApi
from datadog_api_client.v2.model.governance_control_resource_type import GovernanceControlResourceType
from datadog_api_client.v2.model.governance_control_update_attributes import GovernanceControlUpdateAttributes
from datadog_api_client.v2.model.governance_control_update_data import GovernanceControlUpdateData
from datadog_api_client.v2.model.governance_control_update_request import GovernanceControlUpdateRequest

body = GovernanceControlUpdateRequest(
    data=GovernanceControlUpdateData(
        attributes=GovernanceControlUpdateAttributes(
            detection_frequency="daily",
            mitigation_type="revoke_api_key",
        ),
        type=GovernanceControlResourceType.GOVERNANCE_CONTROL,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_governance_control"] = True
with ApiClient(configuration) as api_client:
    api_instance = GovernanceConsoleApi(api_client)
    response = api_instance.update_governance_control(detection_type="detection_type", body=body)

    print(response)
