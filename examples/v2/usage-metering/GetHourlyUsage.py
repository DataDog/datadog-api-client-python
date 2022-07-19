"""
Get hourly usage by product family returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_hourly_usage(
        filter_timestamp_start=(datetime.now() + relativedelta(days=-3)),
        filter_product_families="infra_hosts",
    )

    print(response)
