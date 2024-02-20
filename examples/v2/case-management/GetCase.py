"""
Get the details of a case returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.get_case(
        case_id=CASE_ID,
    )

    print(response)
