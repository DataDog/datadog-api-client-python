"""
Bulk export security monitoring rules returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_rule_bulk_export_attributes import (
    SecurityMonitoringRuleBulkExportAttributes,
)
from datadog_api_client.v2.model.security_monitoring_rule_bulk_export_data import SecurityMonitoringRuleBulkExportData
from datadog_api_client.v2.model.security_monitoring_rule_bulk_export_data_type import (
    SecurityMonitoringRuleBulkExportDataType,
)
from datadog_api_client.v2.model.security_monitoring_rule_bulk_export_payload import (
    SecurityMonitoringRuleBulkExportPayload,
)

# there is a valid "security_rule" in the system
SECURITY_RULE_ID = environ["SECURITY_RULE_ID"]

body = SecurityMonitoringRuleBulkExportPayload(
    data=SecurityMonitoringRuleBulkExportData(
        attributes=SecurityMonitoringRuleBulkExportAttributes(
            rule_ids=[
                SECURITY_RULE_ID,
            ],
        ),
        type=SecurityMonitoringRuleBulkExportDataType.SECURITY_MONITORING_RULES_BULK_EXPORT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.bulk_export_security_monitoring_rules(body=body)

    print(response.read())
