"""
Get a RUM retention quota configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_quota_api import RUMRetentionQuotaApi
from datadog_api_client.v2.model.rum_retention_quota_scope_type import RumRetentionQuotaScopeType

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMRetentionQuotaApi(api_client)
    response = api_instance.get_rum_quota_config(
        scope_type=RumRetentionQuotaScopeType.APPLICATION,
        scope_id="ced16651-97b6-4e67-8590-8caec3af0695",
    )

    print(response)
