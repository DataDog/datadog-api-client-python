"""
Update an existing Workflow returns "Successfully updated a workflow." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi
from datadog_api_client.v2.model.connection import Connection
from datadog_api_client.v2.model.connection_env import ConnectionEnv
from datadog_api_client.v2.model.connection_env_env import ConnectionEnvEnv
from datadog_api_client.v2.model.github_webhook_trigger import GithubWebhookTrigger
from datadog_api_client.v2.model.github_webhook_trigger_wrapper import GithubWebhookTriggerWrapper
from datadog_api_client.v2.model.input_schema import InputSchema
from datadog_api_client.v2.model.input_schema_parameters import InputSchemaParameters
from datadog_api_client.v2.model.input_schema_parameters_type import InputSchemaParametersType
from datadog_api_client.v2.model.monitor_trigger import MonitorTrigger
from datadog_api_client.v2.model.monitor_trigger_wrapper import MonitorTriggerWrapper
from datadog_api_client.v2.model.outbound_edge import OutboundEdge
from datadog_api_client.v2.model.output_schema import OutputSchema
from datadog_api_client.v2.model.output_schema_parameters import OutputSchemaParameters
from datadog_api_client.v2.model.output_schema_parameters_type import OutputSchemaParametersType
from datadog_api_client.v2.model.parameter import Parameter
from datadog_api_client.v2.model.spec import Spec
from datadog_api_client.v2.model.step import Step
from datadog_api_client.v2.model.trigger_rate_limit import TriggerRateLimit
from datadog_api_client.v2.model.update_workflow_request import UpdateWorkflowRequest
from datadog_api_client.v2.model.workflow_data_type import WorkflowDataType
from datadog_api_client.v2.model.workflow_data_update import WorkflowDataUpdate
from datadog_api_client.v2.model.workflow_data_update_attributes import WorkflowDataUpdateAttributes

# there is a valid "workflow" in the system
WORKFLOW_DATA_ID = environ["WORKFLOW_DATA_ID"]

body = UpdateWorkflowRequest(
    data=WorkflowDataUpdate(
        attributes=WorkflowDataUpdateAttributes(
            description="A sample workflow.",
            name="Example Workflow",
            published=True,
            spec=Spec(
                connection_envs=[
                    ConnectionEnv(
                        connections=[
                            Connection(
                                connection_id="11111111-1111-1111-1111-111111111111",
                                label="INTEGRATION_DATADOG",
                            ),
                        ],
                        env=ConnectionEnvEnv.DEFAULT,
                    ),
                ],
                input_schema=InputSchema(
                    parameters=[
                        InputSchemaParameters(
                            default_value="default",
                            name="input",
                            type=InputSchemaParametersType.STRING,
                        ),
                    ],
                ),
                output_schema=OutputSchema(
                    parameters=[
                        OutputSchemaParameters(
                            name="output",
                            type=OutputSchemaParametersType.ARRAY_OBJECT,
                            value="outputValue",
                        ),
                    ],
                ),
                steps=[
                    Step(
                        action_id="com.datadoghq.dd.monitor.listMonitors",
                        connection_label="INTEGRATION_DATADOG",
                        name="Step1",
                        outbound_edges=[
                            OutboundEdge(
                                branch_name="main",
                                next_step_name="Step2",
                            ),
                        ],
                        parameters=[
                            Parameter(
                                name="tags",
                                value="service:monitoring",
                            ),
                        ],
                    ),
                    Step(
                        action_id="com.datadoghq.core.noop",
                        name="Step2",
                    ),
                ],
                triggers=[
                    MonitorTriggerWrapper(
                        monitor_trigger=MonitorTrigger(
                            rate_limit=TriggerRateLimit(
                                count=1,
                                interval="3600s",
                            ),
                        ),
                        start_step_names=[
                            "Step1",
                        ],
                    ),
                    GithubWebhookTriggerWrapper(
                        start_step_names=[
                            "Step1",
                        ],
                        github_webhook_trigger=GithubWebhookTrigger(),
                    ),
                ],
            ),
            tags=[
                "team:infra",
                "service:monitoring",
                "foo:bar",
            ],
        ),
        id="22222222-2222-2222-2222-222222222222",
        type=WorkflowDataType.WORKFLOWS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.update_workflow(workflow_id=WORKFLOW_DATA_ID, body=body)

    print(response)
