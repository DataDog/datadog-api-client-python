"""
Get hourly usage for RUM sessions returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_rum_sessions(
        start_hr=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)
