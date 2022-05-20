"""
Update indexes order returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi
from datadog_api_client.v1.model.logs_indexes_order import LogsIndexesOrder

body = LogsIndexesOrder(
    index_names=[
        "main",
        "payments",
        "web",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsIndexesApi(api_client)
    response = api_instance.update_logs_index_order(body=body)

    print(response)
