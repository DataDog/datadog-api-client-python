"""
Create incident rule returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_rule_attributes_request import IncidentRuleAttributesRequest
from datadog_api_client.v2.model.incident_rule_data_request import IncidentRuleDataRequest
from datadog_api_client.v2.model.incident_rule_request import IncidentRuleRequest
from datadog_api_client.v2.model.incident_rule_type import IncidentRuleType

body = IncidentRuleRequest(
    data=IncidentRuleDataRequest(
        attributes=IncidentRuleAttributesRequest(
            name="High Severity Rule",
        ),
        type=IncidentRuleType.INCIDENT_RULE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_config_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_config_rule(body=body)

    print(response)
