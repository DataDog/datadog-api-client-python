"""
Reorder the list of inbox rules in the pipeline returns "The list of inbox rules" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.inbox_rules_type import InboxRulesType
from datadog_api_client.v2.model.reorder_inbox_rules_parameters import ReorderInboxRulesParameters
from datadog_api_client.v2.model.reorder_inbox_rules_parameters_data import ReorderInboxRulesParametersData
from uuid import UUID

body = ReorderInboxRulesParameters(
    data=[
        ReorderInboxRulesParametersData(
            id=UUID("123e4567-e89b-12d3-a456-426655440000"),
            type=InboxRulesType.INBOX_RULES,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.reorder_inbox_rules(body=body)

    print(response)
