"""
Delete an SLO correction returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objective_corrections_api import ServiceLevelObjectiveCorrectionsApi

# there is a valid "correction" for "slo"
CORRECTION_DATA_ID = environ["CORRECTION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectiveCorrectionsApi(api_client)
    api_instance.delete_slo_correction(
        slo_correction_id=CORRECTION_DATA_ID,
    )
