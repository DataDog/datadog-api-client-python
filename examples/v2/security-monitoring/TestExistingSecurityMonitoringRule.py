"""
Test an existing rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_rule_query_payload import SecurityMonitoringRuleQueryPayload
from datadog_api_client.v2.model.security_monitoring_rule_query_payload_data import (
    SecurityMonitoringRuleQueryPayloadData,
)
from datadog_api_client.v2.model.security_monitoring_rule_test_request import SecurityMonitoringRuleTestRequest

body = SecurityMonitoringRuleTestRequest(
    rule_query_payloads=[
        SecurityMonitoringRuleQueryPayload(
            expected_result=True,
            index=0,
            payload=SecurityMonitoringRuleQueryPayloadData(
                ddsource="nginx",
                ddtags="env:staging,version:5.1",
                hostname="i-012345678",
                message="2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
                service="payment",
            ),
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.test_existing_security_monitoring_rule(rule_id="rule_id", body=body)

    print(response)
