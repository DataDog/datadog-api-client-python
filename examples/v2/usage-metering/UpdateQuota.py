"""
Update a usage quota returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi
from datadog_api_client.v2.model.usage_quota_type import UsageQuotaType
from datadog_api_client.v2.model.usage_quota_update_attributes import UsageQuotaUpdateAttributes
from datadog_api_client.v2.model.usage_quota_update_data import UsageQuotaUpdateData
from datadog_api_client.v2.model.usage_quota_update_request import UsageQuotaUpdateRequest

body = UsageQuotaUpdateRequest(
    data=UsageQuotaUpdateData(
        attributes=UsageQuotaUpdateAttributes(
            enforced=False,
            pending_usage_limit=50000,
            usage_limit=120000,
        ),
        id="MTIzNB9haV9jcmVkaXRzH3VzZXJfaGFuZGxlOl9fQUxMX18",
        type=UsageQuotaType.QUOTAS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_quota"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.update_quota(
        quota_namespace="ai_credits", id="MTIzNB9haV9jcmVkaXRzH3VzZXJfaGFuZGxlOl9fQUxMX18", body=body
    )

    print(response)
