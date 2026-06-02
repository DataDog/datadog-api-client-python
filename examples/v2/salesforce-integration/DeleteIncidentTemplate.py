"""
Delete a Salesforce incident template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.salesforce_integration_api import SalesforceIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SalesforceIntegrationApi(api_client)
    api_instance.delete_incident_template(
        incident_template_id="incident_template_id",
    )
