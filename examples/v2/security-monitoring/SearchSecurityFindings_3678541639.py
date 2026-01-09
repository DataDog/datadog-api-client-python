"""
Search security findings returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_findings_search_request import SecurityFindingsSearchRequest
from datadog_api_client.v2.model.security_findings_search_request_data import SecurityFindingsSearchRequestData
from datadog_api_client.v2.model.security_findings_search_request_data_attributes import (
    SecurityFindingsSearchRequestDataAttributes,
)
from datadog_api_client.v2.model.security_findings_search_request_page import SecurityFindingsSearchRequestPage

body = SecurityFindingsSearchRequest(
    data=SecurityFindingsSearchRequestData(
        attributes=SecurityFindingsSearchRequestDataAttributes(
            filter="@severity:(critical OR high)",
            page=SecurityFindingsSearchRequestPage(
                limit=1,
            ),
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["search_security_findings"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.search_security_findings(body=body)

    print(response)
