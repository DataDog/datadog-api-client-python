"""
GetEstimatedCostByOrg with start_month returns "OK" response
"""

from datetime import datetime
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_estimated_cost_by_org(
        view="sub-org",
        start_month=datetime.now(),
    )

    print(response)
