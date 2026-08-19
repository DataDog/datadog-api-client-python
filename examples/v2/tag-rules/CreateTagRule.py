"""
Create a tag rule returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.tag_rules_api import TagRulesApi
from datadog_api_client.v2.model.tag_rule_create_attributes import TagRuleCreateAttributes
from datadog_api_client.v2.model.tag_rule_create_data import TagRuleCreateData
from datadog_api_client.v2.model.tag_rule_create_request import TagRuleCreateRequest
from datadog_api_client.v2.model.tag_rule_create_type import TagRuleCreateType
from datadog_api_client.v2.model.tag_rule_resource_type import TagRuleResourceType
from datadog_api_client.v2.model.tag_rule_source import TagRuleSource

body = TagRuleCreateRequest(
    data=TagRuleCreateData(
        attributes=TagRuleCreateAttributes(
            enabled=True,
            name="Service tag must be one of api or web",
            negated=False,
            required=True,
            rule_type=TagRuleCreateType.SURFACING,
            scope="env",
            source=TagRuleSource.LOGS,
            tag_key="service",
            tag_value_patterns=[
                "api",
                "web",
            ],
        ),
        type=TagRuleResourceType.TAG_RULE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_tag_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = TagRulesApi(api_client)
    response = api_instance.create_tag_rule(body=body)

    print(response)
