"""
Get hourly usage for Logs by Index returns "OK" response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_logs_by_index(
        start_hr=datetime.datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc())
    )

    print(response)
