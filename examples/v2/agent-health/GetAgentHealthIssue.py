"""
Get an Agent Health issue returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agent_health_api import AgentHealthApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_agent_health_issue"] = True
with ApiClient(configuration) as api_client:
    api_instance = AgentHealthApi(api_client)
    response = api_instance.get_agent_health_issue(
        issue_id="issue_id",
    )

    print(response)
