"""
Bulk delete security monitoring rules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_attributes import (
    SecurityMonitoringRuleBulkDeleteAttributes,
)
from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_data import SecurityMonitoringRuleBulkDeleteData
from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_payload import (
    SecurityMonitoringRuleBulkDeletePayload,
)
from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_request_data_type import (
    SecurityMonitoringRuleBulkDeleteRequestDataType,
)

body = SecurityMonitoringRuleBulkDeletePayload(
    data=SecurityMonitoringRuleBulkDeleteData(
        attributes=SecurityMonitoringRuleBulkDeleteAttributes(
            rule_ids=[
                "abc-000-u7q",
                "abc-000-7dd",
            ],
        ),
        type=SecurityMonitoringRuleBulkDeleteRequestDataType.BULK_DELETE_RULES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.bulk_delete_security_monitoring_rules(body=body)

    print(response)
