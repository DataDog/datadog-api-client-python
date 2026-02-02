"""
Create a tag policy returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.tag_policies_api import TagPoliciesApi
from datadog_api_client.v2.model.tag_policy_attributes_request import TagPolicyAttributesRequest
from datadog_api_client.v2.model.tag_policy_create_request import TagPolicyCreateRequest
from datadog_api_client.v2.model.tag_policy_data_request import TagPolicyDataRequest
from datadog_api_client.v2.model.tag_policy_type import TagPolicyType

body = TagPolicyCreateRequest(
    data=TagPolicyDataRequest(
        attributes=TagPolicyAttributesRequest(
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
configuration.unstable_operations["create_tag_policy"] = True
with ApiClient(configuration) as api_client:
    api_instance = TagPoliciesApi(api_client)
    response = api_instance.create_tag_policy(body=body)

    print(response)
