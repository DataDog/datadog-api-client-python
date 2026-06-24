"""
Update a governance control returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.governance_controls_api import GovernanceControlsApi
from datadog_api_client.v2.model.governance_control_resource_type import GovernanceControlResourceType
from datadog_api_client.v2.model.governance_control_update_attributes import GovernanceControlUpdateAttributes
from datadog_api_client.v2.model.governance_control_update_data import GovernanceControlUpdateData
from datadog_api_client.v2.model.governance_control_update_request import GovernanceControlUpdateRequest

body = GovernanceControlUpdateRequest(
    data=GovernanceControlUpdateData(
        attributes=GovernanceControlUpdateAttributes(
            detection_frequency="daily",
            mitigation_type="revoke_api_key",
            name="Unused API Keys",
            notification_frequency="daily",
            notification_type="slack",
        ),
        id="0d4e6f8a-1b2c-3d4e-5f6a-7b8c9d0e1f2a",
        type=GovernanceControlResourceType.GOVERNANCE_CONTROL,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_governance_control"] = True
with ApiClient(configuration) as api_client:
    api_instance = GovernanceControlsApi(api_client)
    response = api_instance.update_governance_control(detection_type="detection_type", body=body)

    print(response)
