"""
Get the CSM Hosts and Containers Coverage Analysis returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_coverage_analysis_api import CSMCoverageAnalysisApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMCoverageAnalysisApi(api_client)
    response = api_instance.get_csm_hosts_and_containers_coverage_analysis()

    print(response)
