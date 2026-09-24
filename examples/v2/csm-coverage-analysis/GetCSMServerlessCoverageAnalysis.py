"""
Get the CSM Serverless Coverage Analysis returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_coverage_analysis_api import CSMCoverageAnalysisApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = CSMCoverageAnalysisApi(api_client)
    response = api_instance.get_csm_serverless_coverage_analysis()

    print(response)
