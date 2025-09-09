"""
Validate a suppression rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_suppression_create_attributes import (
    SecurityMonitoringSuppressionCreateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_suppression_create_data import (
    SecurityMonitoringSuppressionCreateData,
)
from datadog_api_client.v2.model.security_monitoring_suppression_create_request import (
    SecurityMonitoringSuppressionCreateRequest,
)
from datadog_api_client.v2.model.security_monitoring_suppression_type import SecurityMonitoringSuppressionType

body = SecurityMonitoringSuppressionCreateRequest(
    data=SecurityMonitoringSuppressionCreateData(
        attributes=SecurityMonitoringSuppressionCreateAttributes(
            data_exclusion_query="source:cloudtrail account_id:12345",
            description="This rule suppresses low-severity signals in staging environments.",
            enabled=True,
            name="Custom suppression",
            rule_query="type:log_detection source:cloudtrail",
        ),
        type=SecurityMonitoringSuppressionType.SUPPRESSIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.validate_security_monitoring_suppression(body=body)
