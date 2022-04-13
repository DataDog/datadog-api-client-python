"""
Get an SLO correction for an SLO returns "OK" response
"""

from os import environ
from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objective_corrections_api import ServiceLevelObjectiveCorrectionsApi

# there is a valid "correction" for "slo"
CORRECTION_DATA_ID = environ["CORRECTION_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_slo_correction"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectiveCorrectionsApi(api_client)
    response = api_instance.get_slo_correction(
        slo_correction_id=CORRECTION_DATA_ID,
    )

    print(response)
