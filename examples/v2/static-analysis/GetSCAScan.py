"""
Retrieve a dependency scan result returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi

configuration = Configuration()
configuration.unstable_operations["get_sca_scan"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.get_sca_scan(
        job_id="0190a3d4-1234-7000-8000-000000000000",
    )

    print(response)
