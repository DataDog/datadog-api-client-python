"""
Get all SLO corrections returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objective_corrections_api import ServiceLevelObjectiveCorrectionsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectiveCorrectionsApi(api_client)
    items = api_instance.list_slo_correction_with_pagination(
        limit=2,
    )
    for item in items:
        print(item)
