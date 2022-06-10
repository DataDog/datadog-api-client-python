"""
Get a quick list of logs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datetime import datetime
from dateutil.tz import tzoffset

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.list_logs_get(
        filter_query="datadog-agent",
        filter_index="main",
        filter_from=datetime(2020, 9, 17, 11, 48, 36, tzinfo=tzoffset(None, 3600)),
        filter_to=datetime(2020, 9, 17, 12, 48, 36, tzinfo=tzoffset(None, 3600)),
        page_limit=5,
    )

    print(response)
