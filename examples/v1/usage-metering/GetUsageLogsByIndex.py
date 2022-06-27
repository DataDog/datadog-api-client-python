"""
Get hourly usage for Logs by Index returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_logs_by_index(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)
