"""
Get a restriction query returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi

configuration = Configuration()
configuration.unstable_operations["get_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.get_restriction_query(
        restriction_query_id="restriction_query_id",
    )

    print(response)
