"""
Get Monthly Usage Attribution returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datadog_api_client.v1.model.monthly_usage_attribution_supported_metrics import (
    MonthlyUsageAttributionSupportedMetrics,
)

configuration = Configuration()
configuration.unstable_operations["get_monthly_usage_attribution"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_monthly_usage_attribution(
        start_month=(datetime.now() + relativedelta(days=-3)).isoformat(timespec="seconds"),
        fields=MonthlyUsageAttributionSupportedMetrics("infra_host_usage"),
    )

    print(response)
