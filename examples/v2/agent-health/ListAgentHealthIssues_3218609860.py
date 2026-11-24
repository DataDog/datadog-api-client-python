"""
List Agent Health issues returns "OK" response with pagination
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agent_health_api import AgentHealthApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = AgentHealthApi(api_client)
    items = api_instance.list_agent_health_issues_with_pagination()
    for item in items:
        print(item)
