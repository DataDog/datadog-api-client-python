"""
POST request to resolve vulnerable symbols returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.resolve_vulnerable_symbols_request import ResolveVulnerableSymbolsRequest
from datadog_api_client.v2.model.resolve_vulnerable_symbols_request_data import ResolveVulnerableSymbolsRequestData
from datadog_api_client.v2.model.resolve_vulnerable_symbols_request_data_attributes import (
    ResolveVulnerableSymbolsRequestDataAttributes,
)
from datadog_api_client.v2.model.resolve_vulnerable_symbols_request_data_type import (
    ResolveVulnerableSymbolsRequestDataType,
)

body = ResolveVulnerableSymbolsRequest(
    data=ResolveVulnerableSymbolsRequestData(
        attributes=ResolveVulnerableSymbolsRequestDataAttributes(
            purls=[],
        ),
        type=ResolveVulnerableSymbolsRequestDataType.RESOLVE_VULNERABLE_SYMBOLS_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_sca_resolve_vulnerable_symbols"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    response = api_instance.create_sca_resolve_vulnerable_symbols(body=body)

    print(response)
