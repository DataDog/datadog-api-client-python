"""
Get estimated cost across multi-org account with date returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_estimated_cost_by_org(
        start_date=(datetime.now() + relativedelta(days=-5)),
        end_date=(datetime.now() + relativedelta(days=-3)),
    )

    print(response)
