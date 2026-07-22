"""
Update a governance control detection returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.governance_controls_api import GovernanceControlsApi
from datadog_api_client.v2.model.governance_control_detection_resource_type import (
    GovernanceControlDetectionResourceType,
)
from datadog_api_client.v2.model.governance_control_detection_update_attributes import (
    GovernanceControlDetectionUpdateAttributes,
)
from datadog_api_client.v2.model.governance_control_detection_update_data import GovernanceControlDetectionUpdateData
from datadog_api_client.v2.model.governance_control_detection_update_request import (
    GovernanceControlDetectionUpdateRequest,
)
from datadog_api_client.v2.model.governance_control_detection_update_state import GovernanceControlDetectionUpdateState
from datetime import datetime
from dateutil.tz import tzutc

body = GovernanceControlDetectionUpdateRequest(
    data=GovernanceControlDetectionUpdateData(
        attributes=GovernanceControlDetectionUpdateAttributes(
            assigned_team="platform-security",
            assigned_to="11111111-2222-3333-4444-555555555555",
            mitigate_after=datetime(2024, 3, 15, 0, 0, tzinfo=tzutc()),
            state=GovernanceControlDetectionUpdateState.EXCEPTION,
        ),
        type=GovernanceControlDetectionResourceType.GOVERNANCE_CONTROL_DETECTION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_governance_control_detection"] = True
with ApiClient(configuration) as api_client:
    api_instance = GovernanceControlsApi(api_client)
    response = api_instance.update_governance_control_detection(
        detection_type="detection_type", detection_id="detection_id", body=body
    )

    print(response)
