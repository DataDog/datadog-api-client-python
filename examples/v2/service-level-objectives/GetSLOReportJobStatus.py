"""
Get SLO report status returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_level_objectives_api import ServiceLevelObjectivesApi

# there is a valid "report" in the system
REPORT_DATA_ID = environ["REPORT_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_slo_report_job_status"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.get_slo_report_job_status(
        report_id=REPORT_DATA_ID,
    )

    print(response)
