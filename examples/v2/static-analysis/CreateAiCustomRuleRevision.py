"""
Create an AI custom rule revision returns "Successfully created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.ai_custom_rule_revision_data_type import AiCustomRuleRevisionDataType
from datadog_api_client.v2.model.ai_custom_rule_revision_execution_mode import AiCustomRuleRevisionExecutionMode
from datadog_api_client.v2.model.ai_custom_rule_revision_request import AiCustomRuleRevisionRequest
from datadog_api_client.v2.model.ai_custom_rule_revision_request_attributes import AiCustomRuleRevisionRequestAttributes
from datadog_api_client.v2.model.ai_custom_rule_revision_request_data import AiCustomRuleRevisionRequestData
from datadog_api_client.v2.model.custom_rule_revision_attributes_category import CustomRuleRevisionAttributesCategory
from datadog_api_client.v2.model.custom_rule_revision_attributes_severity import CustomRuleRevisionAttributesSeverity

body = AiCustomRuleRevisionRequest(
    data=AiCustomRuleRevisionRequestData(
        attributes=AiCustomRuleRevisionRequestAttributes(
            category=CustomRuleRevisionAttributesCategory.SECURITY,
            content="Content",
            cwe="79",
            description="Ruleset description",
            directories=[],
            execution_mode=AiCustomRuleRevisionExecutionMode.AUTO,
            globs=[
                "**/*.py",
            ],
            is_published=False,
            is_testing=False,
            severity=CustomRuleRevisionAttributesSeverity.ERROR,
            short_description="Ruleset short description",
            version_id=1,
        ),
        id="revision-abc-123",
        type=AiCustomRuleRevisionDataType.AI_RULE_REVISION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_ai_custom_rule_revision"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    api_instance.create_ai_custom_rule_revision(ruleset_name="my-ai-ruleset", rule_name="my-ai-rule", body=body)
