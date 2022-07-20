"""
Query timeseries points returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.query_metrics(
        _from=int((datetime.now() + relativedelta(days=-1)).timestamp()),
        to=int(datetime.now().timestamp()),
        query="system.cpu.idle{*}",
    )

    print(response)
