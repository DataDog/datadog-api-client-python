"""
Get hourly usage for synthetics checks returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_synthetics(
        start_hr=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
    )

    print(response)
