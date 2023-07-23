"""
Update a restriction policy returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.restriction_policies_api import RestrictionPoliciesApi
from datadog_api_client.v2.model.restriction_policy_binding import RestrictionPolicyBinding
from datadog_api_client.v2.model.restriction_policy_update_request import RestrictionPolicyUpdateRequestJSON

# there is a valid "user" in the system
USER_DATA_RELATIONSHIPS_ORG_DATA_ID = environ["USER_DATA_RELATIONSHIPS_ORG_DATA_ID"]

body = RestrictionPolicyUpdateRequestJSON(
    id="dashboard:test-update",
    bindings=[
        RestrictionPolicyBinding(
            relation="editor",
            principals=[
                "org:00000000-0000-beef-0000-000000000000",
            ],
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RestrictionPoliciesApi(api_client)
    response = api_instance.update_restriction_policy(resource_id="dashboard:test-update", body=body)

    print(response)
