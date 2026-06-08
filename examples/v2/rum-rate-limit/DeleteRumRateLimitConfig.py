"""
Delete a RUM rate limit configuration returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_rate_limit_api import RumRateLimitApi
from datadog_api_client.v2.model.rum_rate_limit_scope_type import RumRateLimitScopeType

configuration = Configuration()
configuration.unstable_operations["delete_rum_rate_limit_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumRateLimitApi(api_client)
    api_instance.delete_rum_rate_limit_config(
        scope_type=RumRateLimitScopeType.APPLICATION,
        scope_id="cd73a516-a481-4af5-8352-9b577465c77b",
    )
