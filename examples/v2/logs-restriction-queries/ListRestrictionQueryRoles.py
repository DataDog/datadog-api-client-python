"""
List roles for a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["list_restriction_query_roles"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.list_restriction_query_roles(
        restriction_query_id=RESTRICTION_QUERY_DATA_ID,
    )

    print(response)
