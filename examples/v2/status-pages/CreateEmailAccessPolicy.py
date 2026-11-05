"""
Create an email access policy returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.create_status_page_email_access_policy_request import (
    CreateStatusPageEmailAccessPolicyRequest,
)
from datadog_api_client.v2.model.create_status_page_email_access_policy_request_data import (
    CreateStatusPageEmailAccessPolicyRequestData,
)
from datadog_api_client.v2.model.create_status_page_email_access_policy_request_data_attributes import (
    CreateStatusPageEmailAccessPolicyRequestDataAttributes,
)
from datadog_api_client.v2.model.execution_policy_effect import ExecutionPolicyEffect
from datadog_api_client.v2.model.status_page_email_access_policy_type import StatusPageEmailAccessPolicyType
from uuid import UUID

body = CreateStatusPageEmailAccessPolicyRequest(
    data=CreateStatusPageEmailAccessPolicyRequestData(
        attributes=CreateStatusPageEmailAccessPolicyRequestDataAttributes(
            effect=ExecutionPolicyEffect.ALLOW,
            pattern="@example.com",
        ),
        type=StatusPageEmailAccessPolicyType.EMAIL_ACCESS_POLICIES,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.create_email_access_policy(page_id=UUID("1234abcd-12ab-34cd-56ef-123456abcdef"), body=body)

    print(response)
