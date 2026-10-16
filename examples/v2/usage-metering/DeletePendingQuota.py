"""
Cancel a scheduled usage quota limit returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_pending_quota"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    api_instance.delete_pending_quota(
        quota_namespace="ai_credits",
        id="MTIzNB9haV9jcmVkaXRzH3VzZXJfaGFuZGxlOl9fQUxMX18",
    )
