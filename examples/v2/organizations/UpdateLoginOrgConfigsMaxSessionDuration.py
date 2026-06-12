"""
Update the maximum session duration returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.organizations_api import OrganizationsApi
from datadog_api_client.v2.model.max_session_duration_type import MaxSessionDurationType
from datadog_api_client.v2.model.max_session_duration_update_attributes import MaxSessionDurationUpdateAttributes
from datadog_api_client.v2.model.max_session_duration_update_data import MaxSessionDurationUpdateData
from datadog_api_client.v2.model.max_session_duration_update_request import MaxSessionDurationUpdateRequest

body = MaxSessionDurationUpdateRequest(
    data=MaxSessionDurationUpdateData(
        attributes=MaxSessionDurationUpdateAttributes(
            max_session_duration=604800,
        ),
        type=MaxSessionDurationType.MAX_SESSION_DURATION,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    api_instance.update_login_org_configs_max_session_duration(body=body)
