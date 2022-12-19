"""
Update a cloud configuration rule's details returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.cloud_configuration_compliance_rule_options import (
    CloudConfigurationComplianceRuleOptions,
)
from datadog_api_client.v2.model.cloud_configuration_rego_rule import CloudConfigurationRegoRule
from datadog_api_client.v2.model.cloud_configuration_rule_compliance_signal_options import (
    CloudConfigurationRuleComplianceSignalOptions,
)
from datadog_api_client.v2.model.security_monitoring_rule_case import SecurityMonitoringRuleCase
from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity
from datadog_api_client.v2.model.security_monitoring_rule_update_payload import SecurityMonitoringRuleUpdatePayload

# there is a valid "cloud_configuration_rule" in the system
CLOUD_CONFIGURATION_RULE_ID = environ["CLOUD_CONFIGURATION_RULE_ID"]

body = SecurityMonitoringRuleUpdatePayload(
    name="Example-Update_a_cloud_configuration_rule_s_details_returns_OK_response_cloud_updated",
    is_enabled=False,
    cases=[
        SecurityMonitoringRuleCase(
            status=SecurityMonitoringRuleSeverity.INFO,
            notifications=[],
        ),
    ],
    options=SecurityMonitoringRuleOptions(
        compliance_rule_options=CloudConfigurationComplianceRuleOptions(
            resource_type="gcp_compute_disk",
            rego_rule=CloudConfigurationRegoRule(
                policy="package datadog\n",
                resource_types=[
                    "gcp_compute_disk",
                ],
            ),
        ),
    ),
    message="ddd",
    tags=[],
    compliance_signal_options=CloudConfigurationRuleComplianceSignalOptions(
        user_activation_status=False,
        user_group_by_fields=[],
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_security_monitoring_rule(rule_id=CLOUD_CONFIGURATION_RULE_ID, body=body)

    print(response)
