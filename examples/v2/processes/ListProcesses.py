"""
Get all processes returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.processes_api import ProcessesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ProcessesApi(api_client)
    response = api_instance.list_processes(
        search="process-agent",
        tags="testing:true",
        page_limit=2,
    )

    print(response)
