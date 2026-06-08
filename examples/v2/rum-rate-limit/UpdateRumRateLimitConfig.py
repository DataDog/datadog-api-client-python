"""
Create or update a RUM rate limit configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_rate_limit_api import RumRateLimitApi
from datadog_api_client.v2.model.rum_rate_limit_adaptive_config import RumRateLimitAdaptiveConfig
from datadog_api_client.v2.model.rum_rate_limit_config_type import RumRateLimitConfigType
from datadog_api_client.v2.model.rum_rate_limit_config_update_attributes import RumRateLimitConfigUpdateAttributes
from datadog_api_client.v2.model.rum_rate_limit_config_update_data import RumRateLimitConfigUpdateData
from datadog_api_client.v2.model.rum_rate_limit_config_update_request import RumRateLimitConfigUpdateRequest
from datadog_api_client.v2.model.rum_rate_limit_custom_config import RumRateLimitCustomConfig
from datadog_api_client.v2.model.rum_rate_limit_mode import RumRateLimitMode
from datadog_api_client.v2.model.rum_rate_limit_quota_reached_action import RumRateLimitQuotaReachedAction
from datadog_api_client.v2.model.rum_rate_limit_scope_type import RumRateLimitScopeType
from datadog_api_client.v2.model.rum_rate_limit_window_type import RumRateLimitWindowType

body = RumRateLimitConfigUpdateRequest(
    data=RumRateLimitConfigUpdateData(
        attributes=RumRateLimitConfigUpdateAttributes(
            adaptive=RumRateLimitAdaptiveConfig(
                max_retention_rate=0.5,
            ),
            custom=RumRateLimitCustomConfig(
                daily_reset_time="08:00",
                daily_reset_timezone="+09:00",
                quota_reached_action=RumRateLimitQuotaReachedAction.STOP,
                session_limit=1000000,
                window_type=RumRateLimitWindowType.DAILY,
            ),
            mode=RumRateLimitMode.CUSTOM,
        ),
        id="cd73a516-a481-4af5-8352-9b577465c77b",
        type=RumRateLimitConfigType.RUM_RATE_LIMIT_CONFIG,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_rum_rate_limit_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumRateLimitApi(api_client)
    response = api_instance.update_rum_rate_limit_config(
        scope_type=RumRateLimitScopeType.APPLICATION, scope_id="cd73a516-a481-4af5-8352-9b577465c77b", body=body
    )

    print(response)
