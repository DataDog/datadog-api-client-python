"""
Get Monthly Cost Attribution returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
configuration.unstable_operations["get_monthly_cost_attribution"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_monthly_cost_attribution(
        start_month=(datetime.now() + relativedelta(days=-5)),
        end_month=(datetime.now() + relativedelta(days=-3)),
        fields="infra_host_total_cost",
    )

    print(response)
