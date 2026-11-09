"""
Get a usage quota returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

# there is a valid "quota" in the system
QUOTA_DATA_0_ID = environ["QUOTA_DATA_0_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_quotas"] = True
configuration.unstable_operations["delete_quota"] = True
configuration.unstable_operations["get_quota"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_quota(
        include_descendants=False,
        quota_namespace="ai_credits",
        id=QUOTA_DATA_0_ID,
    )

    print(response)
