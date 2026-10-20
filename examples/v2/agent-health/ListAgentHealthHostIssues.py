"""
List active Agent Health issues returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agent_health_api import AgentHealthApi
from datadog_api_client.v2.model.agent_health_agent_type import AgentHealthAgentType

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentHealthApi(api_client)
    response = api_instance.list_agent_health_host_issues(
        resource_id="123e4567-e89b-12d3-a456-426614174000",
        agent_type=AgentHealthAgentType.NODE,
    )

    print(response)
