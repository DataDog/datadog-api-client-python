"""
Create a Salesforce incident template returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.salesforce_integration_api import SalesforceIntegrationApi
from datadog_api_client.v2.model.salesforce_incidents_template_create_attributes import (
    SalesforceIncidentsTemplateCreateAttributes,
)
from datadog_api_client.v2.model.salesforce_incidents_template_create_data import SalesforceIncidentsTemplateCreateData
from datadog_api_client.v2.model.salesforce_incidents_template_create_request import (
    SalesforceIncidentsTemplateCreateRequest,
)
from datadog_api_client.v2.model.salesforce_incidents_template_priority import SalesforceIncidentsTemplatePriority
from datadog_api_client.v2.model.salesforce_incidents_template_type import SalesforceIncidentsTemplateType
from uuid import UUID

body = SalesforceIncidentsTemplateCreateRequest(
    data=SalesforceIncidentsTemplateCreateData(
        attributes=SalesforceIncidentsTemplateCreateAttributes(
            description="An incident was detected by Datadog monitors.",
            name="production-outage",
            owner_id="005000000000000",
            priority=SalesforceIncidentsTemplatePriority.HIGH,
            salesforce_org_id=UUID("596da4af-0563-4097-90ff-07230c3f9db3"),
            subject="Datadog Incident: Production Outage",
        ),
        type=SalesforceIncidentsTemplateType.SALESFORCE_INCIDENTS_INCIDENT_TEMPLATE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SalesforceIntegrationApi(api_client)
    response = api_instance.create_incident_template(body=body)

    print(response)
