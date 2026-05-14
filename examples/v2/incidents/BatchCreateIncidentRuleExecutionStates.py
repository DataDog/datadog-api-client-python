"""
Batch create incident rule execution states returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_batch_create_rule_execution_states_data import (
    IncidentBatchCreateRuleExecutionStatesData,
)
from datadog_api_client.v2.model.incident_batch_create_rule_execution_states_data_attributes import (
    IncidentBatchCreateRuleExecutionStatesDataAttributes,
)
from datadog_api_client.v2.model.incident_batch_create_rule_execution_states_request import (
    IncidentBatchCreateRuleExecutionStatesRequest,
)
from datadog_api_client.v2.model.incident_rule_execution_state_rule import IncidentRuleExecutionStateRule
from datadog_api_client.v2.model.incident_rule_execution_state_type import IncidentRuleExecutionStateType
from datetime import datetime
from dateutil.tz import tzutc
from uuid import UUID

body = IncidentBatchCreateRuleExecutionStatesRequest(
    data=IncidentBatchCreateRuleExecutionStatesData(
        attributes=IncidentBatchCreateRuleExecutionStatesDataAttributes(
            rules=[
                IncidentRuleExecutionStateRule(
                    last_executed_at=datetime(2024, 1, 1, 0, 0, tzinfo=tzutc()),
                    rule_uuid=UUID("00000000-0000-0000-0000-000000000000"),
                ),
            ],
        ),
        type=IncidentRuleExecutionStateType.INCIDENT_RULE_EXECUTION_STATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["batch_create_incident_rule_execution_states"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.batch_create_incident_rule_execution_states(incident_id="incident_id", body=body)

    print(response)
