"""
Delete an email access policy returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi

# there is a valid "private_status_page" in the system
PRIVATE_STATUS_PAGE_DATA_ID = environ["PRIVATE_STATUS_PAGE_DATA_ID"]

# there is a valid "email_access_policy" in the system
EMAIL_ACCESS_POLICY_DATA_ID = environ["EMAIL_ACCESS_POLICY_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    api_instance.delete_email_access_policy(
        page_id=PRIVATE_STATUS_PAGE_DATA_ID,
        policy_id=EMAIL_ACCESS_POLICY_DATA_ID,
    )
