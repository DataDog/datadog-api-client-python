"""
Update a WAF Custom Rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition import (
    ApplicationSecurityWafCustomRuleCondition,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_input import (
    ApplicationSecurityWafCustomRuleConditionInput,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_input_address import (
    ApplicationSecurityWafCustomRuleConditionInputAddress,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_operator import (
    ApplicationSecurityWafCustomRuleConditionOperator,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_parameters import (
    ApplicationSecurityWafCustomRuleConditionParameters,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_scope import ApplicationSecurityWafCustomRuleScope
from datadog_api_client.v2.model.application_security_waf_custom_rule_tags import ApplicationSecurityWafCustomRuleTags
from datadog_api_client.v2.model.application_security_waf_custom_rule_tags_category import (
    ApplicationSecurityWafCustomRuleTagsCategory,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_type import ApplicationSecurityWafCustomRuleType
from datadog_api_client.v2.model.application_security_waf_custom_rule_update_attributes import (
    ApplicationSecurityWafCustomRuleUpdateAttributes,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_update_data import (
    ApplicationSecurityWafCustomRuleUpdateData,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_update_request import (
    ApplicationSecurityWafCustomRuleUpdateRequest,
)

# there is a valid "custom_rule" in the system
CUSTOM_RULE_DATA_ID = environ["CUSTOM_RULE_DATA_ID"]

body = ApplicationSecurityWafCustomRuleUpdateRequest(
    data=ApplicationSecurityWafCustomRuleUpdateData(
        type=ApplicationSecurityWafCustomRuleType.CUSTOM_RULE,
        attributes=ApplicationSecurityWafCustomRuleUpdateAttributes(
            blocking=False,
            conditions=[
                ApplicationSecurityWafCustomRuleCondition(
                    operator=ApplicationSecurityWafCustomRuleConditionOperator.MATCH_REGEX,
                    parameters=ApplicationSecurityWafCustomRuleConditionParameters(
                        inputs=[
                            ApplicationSecurityWafCustomRuleConditionInput(
                                address=ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_REQUEST_QUERY,
                                key_path=[
                                    "id",
                                ],
                            ),
                        ],
                        regex="badactor",
                    ),
                ),
            ],
            enabled=False,
            name="test",
            path_glob="/test",
            scope=[
                ApplicationSecurityWafCustomRuleScope(
                    env="test",
                    service="test",
                ),
            ],
            tags=ApplicationSecurityWafCustomRuleTags(
                category=ApplicationSecurityWafCustomRuleTagsCategory.ATTACK_ATTEMPT,
                type="test",
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.update_application_security_waf_custom_rule(custom_rule_id=CUSTOM_RULE_DATA_ID, body=body)

    print(response)
