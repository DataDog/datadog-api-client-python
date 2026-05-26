"""
Get AST for source code returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.get_ast_request import GetAstRequest
from datadog_api_client.v2.model.get_ast_request_data import GetAstRequestData
from datadog_api_client.v2.model.get_ast_request_data_attributes import GetAstRequestDataAttributes
from datadog_api_client.v2.model.get_ast_request_data_type import GetAstRequestDataType

body = GetAstRequest(
    data=GetAstRequestData(
        attributes=GetAstRequestDataAttributes(
            code="aW1wb3J0IHN5cw==",
            file_encoding="utf-8",
            language="python",
        ),
        type=GetAstRequestDataType.GET_AST_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_static_analysis_ast"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_static_analysis_ast(body=body)

    print(response)
