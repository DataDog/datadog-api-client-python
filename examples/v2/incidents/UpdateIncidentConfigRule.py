"""
Update incident rule returns "OK" response
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
configuration.unstable_operations["update_incident_config_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_config_rule(rule_id="612e0c88-9137-4bd2-8de4-9356867d4c6a", body=body)

    print(response)
