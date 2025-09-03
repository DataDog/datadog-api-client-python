"""
Get a job's hist signals returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

configuration = Configuration()
configuration.unstable_operations["get_security_monitoring_histsignals_by_job_id"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_security_monitoring_histsignals_by_job_id(
        job_id="job_id",
    )

    print(response)
