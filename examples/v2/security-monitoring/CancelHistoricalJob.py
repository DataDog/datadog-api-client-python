"""
Cancel a historical job returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "historical_job" in the system
HISTORICAL_JOB_DATA_ID = environ["HISTORICAL_JOB_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["cancel_historical_job"] = True
configuration.unstable_operations["run_historical_job"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.cancel_historical_job(
        job_id=HISTORICAL_JOB_DATA_ID,
    )
