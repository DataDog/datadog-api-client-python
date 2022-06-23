"""
Search for SLOs returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi

# there is a valid "slo" in the system
SLO_DATA_0_NAME = environ["SLO_DATA_0_NAME"]

configuration = Configuration()
configuration.unstable_operations["search_slo"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.search_slo(
        query=SLO_DATA_0_NAME,
        page_size=20,
        page_number=0,
    )

    print(response)
