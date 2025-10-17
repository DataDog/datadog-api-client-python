"""
Delete a case type returns "NotContent" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_type_api import CaseManagementTypeApi

# there is a valid "case_type" in the system
CASE_TYPE_ID = environ["CASE_TYPE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementTypeApi(api_client)
    api_instance.delete_case_type(
        case_type_id=CASE_TYPE_ID,
    )
