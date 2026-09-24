"""
Create an AI custom rule returns "Successfully created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.ai_custom_rule_data_type import AiCustomRuleDataType
from datadog_api_client.v2.model.ai_custom_rule_request import AiCustomRuleRequest
from datadog_api_client.v2.model.ai_custom_rule_request_attributes import AiCustomRuleRequestAttributes
from datadog_api_client.v2.model.ai_custom_rule_request_data import AiCustomRuleRequestData

body = AiCustomRuleRequest(
    data=AiCustomRuleRequestData(
        attributes=AiCustomRuleRequestAttributes(
            name="my-ai-rule",
        ),
        id="my-ai-rule",
        type=AiCustomRuleDataType.AI_RULE,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_ai_custom_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.create_ai_custom_rule(ruleset_name="my-ai-ruleset", body=body)

    print(response)
