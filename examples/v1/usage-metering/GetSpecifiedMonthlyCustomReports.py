"""
Get specified monthly custom reports returns "OK" response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
configuration.unstable_operations["get_specified_monthly_custom_reports"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_specified_monthly_custom_reports(report_id="report_id")

    print(response)
