"""
Create a tag indexing rule with exclude-mode tag usage fields returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.tag_indexing_rule_create_attributes import TagIndexingRuleCreateAttributes
from datadog_api_client.v2.model.tag_indexing_rule_create_data import TagIndexingRuleCreateData
from datadog_api_client.v2.model.tag_indexing_rule_create_request import TagIndexingRuleCreateRequest
from datadog_api_client.v2.model.tag_indexing_rule_dynamic_tags import TagIndexingRuleDynamicTags
from datadog_api_client.v2.model.tag_indexing_rule_options import TagIndexingRuleOptions
from datadog_api_client.v2.model.tag_indexing_rule_options_data import TagIndexingRuleOptionsData
from datadog_api_client.v2.model.tag_indexing_rule_type import TagIndexingRuleType

body = TagIndexingRuleCreateRequest(
    data=TagIndexingRuleCreateData(
        attributes=TagIndexingRuleCreateAttributes(
            exclude_tags_mode=True,
            ignored_metric_name_matches=[],
            metric_name_matches=[
                "dd.test.*",
            ],
            name="my-indexing-rule",
            options=TagIndexingRuleOptions(
                data=TagIndexingRuleOptionsData(
                    dynamic_tags=TagIndexingRuleDynamicTags(
                        exclude_not_queried_window_seconds=3600,
                        exclude_not_used_in_assets=True,
                    ),
                    manage_preexisting_metrics=True,
                    override_previous_rules=False,
                ),
                version=1,
            ),
            tags=[
                "env",
                "service",
            ],
        ),
        type=TagIndexingRuleType.TAG_INDEXING_RULES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_tag_indexing_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.create_tag_indexing_rule(body=body)

    print(response)
