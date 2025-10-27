"""
Delete an existing job returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

configuration = Configuration()
configuration.unstable_operations["delete_threat_hunting_job"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.delete_threat_hunting_job(
        job_id="job_id",
    )
