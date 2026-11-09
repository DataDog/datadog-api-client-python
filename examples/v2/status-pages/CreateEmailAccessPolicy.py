"""
Create an email access policy returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.access_policy_effect import AccessPolicyEffect
from datadog_api_client.v2.model.create_status_page_email_access_policy_request import (
    CreateStatusPageEmailAccessPolicyRequest,
)
from datadog_api_client.v2.model.create_status_page_email_access_policy_request_data import (
    CreateStatusPageEmailAccessPolicyRequestData,
)
from datadog_api_client.v2.model.create_status_page_email_access_policy_request_data_attributes import (
    CreateStatusPageEmailAccessPolicyRequestDataAttributes,
)
from datadog_api_client.v2.model.status_page_email_access_policy_type import StatusPageEmailAccessPolicyType

# there is a valid "private_status_page" in the system
PRIVATE_STATUS_PAGE_DATA_ID = environ["PRIVATE_STATUS_PAGE_DATA_ID"]

body = CreateStatusPageEmailAccessPolicyRequest(
    data=CreateStatusPageEmailAccessPolicyRequestData(
        attributes=CreateStatusPageEmailAccessPolicyRequestDataAttributes(
            effect=AccessPolicyEffect.ALLOW,
            pattern="@example.com",
        ),
        type=StatusPageEmailAccessPolicyType.EMAIL_ACCESS_POLICIES,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.create_email_access_policy(page_id=PRIVATE_STATUS_PAGE_DATA_ID, body=body)

    print(response)
