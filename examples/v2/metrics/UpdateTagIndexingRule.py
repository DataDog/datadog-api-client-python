"""
Update a tag indexing rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.tag_indexing_rule_dynamic_tags import TagIndexingRuleDynamicTags
from datadog_api_client.v2.model.tag_indexing_rule_metric_match import TagIndexingRuleMetricMatch
from datadog_api_client.v2.model.tag_indexing_rule_options import TagIndexingRuleOptions
from datadog_api_client.v2.model.tag_indexing_rule_options_data import TagIndexingRuleOptionsData
from datadog_api_client.v2.model.tag_indexing_rule_type import TagIndexingRuleType
from datadog_api_client.v2.model.tag_indexing_rule_update_attributes import TagIndexingRuleUpdateAttributes
from datadog_api_client.v2.model.tag_indexing_rule_update_data import TagIndexingRuleUpdateData
from datadog_api_client.v2.model.tag_indexing_rule_update_request import TagIndexingRuleUpdateRequest

# there is a valid "tag_indexing_rule" in the system
TAG_INDEXING_RULE_DATA_ID = environ["TAG_INDEXING_RULE_DATA_ID"]

body = TagIndexingRuleUpdateRequest(
    data=TagIndexingRuleUpdateData(
        attributes=TagIndexingRuleUpdateAttributes(
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
            rule_order=2,
            tags=[
                "env",
                "service",
            ],
        ),
        type=TagIndexingRuleType.TAG_INDEXING_RULES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_tag_indexing_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.update_tag_indexing_rule(id=TAG_INDEXING_RULE_DATA_ID, body=body)

    print(response)
