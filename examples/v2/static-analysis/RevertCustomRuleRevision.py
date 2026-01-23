"""
Revert Custom Rule Revision returns "Successfully reverted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.revert_custom_rule_revision_data_type import RevertCustomRuleRevisionDataType
from datadog_api_client.v2.model.revert_custom_rule_revision_request import RevertCustomRuleRevisionRequest
from datadog_api_client.v2.model.revert_custom_rule_revision_request_data import RevertCustomRuleRevisionRequestData
from datadog_api_client.v2.model.revert_custom_rule_revision_request_data_attributes import (
    RevertCustomRuleRevisionRequestDataAttributes,
)

body = RevertCustomRuleRevisionRequest(
    data=RevertCustomRuleRevisionRequestData(
        attributes=RevertCustomRuleRevisionRequestDataAttributes(),
        type=RevertCustomRuleRevisionDataType.REVERT_CUSTOM_RULE_REVISION_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["revert_custom_rule_revision"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    api_instance.revert_custom_rule_revision(ruleset_name="ruleset_name", rule_name="rule_name", body=body)
