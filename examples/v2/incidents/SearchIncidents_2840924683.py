"""
Search for incidents accepts responders include
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_related_object import IncidentRelatedObject

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["search_incidents"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.search_incidents(
        include=IncidentRelatedObject.RESPONDERS,
        query="state:(active OR stable OR resolved)",
        page_size=1,
    )

    print(response)
