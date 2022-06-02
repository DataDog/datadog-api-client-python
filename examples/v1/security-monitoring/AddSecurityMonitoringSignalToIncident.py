"""
Add a security signal to an incident returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v1.model.add_signal_to_incident_request import AddSignalToIncidentRequest

body = AddSignalToIncidentRequest(
    incident_id=2609,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.add_security_monitoring_signal_to_incident(
        signal_id="AQAAAYDiB_Ol8PbzFAAAAABBWURpQl9PbEFBQU0yeXhGTG9ZV2JnQUE", body=body
    )

    print(response)
