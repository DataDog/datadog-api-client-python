"""
Create Custom Rule returns "Successfully created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.custom_rule_data_type import CustomRuleDataType
from datadog_api_client.v2.model.custom_rule_request import CustomRuleRequest
from datadog_api_client.v2.model.custom_rule_request_data import CustomRuleRequestData
from datadog_api_client.v2.model.custom_rule_request_data_attributes import CustomRuleRequestDataAttributes

body = CustomRuleRequest(
    data=CustomRuleRequestData(
        attributes=CustomRuleRequestDataAttributes(),
        type=CustomRuleDataType.CUSTOM_RULE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_custom_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.create_custom_rule(ruleset_name="ruleset_name", body=body)

    print(response)
