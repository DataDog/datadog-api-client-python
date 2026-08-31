"""
List usage quotas returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
configuration.unstable_operations["list_quotas"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    items = api_instance.list_quotas_with_pagination(
        quota_namespace="ai_credits",
    )
    for item in items:
        print(item)
