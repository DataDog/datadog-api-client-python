"""
Update a tag policy returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.tag_policies_api import TagPoliciesApi
from datadog_api_client.v2.model.tag_policy_attributes_update_request import TagPolicyAttributesUpdateRequest
from datadog_api_client.v2.model.tag_policy_data_update_request import TagPolicyDataUpdateRequest
from datadog_api_client.v2.model.tag_policy_type import TagPolicyType
from datadog_api_client.v2.model.tag_policy_update_request import TagPolicyUpdateRequest

body = TagPolicyUpdateRequest(
    data=TagPolicyDataUpdateRequest(
        attributes=TagPolicyAttributesUpdateRequest(
            enabled=True,
            negated=False,
            policy_name="production-tags-policy",
            required=True,
            scope="env",
            source="logs",
            tag_key="service",
            tag_value_patterns=[
                "api",
                "web",
            ],
        ),
        type=TagPolicyType.TAG_POLICY,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_tag_policy"] = True
with ApiClient(configuration) as api_client:
    api_instance = TagPoliciesApi(api_client)
    response = api_instance.update_tag_policy(policy_id="123", body=body)

    print(response)
