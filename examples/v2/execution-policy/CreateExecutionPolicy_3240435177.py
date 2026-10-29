"""
Create a Slack execution policy with scope and targets returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.execution_policy_api import ExecutionPolicyApi
from datadog_api_client.v2.model.execution_policy_action_pattern import ExecutionPolicyActionPattern
from datadog_api_client.v2.model.execution_policy_create_request import ExecutionPolicyCreateRequest
from datadog_api_client.v2.model.execution_policy_create_request_data import ExecutionPolicyCreateRequestData
from datadog_api_client.v2.model.execution_policy_effect import ExecutionPolicyEffect
from datadog_api_client.v2.model.execution_policy_integration import ExecutionPolicyIntegration
from datadog_api_client.v2.model.execution_policy_scope import ExecutionPolicyScope
from datadog_api_client.v2.model.execution_policy_slack_scope import ExecutionPolicySlackScope
from datadog_api_client.v2.model.execution_policy_slack_scope_rule import ExecutionPolicySlackScopeRule
from datadog_api_client.v2.model.execution_policy_target import ExecutionPolicyTarget
from datadog_api_client.v2.model.execution_policy_type import ExecutionPolicyType
from datadog_api_client.v2.model.execution_policy_write_attributes import ExecutionPolicyWriteAttributes

body = ExecutionPolicyCreateRequest(
    data=ExecutionPolicyCreateRequestData(
        type=ExecutionPolicyType.EXECUTION_POLICY,
        attributes=ExecutionPolicyWriteAttributes(
            name="Cassette Execution Policy exampleexecutionpolicy",
            effect=ExecutionPolicyEffect.ALLOW,
            action_pattern=ExecutionPolicyActionPattern(
                integration=ExecutionPolicyIntegration.INTEGRATION_SLACK,
                action_fqns=[
                    "com.datadoghq.slack.*",
                ],
            ),
            scope=ExecutionPolicyScope(
                slack=ExecutionPolicySlackScope(
                    rules=[
                        ExecutionPolicySlackScopeRule(
                            channel_name_selectors=[
                                "incident-*",
                            ],
                        ),
                    ],
                ),
            ),
            targets=[
                ExecutionPolicyTarget(
                    name="Incident workspace",
                    agent_tags=[
                        "slack_workspace_id:T01234567",
                    ],
                ),
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_execution_policy"] = True
with ApiClient(configuration) as api_client:
    api_instance = ExecutionPolicyApi(api_client)
    response = api_instance.create_execution_policy(body=body)

    print(response)
