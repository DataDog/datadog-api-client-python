"""
Create or update usage quotas returns "OK. The response includes each item's result; see each item's `error` attribute
for any that failed to write." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi
from datadog_api_client.v2.model.usage_quota_create_attributes import UsageQuotaCreateAttributes
from datadog_api_client.v2.model.usage_quota_create_data import UsageQuotaCreateData
from datadog_api_client.v2.model.usage_quota_request_scope import UsageQuotaRequestScope
from datadog_api_client.v2.model.usage_quota_type import UsageQuotaType
from datadog_api_client.v2.model.usage_quotas_create_request import UsageQuotasCreateRequest

body = UsageQuotasCreateRequest(
    data=[
        UsageQuotaCreateData(
            attributes=UsageQuotaCreateAttributes(
                enforced=True,
                scope=UsageQuotaRequestScope(
                    user_handle="jane@example.com",
                ),
                usage_limit=100000,
            ),
            type=UsageQuotaType.QUOTAS,
        ),
    ],
)

configuration = Configuration()
configuration.unstable_operations["create_quotas"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.create_quotas(quota_namespace="ai_credits", body=body)

    print(response)
