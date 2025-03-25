# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.annotation import Annotation
    from datadog_api_client.v2.model.connection_env import ConnectionEnv
    from datadog_api_client.v2.model.input_schema import InputSchema
    from datadog_api_client.v2.model.output_schema import OutputSchema
    from datadog_api_client.v2.model.step import Step
    from datadog_api_client.v2.model.trigger import Trigger
    from datadog_api_client.v2.model.api_trigger_wrapper import APITriggerWrapper
    from datadog_api_client.v2.model.app_trigger_wrapper import AppTriggerWrapper
    from datadog_api_client.v2.model.case_trigger_wrapper import CaseTriggerWrapper
    from datadog_api_client.v2.model.change_event_trigger_wrapper import ChangeEventTriggerWrapper
    from datadog_api_client.v2.model.database_monitoring_trigger_wrapper import DatabaseMonitoringTriggerWrapper
    from datadog_api_client.v2.model.dashboard_trigger_wrapper import DashboardTriggerWrapper
    from datadog_api_client.v2.model.github_webhook_trigger_wrapper import GithubWebhookTriggerWrapper
    from datadog_api_client.v2.model.incident_trigger_wrapper import IncidentTriggerWrapper
    from datadog_api_client.v2.model.monitor_trigger_wrapper import MonitorTriggerWrapper
    from datadog_api_client.v2.model.notebook_trigger_wrapper import NotebookTriggerWrapper
    from datadog_api_client.v2.model.schedule_trigger_wrapper import ScheduleTriggerWrapper
    from datadog_api_client.v2.model.security_trigger_wrapper import SecurityTriggerWrapper
    from datadog_api_client.v2.model.self_service_trigger_wrapper import SelfServiceTriggerWrapper
    from datadog_api_client.v2.model.slack_trigger_wrapper import SlackTriggerWrapper
    from datadog_api_client.v2.model.software_catalog_trigger_wrapper import SoftwareCatalogTriggerWrapper
    from datadog_api_client.v2.model.workflow_trigger_wrapper import WorkflowTriggerWrapper


class Spec(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.annotation import Annotation
        from datadog_api_client.v2.model.connection_env import ConnectionEnv
        from datadog_api_client.v2.model.input_schema import InputSchema
        from datadog_api_client.v2.model.output_schema import OutputSchema
        from datadog_api_client.v2.model.step import Step
        from datadog_api_client.v2.model.trigger import Trigger

        return {
            "annotations": ([Annotation],),
            "connection_envs": ([ConnectionEnv],),
            "handle": (str,),
            "input_schema": (InputSchema,),
            "output_schema": (OutputSchema,),
            "steps": ([Step],),
            "triggers": ([Trigger],),
        }

    attribute_map = {
        "annotations": "annotations",
        "connection_envs": "connectionEnvs",
        "handle": "handle",
        "input_schema": "inputSchema",
        "output_schema": "outputSchema",
        "steps": "steps",
        "triggers": "triggers",
    }

    def __init__(
        self_,
        annotations: Union[List[Annotation], UnsetType] = unset,
        connection_envs: Union[List[ConnectionEnv], UnsetType] = unset,
        handle: Union[str, UnsetType] = unset,
        input_schema: Union[InputSchema, UnsetType] = unset,
        output_schema: Union[OutputSchema, UnsetType] = unset,
        steps: Union[List[Step], UnsetType] = unset,
        triggers: Union[
            List[
                Union[
                    Trigger,
                    APITriggerWrapper,
                    AppTriggerWrapper,
                    CaseTriggerWrapper,
                    ChangeEventTriggerWrapper,
                    DatabaseMonitoringTriggerWrapper,
                    DashboardTriggerWrapper,
                    GithubWebhookTriggerWrapper,
                    IncidentTriggerWrapper,
                    MonitorTriggerWrapper,
                    NotebookTriggerWrapper,
                    ScheduleTriggerWrapper,
                    SecurityTriggerWrapper,
                    SelfServiceTriggerWrapper,
                    SlackTriggerWrapper,
                    SoftwareCatalogTriggerWrapper,
                    WorkflowTriggerWrapper,
                ]
            ],
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        The spec defines what the workflow does.

        :param annotations: A list of annotations used in the workflow. These are like sticky notes for your workflow!
        :type annotations: [Annotation], optional

        :param connection_envs: A list of connections or connection groups used in the workflow.
        :type connection_envs: [ConnectionEnv], optional

        :param handle: Unique identifier used to trigger workflows automatically in Datadog.
        :type handle: str, optional

        :param input_schema: A list of input parameters for the workflow. These can be used as dynamic runtime values in your workflow.
        :type input_schema: InputSchema, optional

        :param output_schema: A list of output parameters for the workflow.
        :type output_schema: OutputSchema, optional

        :param steps: A ``Step`` is a sub-component of a workflow. Each ``Step`` performs an action.
        :type steps: [Step], optional

        :param triggers: The list of triggers that activate this workflow. At least one trigger is required, and each trigger type may appear at most once.
        :type triggers: [Trigger], optional
        """
        if annotations is not unset:
            kwargs["annotations"] = annotations
        if connection_envs is not unset:
            kwargs["connection_envs"] = connection_envs
        if handle is not unset:
            kwargs["handle"] = handle
        if input_schema is not unset:
            kwargs["input_schema"] = input_schema
        if output_schema is not unset:
            kwargs["output_schema"] = output_schema
        if steps is not unset:
            kwargs["steps"] = steps
        if triggers is not unset:
            kwargs["triggers"] = triggers
        super().__init__(kwargs)
