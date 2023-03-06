"""
Update a restriction policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.restriction_policies_api import RestrictionPoliciesApi
from datadog_api_client.v2.model.restriction_policy import RestrictionPolicy
from datadog_api_client.v2.model.restriction_policy_attributes import RestrictionPolicyAttributes
from datadog_api_client.v2.model.restriction_policy_binding import RestrictionPolicyBinding
from datadog_api_client.v2.model.restriction_policy_type import RestrictionPolicyType
from datadog_api_client.v2.model.restriction_policy_update_request import RestrictionPolicyUpdateRequest

# there is a valid "user" in the system
USER_DATA_RELATIONSHIPS_ORG_DATA_ID = environ["USER_DATA_RELATIONSHIPS_ORG_DATA_ID"]

body = RestrictionPolicyUpdateRequest(
    data=RestrictionPolicy(
        id="dashboard:test-update",
        type=RestrictionPolicyType.RESTRICTION_POLICY,
        attributes=RestrictionPolicyAttributes(
            bindings=[
                RestrictionPolicyBinding(
                    relation="editor",
                    principals=[
                        "org:00000000-0000-beef-0000-000000000000",
                    ],
                ),
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RestrictionPoliciesApi(api_client)
    response = api_instance.update_restriction_policy(resource_id="dashboard:test-update", body=body)

    print(response)
