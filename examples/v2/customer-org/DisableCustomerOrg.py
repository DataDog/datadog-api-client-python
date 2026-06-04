"""
Disable the authenticated customer organization returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.customer_org_api import CustomerOrgApi
from datadog_api_client.v2.model.customer_org_disable_request import CustomerOrgDisableRequest
from datadog_api_client.v2.model.customer_org_disable_request_attributes import CustomerOrgDisableRequestAttributes
from datadog_api_client.v2.model.customer_org_disable_request_data import CustomerOrgDisableRequestData
from datadog_api_client.v2.model.customer_org_disable_type import CustomerOrgDisableType

body = CustomerOrgDisableRequest(
    data=CustomerOrgDisableRequestData(
        attributes=CustomerOrgDisableRequestAttributes(
            org_uuid="abcdef01-2345-6789-abcd-ef0123456789",
        ),
        id="1",
        type=CustomerOrgDisableType.CUSTOMER_ORG_DISABLE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["disable_customer_org"] = True
with ApiClient(configuration) as api_client:
    api_instance = CustomerOrgApi(api_client)
    response = api_instance.disable_customer_org(body=body)

    print(response)
