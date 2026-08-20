"""
Create or update a RUM retention quota config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_quota_api import RUMRetentionQuotaApi
from datadog_api_client.v2.model.rum_retention_quota_adaptive_config import RumRetentionQuotaAdaptiveConfig
from datadog_api_client.v2.model.rum_retention_quota_config_type import RumRetentionQuotaConfigType
from datadog_api_client.v2.model.rum_retention_quota_config_update_attributes import (
    RumRetentionQuotaConfigUpdateAttributes,
)
from datadog_api_client.v2.model.rum_retention_quota_config_update_data import RumRetentionQuotaConfigUpdateData
from datadog_api_client.v2.model.rum_retention_quota_config_update_request import RumRetentionQuotaConfigUpdateRequest
from datadog_api_client.v2.model.rum_retention_quota_custom_config import RumRetentionQuotaCustomConfig
from datadog_api_client.v2.model.rum_retention_quota_mode import RumRetentionQuotaMode
from datadog_api_client.v2.model.rum_retention_quota_reached_action import RumRetentionQuotaReachedAction
from datadog_api_client.v2.model.rum_retention_quota_scope_type import RumRetentionQuotaScopeType
from datadog_api_client.v2.model.rum_retention_quota_window_type import RumRetentionQuotaWindowType

body = RumRetentionQuotaConfigUpdateRequest(
    data=RumRetentionQuotaConfigUpdateData(
        attributes=RumRetentionQuotaConfigUpdateAttributes(
            adaptive=RumRetentionQuotaAdaptiveConfig(
                max_retention_rate=0.5,
            ),
            custom=RumRetentionQuotaCustomConfig(
                daily_reset_time="08:00",
                daily_reset_timezone="+09:00",
                quota_reached_action=RumRetentionQuotaReachedAction.STOP,
                session_limit=1000000,
                window_type=RumRetentionQuotaWindowType.DAILY,
            ),
            mode=RumRetentionQuotaMode.CUSTOM,
        ),
        id="ced16651-97b6-4e67-8590-8caec3af0695",
        type=RumRetentionQuotaConfigType.RUM_QUOTA_CONFIG,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMRetentionQuotaApi(api_client)
    response = api_instance.upsert_rum_quota_config(
        scope_type=RumRetentionQuotaScopeType.APPLICATION, scope_id="ced16651-97b6-4e67-8590-8caec3af0695", body=body
    )

    print(response)
