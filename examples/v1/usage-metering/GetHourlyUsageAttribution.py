"""
Get Hourly Usage Attribution returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datadog_api_client.v1.model.hourly_usage_attribution_usage_type import HourlyUsageAttributionUsageType

configuration = Configuration()
configuration.unstable_operations["get_hourly_usage_attribution"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_hourly_usage_attribution(
        start_hr=(datetime.now() + relativedelta(days=-3)).isoformat(timespec="seconds"),
        usage_type=HourlyUsageAttributionUsageType("infra_host_usage"),
    )

    print(response)
