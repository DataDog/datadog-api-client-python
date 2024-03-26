"""
Get SLO report returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_level_objectives_api import ServiceLevelObjectivesApi

configuration = Configuration()
configuration.unstable_operations["get_slo_report"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.get_slo_report(
        report_id="9fb2dc2a-ead0-11ee-a174-9fe3a9d7627f",
    )
