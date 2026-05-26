"""
Get tree-sitter WASM file returns "BLOB with the content of the WASM file" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi

configuration = Configuration()
configuration.unstable_operations["get_static_analysis_tree_sitter_wasm"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.get_static_analysis_tree_sitter_wasm(
        file="tree-sitter-python.wasm",
    )

    print(response.read())
