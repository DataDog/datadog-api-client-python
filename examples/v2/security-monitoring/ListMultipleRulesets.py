"""
Ruleset get multiple returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.get_multiple_rulesets_request import GetMultipleRulesetsRequest
from datadog_api_client.v2.model.get_multiple_rulesets_request_data import GetMultipleRulesetsRequestData
from datadog_api_client.v2.model.get_multiple_rulesets_request_data_attributes import (
    GetMultipleRulesetsRequestDataAttributes,
)
from datadog_api_client.v2.model.get_multiple_rulesets_request_data_type import GetMultipleRulesetsRequestDataType

body = GetMultipleRulesetsRequest(
    data=GetMultipleRulesetsRequestData(
        attributes=GetMultipleRulesetsRequestDataAttributes(
            rulesets=[],
        ),
        type=GetMultipleRulesetsRequestDataType.GET_MULTIPLE_RULESETS_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["list_multiple_rulesets"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.list_multiple_rulesets(body=body)

    print(response)
