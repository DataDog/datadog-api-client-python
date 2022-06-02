"""
Get hourly logs usage by retention returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_logs_by_retention(
        start_hr=(datetime.now() + relativedelta(days=-5)).isoformat(timespec="seconds"),
        end_hr=(datetime.now() + relativedelta(days=-3)).isoformat(timespec="seconds"),
    )

    print(response)
