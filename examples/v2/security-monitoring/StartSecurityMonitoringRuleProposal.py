"""
Start a rule proposal returns "Accepted" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_rule_proposal_input_type import (
    SecurityMonitoringRuleProposalInputType,
)
from datadog_api_client.v2.model.security_monitoring_rule_proposal_start_request import (
    SecurityMonitoringRuleProposalStartRequest,
)
from datadog_api_client.v2.model.security_monitoring_rule_proposal_start_request_attributes import (
    SecurityMonitoringRuleProposalStartRequestAttributes,
)
from datadog_api_client.v2.model.security_monitoring_rule_proposal_start_request_data import (
    SecurityMonitoringRuleProposalStartRequestData,
)
from datadog_api_client.v2.model.security_monitoring_rule_proposal_type import SecurityMonitoringRuleProposalType

body = SecurityMonitoringRuleProposalStartRequest(
    data=SecurityMonitoringRuleProposalStartRequestData(
        type=SecurityMonitoringRuleProposalType.RULE_PROPOSALS,
        attributes=SecurityMonitoringRuleProposalStartRequestAttributes(
            input_type=SecurityMonitoringRuleProposalInputType.NATURAL_LANGUAGE,
            input="Detect repeated failed Okta logins followed by a successful login from the same IP.",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["start_security_monitoring_rule_proposal"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.start_security_monitoring_rule_proposal(body=body)

    print(response)
