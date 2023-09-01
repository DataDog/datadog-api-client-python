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
    name="Example-Security-Monitoring_cloud_updated",
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
                policy='package datadog\n\nimport data.datadog.output as dd_output\n\nimport future.keywords.contains\nimport future.keywords.if\nimport future.keywords.in\n\nmilliseconds_in_a_day := ((1000 * 60) * 60) * 24\n\neval(iam_service_account_key) = "skip" if {\n\tiam_service_account_key.disabled\n} else = "pass" if {\n\t(iam_service_account_key.resource_seen_at / milliseconds_in_a_day) - (iam_service_account_key.valid_after_time / milliseconds_in_a_day) <= 90\n} else = "fail"\n\n# This part remains unchanged for all rules\nresults contains result if {\n\tsome resource in input.resources[input.main_resource_type]\n\tresult := dd_output.format(resource, eval(resource))\n}\n',
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
