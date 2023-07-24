"""
Create a cloud_configuration rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.cloud_configuration_compliance_rule_options import (
    CloudConfigurationComplianceRuleOptions,
)
from datadog_api_client.v2.model.cloud_configuration_rego_rule import CloudConfigurationRegoRule
from datadog_api_client.v2.model.cloud_configuration_rule_case_create import CloudConfigurationRuleCaseCreate
from datadog_api_client.v2.model.cloud_configuration_rule_compliance_signal_options import (
    CloudConfigurationRuleComplianceSignalOptions,
)
from datadog_api_client.v2.model.cloud_configuration_rule_create_payload import CloudConfigurationRuleCreatePayload
from datadog_api_client.v2.model.cloud_configuration_rule_options import CloudConfigurationRuleOptions
from datadog_api_client.v2.model.cloud_configuration_rule_type import CloudConfigurationRuleType
from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
from datadog_api_client.v2.model.security_monitoring_filter_action import SecurityMonitoringFilterAction
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity

body = CloudConfigurationRuleCreatePayload(
    type=CloudConfigurationRuleType.CLOUD_CONFIGURATION,
    name="Example-Security-Monitoring_cloud",
    is_enabled=False,
    cases=[
        CloudConfigurationRuleCaseCreate(
            status=SecurityMonitoringRuleSeverity.INFO,
            notifications=[
                "channel",
            ],
        ),
    ],
    options=CloudConfigurationRuleOptions(
        compliance_rule_options=CloudConfigurationComplianceRuleOptions(
            resource_type="gcp_compute_disk",
            complex_rule=False,
            rego_rule=CloudConfigurationRegoRule(
                policy="package datadog\n",
                resource_types=[
                    "gcp_compute_disk",
                ],
            ),
        ),
    ),
    message="ddd",
    tags=[
        "my:tag",
    ],
    compliance_signal_options=CloudConfigurationRuleComplianceSignalOptions(
        user_activation_status=True,
        user_group_by_fields=[
            "@account_id",
        ],
    ),
    filters=[
        SecurityMonitoringFilter(
            action=SecurityMonitoringFilterAction.REQUIRE,
            query="resource_id:helo*",
        ),
        SecurityMonitoringFilter(
            action=SecurityMonitoringFilterAction.SUPPRESS,
            query="control:helo*",
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_rule(body=body)

    print(response)
