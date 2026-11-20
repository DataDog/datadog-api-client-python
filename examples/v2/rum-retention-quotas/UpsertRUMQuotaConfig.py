"""
Create or update a RUM retention quota config returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_quotas_api import RUMRetentionQuotasApi
from datadog_api_client.v2.model.rum_retention_quota_config_type import RUMRetentionQuotaConfigType
from datadog_api_client.v2.model.rum_retention_quota_config_update_attributes import (
    RUMRetentionQuotaConfigUpdateAttributes,
)
from datadog_api_client.v2.model.rum_retention_quota_config_update_data import RUMRetentionQuotaConfigUpdateData
from datadog_api_client.v2.model.rum_retention_quota_config_update_request import RUMRetentionQuotaConfigUpdateRequest
from datadog_api_client.v2.model.rum_retention_quota_custom_config import RUMRetentionQuotaCustomConfig
from datadog_api_client.v2.model.rum_retention_quota_mode import RUMRetentionQuotaMode
from datadog_api_client.v2.model.rum_retention_quota_reached_action import RUMRetentionQuotaReachedAction
from datadog_api_client.v2.model.rum_retention_quota_scope_type import RUMRetentionQuotaScopeType
from datadog_api_client.v2.model.rum_retention_quota_window_type import RUMRetentionQuotaWindowType

body = RUMRetentionQuotaConfigUpdateRequest(
    data=RUMRetentionQuotaConfigUpdateData(
        attributes=RUMRetentionQuotaConfigUpdateAttributes(
            custom=RUMRetentionQuotaCustomConfig(
                daily_reset_time="08:00",
                daily_reset_timezone="+09:00",
                quota_reached_action=RUMRetentionQuotaReachedAction.STOP,
                session_limit=1000000,
                window_type=RUMRetentionQuotaWindowType.DAILY,
            ),
            mode=RUMRetentionQuotaMode.CUSTOM,
        ),
        id="cd73a516-a481-4af5-8352-9b577465c77b",
        type=RUMRetentionQuotaConfigType.RUM_QUOTA_CONFIG,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RUMRetentionQuotasApi(api_client)
    response = api_instance.upsert_rum_quota_config(
        scope_type=RUMRetentionQuotaScopeType.APPLICATION, scope_id="cd73a516-a481-4af5-8352-9b577465c77b", body=body
    )

    print(response)
