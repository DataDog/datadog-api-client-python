"""
Update maximum session duration returns "No Content - The maximum session duration was successfully updated." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.organizations_api import OrganizationsApi
from datadog_api_client.v2.model.max_session_duration_update_attributes import MaxSessionDurationUpdateAttributes
from datadog_api_client.v2.model.max_session_duration_update_request import MaxSessionDurationUpdateRequest
from datadog_api_client.v2.model.max_session_duration_update_request_data import MaxSessionDurationUpdateRequestData
from datadog_api_client.v2.model.max_session_duration_update_request_data_type import (
    MaxSessionDurationUpdateRequestDataType,
)

body = MaxSessionDurationUpdateRequest(
    data=MaxSessionDurationUpdateRequestData(
        attributes=MaxSessionDurationUpdateAttributes(
            max_session_duration=60,
        ),
        type=MaxSessionDurationUpdateRequestDataType.MAX_SESSION_DURATION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_login_org_config_max_session_duration"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    api_instance.update_login_org_config_max_session_duration(body=body)
