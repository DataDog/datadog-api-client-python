"""
Create a WAF custom rule returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi
from datadog_api_client.v2.model.application_security_waf_custom_rule_action import (
    ApplicationSecurityWafCustomRuleAction,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_action_action import (
    ApplicationSecurityWafCustomRuleActionAction,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_action_parameters import (
    ApplicationSecurityWafCustomRuleActionParameters,
)
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
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_options import (
    ApplicationSecurityWafCustomRuleConditionOptions,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_condition_parameters import (
    ApplicationSecurityWafCustomRuleConditionParameters,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_create_attributes import (
    ApplicationSecurityWafCustomRuleCreateAttributes,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_create_data import (
    ApplicationSecurityWafCustomRuleCreateData,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_create_request import (
    ApplicationSecurityWafCustomRuleCreateRequest,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_scope import ApplicationSecurityWafCustomRuleScope
from datadog_api_client.v2.model.application_security_waf_custom_rule_tags import ApplicationSecurityWafCustomRuleTags
from datadog_api_client.v2.model.application_security_waf_custom_rule_tags_category import (
    ApplicationSecurityWafCustomRuleTagsCategory,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_type import ApplicationSecurityWafCustomRuleType

body = ApplicationSecurityWafCustomRuleCreateRequest(
    data=ApplicationSecurityWafCustomRuleCreateData(
        attributes=ApplicationSecurityWafCustomRuleCreateAttributes(
            action=ApplicationSecurityWafCustomRuleAction(
                action=ApplicationSecurityWafCustomRuleActionAction.BLOCK_REQUEST,
                parameters=ApplicationSecurityWafCustomRuleActionParameters(
                    location="/blocking",
                    status_code=403,
                ),
            ),
            blocking=False,
            conditions=[
                ApplicationSecurityWafCustomRuleCondition(
                    operator=ApplicationSecurityWafCustomRuleConditionOperator.MATCH_REGEX,
                    parameters=ApplicationSecurityWafCustomRuleConditionParameters(
                        data="blocked_users",
                        inputs=[
                            ApplicationSecurityWafCustomRuleConditionInput(
                                address=ApplicationSecurityWafCustomRuleConditionInputAddress.SERVER_DB_STATEMENT,
                                key_path=[],
                            ),
                        ],
                        list=[],
                        options=ApplicationSecurityWafCustomRuleConditionOptions(
                            case_sensitive=False,
                            min_length=0,
                        ),
                        regex="path.*",
                        value="custom_tag",
                    ),
                ),
            ],
            enabled=False,
            name="Block request from a bad useragent",
            path_glob="/api/search/*",
            scope=[
                ApplicationSecurityWafCustomRuleScope(
                    env="prod",
                    service="billing-service",
                ),
            ],
            tags=ApplicationSecurityWafCustomRuleTags(
                category=ApplicationSecurityWafCustomRuleTagsCategory.BUSINESS_LOGIC,
                type="users.login.success",
            ),
        ),
        type=ApplicationSecurityWafCustomRuleType.CUSTOM_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.create_application_security_waf_custom_rule(body=body)

    print(response)
