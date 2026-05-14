"""
Get PagerDuty related incidents returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

configuration = Configuration()
configuration.unstable_operations["get_incident_pagerduty_related_incidents"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.get_incident_pagerduty_related_incidents(
        pagerduty_incident_id="pagerduty_incident_id",
    )

    print(response)
