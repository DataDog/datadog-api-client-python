"""
Get historical cost across your account returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_historical_cost_by_org(
        view="sub-org",
        start_month=(datetime.now() + relativedelta(months=-2)),
    )

    print(response)
