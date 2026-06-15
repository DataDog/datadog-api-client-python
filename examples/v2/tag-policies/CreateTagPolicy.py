"""
Create a tag policy returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.tag_policies_api import TagPoliciesApi
from datadog_api_client.v2.model.tag_policy_create_attributes import TagPolicyCreateAttributes
from datadog_api_client.v2.model.tag_policy_create_data import TagPolicyCreateData
from datadog_api_client.v2.model.tag_policy_create_request import TagPolicyCreateRequest
from datadog_api_client.v2.model.tag_policy_create_type import TagPolicyCreateType
from datadog_api_client.v2.model.tag_policy_resource_type import TagPolicyResourceType
from datadog_api_client.v2.model.tag_policy_source import TagPolicySource

body = TagPolicyCreateRequest(
    data=TagPolicyCreateData(
        attributes=TagPolicyCreateAttributes(
            enabled=True,
            negated=False,
            policy_name="Service tag must be one of api or web",
            policy_type=TagPolicyCreateType.SURFACING,
            required=True,
            scope="env",
            source=TagPolicySource.LOGS,
            tag_key="service",
            tag_value_patterns=[
                "api",
                "web",
            ],
        ),
        type=TagPolicyResourceType.TAG_POLICY,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_tag_policy"] = True
with ApiClient(configuration) as api_client:
    api_instance = TagPoliciesApi(api_client)
    response = api_instance.create_tag_policy(body=body)

    print(response)
