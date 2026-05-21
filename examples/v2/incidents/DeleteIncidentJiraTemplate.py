"""
Delete an incident Jira template returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["delete_incident_jira_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    api_instance.delete_incident_jira_template(
        template_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )
