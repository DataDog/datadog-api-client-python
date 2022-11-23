"""
Update an index returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi
from datadog_api_client.v1.model.logs_exclusion import LogsExclusion
from datadog_api_client.v1.model.logs_exclusion_filter import LogsExclusionFilter
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_index_update_request import LogsIndexUpdateRequest

body = LogsIndexUpdateRequest(
    daily_limit=300000000,
    disable_daily_limit=False,
    exclusion_filters=[
        LogsExclusion(
            filter=LogsExclusionFilter(
                query="*",
                sample_rate=1.0,
            ),
            name="payment",
        ),
    ],
    filter=LogsFilter(
        query="source:python",
    ),
    num_retention_days=15,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    response = api_instance.update_logs_index(name="name", body=body)

    print(response)
