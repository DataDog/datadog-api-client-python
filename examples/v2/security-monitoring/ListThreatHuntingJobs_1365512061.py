"""
List historical jobs returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

# there is a valid "threat_hunting_job" in the system
THREAT_HUNTING_JOB_DATA_ID = environ["THREAT_HUNTING_JOB_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["list_threat_hunting_jobs"] = True
configuration.unstable_operations["run_threat_hunting_job"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.list_threat_hunting_jobs(
        filter_query="id:string",
    )

    print(response)
