"""
Get the CSM Cloud Accounts Coverage Analysis returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_coverage_analysis_api import CSMCoverageAnalysisApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMCoverageAnalysisApi(api_client)
    response = api_instance.get_csm_cloud_accounts_coverage_analysis()

    print(response)