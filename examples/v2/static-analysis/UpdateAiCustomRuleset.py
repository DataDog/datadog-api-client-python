"""
Update an AI custom ruleset returns "Successfully updated" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.ai_custom_ruleset_data_type import AiCustomRulesetDataType
from datadog_api_client.v2.model.ai_custom_ruleset_update_attributes import AiCustomRulesetUpdateAttributes
from datadog_api_client.v2.model.ai_custom_ruleset_update_data import AiCustomRulesetUpdateData
from datadog_api_client.v2.model.ai_custom_ruleset_update_request import AiCustomRulesetUpdateRequest

body = AiCustomRulesetUpdateRequest(
    data=AiCustomRulesetUpdateData(
        attributes=AiCustomRulesetUpdateAttributes(
            description="Ruleset description",
            name="my-ai-ruleset",
            short_description="Ruleset short description",
        ),
        id="my-ai-ruleset",
        type=AiCustomRulesetDataType.AI_RULESET,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_ai_custom_ruleset"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    api_instance.update_ai_custom_ruleset(ruleset_name="my-ai-ruleset", body=body)
