"""
Create a child organization returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.organizations_api import OrganizationsApi
from datadog_api_client.v1.model.organization_billing import OrganizationBilling
from datadog_api_client.v1.model.organization_create_body import OrganizationCreateBody
from datadog_api_client.v1.model.organization_subscription import OrganizationSubscription

body = OrganizationCreateBody(
    billing=OrganizationBilling(
        type="parent_billing",
    ),
    name="New child org",
    subscription=OrganizationSubscription(
        type="pro",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    response = api_instance.create_child_org(body=body)

    print(response)
