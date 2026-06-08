"""
Create a tag indexing rule exemption returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.tag_indexing_rule_exemption_create_attributes import (
    TagIndexingRuleExemptionCreateAttributes,
)
from datadog_api_client.v2.model.tag_indexing_rule_exemption_create_data import TagIndexingRuleExemptionCreateData
from datadog_api_client.v2.model.tag_indexing_rule_exemption_create_request import TagIndexingRuleExemptionCreateRequest
from datadog_api_client.v2.model.tag_indexing_rule_exemption_type import TagIndexingRuleExemptionType

body = TagIndexingRuleExemptionCreateRequest(
    data=TagIndexingRuleExemptionCreateData(
        attributes=TagIndexingRuleExemptionCreateAttributes(
            reason="This metric has a pre-existing tag configuration.",
        ),
        type=TagIndexingRuleExemptionType.TAG_INDEXING_RULE_EXEMPTIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.create_tag_indexing_rule_exemption(metric_name="metric_name", body=body)

    print(response)
