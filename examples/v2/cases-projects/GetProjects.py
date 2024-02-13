"""
Get all projects returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cases_projects_api import CasesProjectsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CasesProjectsApi(api_client)
    response = api_instance.get_projects()

    print(response)
