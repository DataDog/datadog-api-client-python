"""
Update a secure embed for a dashboard returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_secure_embed_api import DashboardSecureEmbedApi
from datadog_api_client.v2.model.secure_embed_global_time import SecureEmbedGlobalTime
from datadog_api_client.v2.model.secure_embed_global_time_live_span import SecureEmbedGlobalTimeLiveSpan
from datadog_api_client.v2.model.secure_embed_selectable_template_variable import SecureEmbedSelectableTemplateVariable
from datadog_api_client.v2.model.secure_embed_status import SecureEmbedStatus
from datadog_api_client.v2.model.secure_embed_update_request import SecureEmbedUpdateRequest
from datadog_api_client.v2.model.secure_embed_update_request_attributes import SecureEmbedUpdateRequestAttributes
from datadog_api_client.v2.model.secure_embed_update_request_data import SecureEmbedUpdateRequestData
from datadog_api_client.v2.model.secure_embed_update_request_type import SecureEmbedUpdateRequestType
from datadog_api_client.v2.model.secure_embed_viewing_preferences import SecureEmbedViewingPreferences
from datadog_api_client.v2.model.secure_embed_viewing_preferences_theme import SecureEmbedViewingPreferencesTheme

body = SecureEmbedUpdateRequest(
    data=SecureEmbedUpdateRequestData(
        attributes=SecureEmbedUpdateRequestAttributes(
            global_time=SecureEmbedGlobalTime(
                live_span=SecureEmbedGlobalTimeLiveSpan.PAST_ONE_HOUR,
            ),
            global_time_selectable=True,
            selectable_template_vars=[
                SecureEmbedSelectableTemplateVariable(
                    default_values=[
                        "1",
                    ],
                    name="org_id",
                    prefix="org_id",
                    visible_tags=[
                        "1",
                    ],
                ),
            ],
            status=SecureEmbedStatus.ACTIVE,
            title="Q1 Metrics Dashboard (Updated)",
            viewing_preferences=SecureEmbedViewingPreferences(
                high_density=False,
                theme=SecureEmbedViewingPreferencesTheme.SYSTEM,
            ),
        ),
        type=SecureEmbedUpdateRequestType.SECURE_EMBED_UPDATE_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_dashboard_secure_embed"] = True
with ApiClient(configuration) as api_client:
    api_instance = DashboardSecureEmbedApi(api_client)
    response = api_instance.update_dashboard_secure_embed(dashboard_id="dashboard_id", token="token", body=body)

    print(response)
