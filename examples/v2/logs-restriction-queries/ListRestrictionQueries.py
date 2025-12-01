"""
List restriction queries returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi

configuration = Configuration()
configuration.unstable_operations["list_restriction_queries"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.list_restriction_queries()

    print(response)
