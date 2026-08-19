"""
Create an execution policy with scope and targets returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.execution_policy_api import ExecutionPolicyApi
from datadog_api_client.v2.model.execution_policy_action_pattern import ExecutionPolicyActionPattern
from datadog_api_client.v2.model.execution_policy_create_request import ExecutionPolicyCreateRequest
from datadog_api_client.v2.model.execution_policy_create_request_data import ExecutionPolicyCreateRequestData
from datadog_api_client.v2.model.execution_policy_effect import ExecutionPolicyEffect
from datadog_api_client.v2.model.execution_policy_integration import ExecutionPolicyIntegration
from datadog_api_client.v2.model.execution_policy_scope import ExecutionPolicyScope
from datadog_api_client.v2.model.execution_policy_script_scope import ExecutionPolicyScriptScope
from datadog_api_client.v2.model.execution_policy_script_scope_rule import ExecutionPolicyScriptScopeRule
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
                integration=ExecutionPolicyIntegration.INTEGRATION_SCRIPT,
                action_fqns=[
                    "com.datadoghq.script.*",
                ],
            ),
            scope=ExecutionPolicyScope(
                scripts=ExecutionPolicyScriptScope(
                    rules=[
                        ExecutionPolicyScriptScopeRule(
                            target_script_names=[
                                "restart_service.sh",
                            ],
                        ),
                    ],
                ),
            ),
            targets=[
                ExecutionPolicyTarget(
                    name="Production hosts",
                    agent_tags=[
                        "env:prod",
                    ],
                ),
            ],
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_execution_policy"] = True
with ApiClient(configuration) as api_client:
    api_instance = ExecutionPolicyApi(api_client)
    response = api_instance.create_execution_policy(body=body)

    print(response)
