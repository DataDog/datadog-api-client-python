"""
Update a tag policy returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.tag_policies_api import TagPoliciesApi
from datadog_api_client.v2.model.tag_policy_resource_type import TagPolicyResourceType
from datadog_api_client.v2.model.tag_policy_type import TagPolicyType
from datadog_api_client.v2.model.tag_policy_update_attributes import TagPolicyUpdateAttributes
from datadog_api_client.v2.model.tag_policy_update_data import TagPolicyUpdateData
from datadog_api_client.v2.model.tag_policy_update_request import TagPolicyUpdateRequest

body = TagPolicyUpdateRequest(
    data=TagPolicyUpdateData(
        attributes=TagPolicyUpdateAttributes(
            policy_type=TagPolicyType.SURFACING,
            tag_value_patterns=[],
        ),
        id="123",
        type=TagPolicyResourceType.TAG_POLICY,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_tag_policy"] = True
with ApiClient(configuration) as api_client:
    api_instance = TagPoliciesApi(api_client)
    response = api_instance.update_tag_policy(policy_id="policy_id", body=body)

    print(response)
