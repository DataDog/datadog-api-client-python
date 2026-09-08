"""
Create Custom Ruleset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.argument import Argument
from datadog_api_client.v2.model.custom_rule import CustomRule
from datadog_api_client.v2.model.custom_rule_revision_attributes_category import CustomRuleRevisionAttributesCategory
from datadog_api_client.v2.model.custom_rule_revision_attributes_severity import CustomRuleRevisionAttributesSeverity
from datadog_api_client.v2.model.custom_rule_revision_input import CustomRuleRevisionInput
from datadog_api_client.v2.model.custom_rule_revision_test import CustomRuleRevisionTest
from datadog_api_client.v2.model.custom_ruleset_data_type import CustomRulesetDataType
from datadog_api_client.v2.model.custom_ruleset_request import CustomRulesetRequest
from datadog_api_client.v2.model.custom_ruleset_request_data import CustomRulesetRequestData
from datadog_api_client.v2.model.custom_ruleset_request_data_attributes import CustomRulesetRequestDataAttributes
from datadog_api_client.v2.model.language import Language

body = CustomRulesetRequest(
    data=CustomRulesetRequestData(
        attributes=CustomRulesetRequestDataAttributes(
            description="bG9uZyBkZXNjcmlwdGlvbg==",
            name="my-ruleset",
            rules=[
                CustomRule(
                    id="my-rule",
                    last_revision=CustomRuleRevisionInput(
                        arguments=[
                            Argument(
                                description="YXJndW1lbnQgZGVzY3JpcHRpb24=",
                                name="YXJndW1lbnRfbmFtZQ==",
                            ),
                        ],
                        category=CustomRuleRevisionAttributesCategory.SECURITY,
                        code="Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                        creation_message="Initial revision",
                        cve="CVE-2024-1234",
                        cwe="CWE-79",
                        description="bG9uZyBkZXNjcmlwdGlvbg==",
                        documentation_url="https://docs.example.com/rules/my-rule",
                        is_published=False,
                        is_testing=False,
                        language=Language.PYTHON,
                        severity=CustomRuleRevisionAttributesSeverity.ERROR,
                        short_description="c2hvcnQgZGVzY3JpcHRpb24=",
                        should_use_ai_fix=False,
                        tags=[
                            "security",
                            "custom",
                        ],
                        tests=[
                            CustomRuleRevisionTest(
                                annotation_count=1,
                                code="Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                                filename="test.yaml",
                            ),
                        ],
                        tree_sitter_query="Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                    ),
                    name="my-rule",
                    revisions=[
                        CustomRuleRevisionInput(
                            arguments=[
                                Argument(
                                    description="YXJndW1lbnQgZGVzY3JpcHRpb24=",
                                    name="YXJndW1lbnRfbmFtZQ==",
                                ),
                            ],
                            category=CustomRuleRevisionAttributesCategory.SECURITY,
                            code="Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                            creation_message="Initial revision",
                            cve="CVE-2024-1234",
                            cwe="CWE-79",
                            description="bG9uZyBkZXNjcmlwdGlvbg==",
                            documentation_url="https://docs.example.com/rules/my-rule",
                            is_published=False,
                            is_testing=False,
                            language=Language.PYTHON,
                            severity=CustomRuleRevisionAttributesSeverity.ERROR,
                            short_description="c2hvcnQgZGVzY3JpcHRpb24=",
                            should_use_ai_fix=False,
                            tags=[
                                "security",
                                "custom",
                            ],
                            tests=[
                                CustomRuleRevisionTest(
                                    annotation_count=1,
                                    code="Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                                    filename="test.yaml",
                                ),
                            ],
                            tree_sitter_query="Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
                        ),
                    ],
                ),
            ],
            short_description="c2hvcnQgZGVzY3JpcHRpb24=",
        ),
        id="my-ruleset",
        type=CustomRulesetDataType.CUSTOM_RULESET,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_custom_ruleset"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.create_custom_ruleset(body=body)

    print(response)
