"""
Preview a rule query with applied filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_rule_detection_method import SecurityMonitoringRuleDetectionMethod
from datadog_api_client.v2.model.security_monitoring_rule_livetail_request import SecurityMonitoringRuleLivetailRequest
from datadog_api_client.v2.model.security_monitoring_rule_type_read import SecurityMonitoringRuleTypeRead

body = SecurityMonitoringRuleLivetailRequest(
    query="source:cloudtrail",
    query_index=0,
    filters=[],
    type=SecurityMonitoringRuleTypeRead.LOG_DETECTION,
    detection_method=SecurityMonitoringRuleDetectionMethod.THRESHOLD,
    data_source="logs",
    group_by_fields=[],
    distinct_fields=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.preview_security_monitoring_rule_query(body=body)

    print(response)
