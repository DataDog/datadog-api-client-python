"""
Take graph snapshots returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.snapshots_api import SnapshotsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SnapshotsApi(api_client)
    response = api_instance.get_graph_snapshot(
        metric_query="avg:system.load.1{*}",
        start=int((datetime.now() + relativedelta(days=-1)).timestamp()),
        end=int(datetime.now().timestamp()),
        title="System load",
        height=400,
        width=600,
    )

    print(response)
