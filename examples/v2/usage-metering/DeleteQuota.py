"""
Delete a usage quota returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
configuration.unstable_operations["delete_quota"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    api_instance.delete_quota(
        quota_namespace="ai_credits",
        id="MjAfYWlfY3JlZGl0c1911c2VyX2hhbmRsZTpfX0FMTF9f",
    )
