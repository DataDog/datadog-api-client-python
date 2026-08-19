"""
Update a tag rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.tag_rules_api import TagRulesApi
from datadog_api_client.v2.model.tag_rule_resource_type import TagRuleResourceType
from datadog_api_client.v2.model.tag_rule_type import TagRuleType
from datadog_api_client.v2.model.tag_rule_update_attributes import TagRuleUpdateAttributes
from datadog_api_client.v2.model.tag_rule_update_data import TagRuleUpdateData
from datadog_api_client.v2.model.tag_rule_update_request import TagRuleUpdateRequest

body = TagRuleUpdateRequest(
    data=TagRuleUpdateData(
        attributes=TagRuleUpdateAttributes(
            rule_type=TagRuleType.SURFACING,
            tag_value_patterns=[],
        ),
        id="123",
        type=TagRuleResourceType.TAG_RULE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_tag_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = TagRulesApi(api_client)
    response = api_instance.update_tag_rule(rule_id="rule_id", body=body)

    print(response)
