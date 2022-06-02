"""
Update pipeline order returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_pipelines_order import LogsPipelinesOrder

body = LogsPipelinesOrder(
    pipeline_ids=[
        "tags",
        "org_ids",
        "products",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.update_logs_pipeline_order(body=body)

    print(response)
