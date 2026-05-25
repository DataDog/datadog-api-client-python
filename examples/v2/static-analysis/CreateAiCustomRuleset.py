"""
Create an AI custom ruleset returns "Successfully created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.ai_custom_ruleset_data_type import AiCustomRulesetDataType
from datadog_api_client.v2.model.ai_custom_ruleset_request import AiCustomRulesetRequest
from datadog_api_client.v2.model.ai_custom_ruleset_request_attributes import AiCustomRulesetRequestAttributes
from datadog_api_client.v2.model.ai_custom_ruleset_request_data import AiCustomRulesetRequestData

body = AiCustomRulesetRequest(
    data=AiCustomRulesetRequestData(
        attributes=AiCustomRulesetRequestAttributes(
            description="Ruleset description",
            name="my-ai-ruleset",
            short_description="Ruleset short description",
        ),
        id="my-ai-ruleset",
        type=AiCustomRulesetDataType.AI_RULESET,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_ai_custom_ruleset"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.create_ai_custom_ruleset(body=body)

    print(response)
