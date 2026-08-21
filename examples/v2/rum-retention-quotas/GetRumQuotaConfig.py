"""
Get a RUM retention quota configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_quotas_api import RUMRetentionQuotasApi
from datadog_api_client.v2.model.rum_retention_quota_scope_type import RumRetentionQuotaScopeType

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMRetentionQuotasApi(api_client)
    response = api_instance.get_rum_quota_config(
        scope_type=RumRetentionQuotaScopeType.APPLICATION,
        scope_id="cd73a516-a481-4af5-8352-9b577465c77b",
    )

    print(response)
