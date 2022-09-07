"""
Get usage attribution returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datadog_api_client.v1.model.usage_attribution_supported_metrics import UsageAttributionSupportedMetrics

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_attribution(
        start_month=(datetime.now() + relativedelta(days=-3)),
        fields=UsageAttributionSupportedMetrics.ALL,
        offset=0,
        limit=1,
    )

    print(response)
