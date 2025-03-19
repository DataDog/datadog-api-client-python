"""
Get AWS On Demand task by id returns "OK." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.get_aws_on_demand_task(
        task_id="63d6b4f5-e5d0-4d90-824a-9580f05f026a",
    )

    print(response)
