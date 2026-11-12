"""
List Agent Health issues returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agent_health_api import AgentHealthApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_agent_health_issues"] = True
with ApiClient(configuration) as api_client:
    api_instance = AgentHealthApi(api_client)
    response = api_instance.list_agent_health_issues()

    print(response)
