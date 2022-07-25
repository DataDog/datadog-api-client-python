"""
Get hourly usage for Lambda Traced Invocations returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_lambda_traced_invocations(
        start_hr=(datetime.now() + relativedelta(days=-5)),
        end_hr=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)
