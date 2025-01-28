"""
Reorder the list of mute rules in the pipeline returns "The list of mute rules" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.mute_rules_type import MuteRulesType
from datadog_api_client.v2.model.reorder_mute_rules_parameters import ReorderMuteRulesParameters
from datadog_api_client.v2.model.reorder_mute_rules_parameters_data import ReorderMuteRulesParametersData
from uuid import UUID

body = ReorderMuteRulesParameters(
    data=[
        ReorderMuteRulesParametersData(
            id=UUID("123e4567-e89b-12d3-a456-426655440000"),
            type=MuteRulesType.MUTE_RULES,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.reorder_mute_rules(body=body)

    print(response)
