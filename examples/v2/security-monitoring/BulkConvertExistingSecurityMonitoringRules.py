"""
Bulk convert rules to Terraform returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_rule_convert_bulk_attributes import (
    SecurityMonitoringRuleConvertBulkAttributes,
)
from datadog_api_client.v2.model.security_monitoring_rule_convert_bulk_data import SecurityMonitoringRuleConvertBulkData
from datadog_api_client.v2.model.security_monitoring_rule_convert_bulk_data_type import (
    SecurityMonitoringRuleConvertBulkDataType,
)
from datadog_api_client.v2.model.security_monitoring_rule_convert_bulk_payload import (
    SecurityMonitoringRuleConvertBulkPayload,
)

body = SecurityMonitoringRuleConvertBulkPayload(
    data=SecurityMonitoringRuleConvertBulkData(
        attributes=SecurityMonitoringRuleConvertBulkAttributes(
            rule_ids=[
                "def-000-u7q",
                "def-000-7dd",
            ],
        ),
        id="convert_bulk",
        type=SecurityMonitoringRuleConvertBulkDataType.SECURITY_MONITORING_RULES_CONVERT_BULK,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.bulk_convert_existing_security_monitoring_rules(body=body)

    print(response.read())
