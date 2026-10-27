"""
Update a tag indexing rule exemption returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.tag_indexing_rule_exemption_type import TagIndexingRuleExemptionType
from datadog_api_client.v2.model.tag_indexing_rule_exemption_update_attributes import (
    TagIndexingRuleExemptionUpdateAttributes,
)
from datadog_api_client.v2.model.tag_indexing_rule_exemption_update_data import TagIndexingRuleExemptionUpdateData
from datadog_api_client.v2.model.tag_indexing_rule_exemption_update_request import TagIndexingRuleExemptionUpdateRequest

body = TagIndexingRuleExemptionUpdateRequest(
    data=TagIndexingRuleExemptionUpdateData(
        attributes=TagIndexingRuleExemptionUpdateAttributes(
            reason="This metric must remain exempt because of its query requirements.",
        ),
        type=TagIndexingRuleExemptionType.TAG_INDEXING_RULE_EXEMPTIONS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_tag_indexing_rule_exemption"] = True
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.update_tag_indexing_rule_exemption(metric_name="metric_name", body=body)

    print(response)
