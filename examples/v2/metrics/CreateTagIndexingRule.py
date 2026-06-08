"""
Create a tag indexing rule returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.tag_indexing_rule_create_attributes import TagIndexingRuleCreateAttributes
from datadog_api_client.v2.model.tag_indexing_rule_create_data import TagIndexingRuleCreateData
from datadog_api_client.v2.model.tag_indexing_rule_create_request import TagIndexingRuleCreateRequest
from datadog_api_client.v2.model.tag_indexing_rule_dynamic_tags import TagIndexingRuleDynamicTags
from datadog_api_client.v2.model.tag_indexing_rule_metric_match import TagIndexingRuleMetricMatch
from datadog_api_client.v2.model.tag_indexing_rule_options import TagIndexingRuleOptions
from datadog_api_client.v2.model.tag_indexing_rule_options_data import TagIndexingRuleOptionsData
from datadog_api_client.v2.model.tag_indexing_rule_type import TagIndexingRuleType

body = TagIndexingRuleCreateRequest(
    data=TagIndexingRuleCreateData(
        attributes=TagIndexingRuleCreateAttributes(
            exclude_tags_mode=False,
            ignored_metric_name_matches=[],
            metric_name_matches=[
                "dd.test.*",
            ],
            name="my-indexing-rule",
            options=TagIndexingRuleOptions(
                data=TagIndexingRuleOptionsData(
                    dynamic_tags=TagIndexingRuleDynamicTags(
                        queried_tags_window_seconds=3600,
                        related_asset_tags=False,
                    ),
                    manage_preexisting_metrics=True,
                    metric_match=TagIndexingRuleMetricMatch(
                        queried_window_seconds=3600,
                    ),
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
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.create_tag_indexing_rule(body=body)

    print(response)
