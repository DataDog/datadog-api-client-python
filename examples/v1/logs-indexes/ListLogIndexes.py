"""
Get all indexes returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    response = api_instance.list_log_indexes()

    print(response)
