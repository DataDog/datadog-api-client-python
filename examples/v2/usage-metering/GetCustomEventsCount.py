"""
Get hourly usage for Custom Events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_custom_events_count(
        start_hr=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)
