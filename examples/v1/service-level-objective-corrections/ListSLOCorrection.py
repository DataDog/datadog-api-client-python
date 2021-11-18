"""
Get all SLO corrections returns "OK" response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objective_corrections_api import ServiceLevelObjectiveCorrectionsApi

configuration = Configuration()
configuration.unstable_operations["list_slo_correction"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectiveCorrectionsApi(api_client)
    response = api_instance.list_slo_correction()

    print(response)
