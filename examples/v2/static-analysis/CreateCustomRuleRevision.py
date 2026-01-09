"""
Create Custom Rule Revision returns "Successfully created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.argument import Argument
from datadog_api_client.v2.model.custom_rule_revision_attributes import CustomRuleRevisionAttributes
from datadog_api_client.v2.model.custom_rule_revision_attributes_category import CustomRuleRevisionAttributesCategory
from datadog_api_client.v2.model.custom_rule_revision_attributes_severity import CustomRuleRevisionAttributesSeverity
from datadog_api_client.v2.model.custom_rule_revision_data_type import CustomRuleRevisionDataType
from datadog_api_client.v2.model.custom_rule_revision_request import CustomRuleRevisionRequest
from datadog_api_client.v2.model.custom_rule_revision_request_data import CustomRuleRevisionRequestData
from datadog_api_client.v2.model.custom_rule_revision_test import CustomRuleRevisionTest
from datadog_api_client.v2.model.language import Language
from datetime import datetime
from dateutil.tz import tzutc

body = CustomRuleRevisionRequest(
    data=CustomRuleRevisionRequestData(
        attributes=CustomRuleRevisionAttributes(
            arguments=[
                Argument(
                    description="YXJndW1lbnQgZGVzY3JpcHRpb24=",
                    name="YXJndW1lbnRfbmFtZQ==",
                ),
            ],
            category=CustomRuleRevisionAttributesCategory.SECURITY,
            checksum="8a66c4e4e631099ad71be3c1ea3ea8fc2d57193e56db2c296e2dd8a508b26b99",
            code="Y29uZHVjdG9yOgogICAgLSBkZXBsb3lfb25seTogdHJ1ZQ==",
            created_at=datetime(2026, 1, 9, 13, 0, 57, 473141, tzinfo=tzutc()),
            created_by="foobarbaz",
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
        type=CustomRuleRevisionDataType.CUSTOM_RULE_REVISION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_custom_rule_revision"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    api_instance.create_custom_rule_revision(ruleset_name="ruleset_name", rule_name="rule_name", body=body)
