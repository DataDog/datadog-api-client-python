"""
Create a secure embed for a dashboard returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_secure_embed_api import DashboardSecureEmbedApi
from datadog_api_client.v2.model.secure_embed_create_request import SecureEmbedCreateRequest
from datadog_api_client.v2.model.secure_embed_create_request_attributes import SecureEmbedCreateRequestAttributes
from datadog_api_client.v2.model.secure_embed_create_request_data import SecureEmbedCreateRequestData
from datadog_api_client.v2.model.secure_embed_global_time import SecureEmbedGlobalTime
from datadog_api_client.v2.model.secure_embed_global_time_live_span import SecureEmbedGlobalTimeLiveSpan
from datadog_api_client.v2.model.secure_embed_request_type import SecureEmbedRequestType
from datadog_api_client.v2.model.secure_embed_selectable_template_variable import SecureEmbedSelectableTemplateVariable
from datadog_api_client.v2.model.secure_embed_status import SecureEmbedStatus
from datadog_api_client.v2.model.secure_embed_viewing_preferences import SecureEmbedViewingPreferences
from datadog_api_client.v2.model.secure_embed_viewing_preferences_theme import SecureEmbedViewingPreferencesTheme

body = SecureEmbedCreateRequest(
    data=SecureEmbedCreateRequestData(
        attributes=SecureEmbedCreateRequestAttributes(
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
            title="Q1 Metrics Dashboard",
            viewing_preferences=SecureEmbedViewingPreferences(
                high_density=False,
                theme=SecureEmbedViewingPreferencesTheme.SYSTEM,
            ),
        ),
        type=SecureEmbedRequestType.SECURE_EMBED_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_dashboard_secure_embed"] = True
with ApiClient(configuration) as api_client:
    api_instance = DashboardSecureEmbedApi(api_client)
    response = api_instance.create_dashboard_secure_embed(dashboard_id="dashboard_id", body=body)

    print(response)
