"""
Analyze code returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.analysis_request import AnalysisRequest
from datadog_api_client.v2.model.analysis_request_data import AnalysisRequestData
from datadog_api_client.v2.model.analysis_request_data_attributes import AnalysisRequestDataAttributes
from datadog_api_client.v2.model.analysis_request_data_type import AnalysisRequestDataType
from datadog_api_client.v2.model.analysis_request_rule import AnalysisRequestRule

body = AnalysisRequest(
    data=AnalysisRequestData(
        attributes=AnalysisRequestDataAttributes(
            code="aW1wb3J0IHN5cw==",
            file_encoding="utf-8",
            filename="test.py",
            language="python",
            rules=[
                AnalysisRequestRule(
                    category="BEST_PRACTICES",
                    checksum="abc123def456",
                    code="ZnVuY3Rpb24gdmlzaXQobm9kZSkge30=",
                    entity_checked=None,
                    id="python-best-practices/no-exit",
                    language="python",
                    regex=None,
                    severity="WARNING",
                    tree_sitter_query="KGNhbGwgbmFtZTogKGF0dHJpYnV0ZSkpQHZhbA==",
                    type="TREE_SITTER_QUERY",
                ),
            ],
        ),
        type=AnalysisRequestDataType.ANALYSIS_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_static_analysis_server_analysis"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_static_analysis_server_analysis(body=body)

    print(response)
