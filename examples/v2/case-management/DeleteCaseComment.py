"""
Delete case comment returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

# there is a valid "comment" in the system
COMMENT_ID = environ["COMMENT_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.delete_case_comment(
        case_id=CASE_ID,
        cell_id=COMMENT_ID,
    )
