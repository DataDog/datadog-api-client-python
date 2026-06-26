"""
Mitigate governance detections returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.governance_controls_api import GovernanceControlsApi
from datadog_api_client.v2.model.governance_control_detection_resource_type import (
    GovernanceControlDetectionResourceType,
)
from datadog_api_client.v2.model.governance_mitigation_request import GovernanceMitigationRequest
from datadog_api_client.v2.model.governance_mitigation_request_attributes import GovernanceMitigationRequestAttributes
from datadog_api_client.v2.model.governance_mitigation_request_data import GovernanceMitigationRequestData

body = GovernanceMitigationRequest(
    data=GovernanceMitigationRequestData(
        attributes=GovernanceMitigationRequestAttributes(
            detection_ids=[
                "3f9b2c1a-8d4e-4a6b-9c2f-1e7d5a0b3c4d",
            ],
            detection_type="unused_api_keys",
            mitigation_type="revoke_api_key",
        ),
        type=GovernanceControlDetectionResourceType.GOVERNANCE_CONTROL_DETECTION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_governance_mitigation"] = True
with ApiClient(configuration) as api_client:
    api_instance = GovernanceControlsApi(api_client)
    api_instance.create_governance_mitigation(body=body)
