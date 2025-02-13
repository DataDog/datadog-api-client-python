# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class Trigger(ModelComposed):
    def __init__(self, **kwargs):
        """
        One of the triggers that can start the execution of a workflow.

        :param api_trigger: Trigger a workflow VIA an API. The workflow must be published.
        :type api_trigger: APITrigger

        :param start_step_names: A list of steps that run first after a trigger fires.
        :type start_step_names: [str], optional

        :param app_trigger: Trigger a workflow VIA an App.
        :type app_trigger: dict

        :param case_trigger: Trigger a workflow VIA a Case. For automatic triggering a handle must be configured and the workflow must be published.
        :type case_trigger: CaseTrigger

        :param change_event_trigger: Trigger a workflow VIA a Change Event.
        :type change_event_trigger: dict

        :param dashboard_trigger: Trigger a workflow VIA a Dashboard.
        :type dashboard_trigger: dict

        :param github_webhook_trigger: Trigger a workflow VIA GitHub webhook. To trigger a workflow from GitHub, you must set a `webhookSecret`. In your GitHub Webhook Settings, set the Payload URL to "base_url"/api/v2/workflows/"workflow_id"/webhook?orgId="org_id", select application/json for the content type, and be highly recommend enabling SSL verification for security. The workflow must be published.
        :type github_webhook_trigger: GithubWebhookTrigger

        :param incident_trigger: Trigger a workflow VIA an Incident. For automatic triggering a handle must be configured and the workflow must be published.
        :type incident_trigger: IncidentTrigger

        :param monitor_trigger: Trigger a workflow VIA a Monitor. For automatic triggering a handle must be configured and the workflow must be published.
        :type monitor_trigger: MonitorTrigger

        :param schedule_trigger: Trigger a workflow VIA a Schedule. The workflow must be published.
        :type schedule_trigger: ScheduleTrigger

        :param security_trigger: Trigger a workflow VIA a Security Signal or Finding. For automatic triggering a handle must be configured and the workflow must be published.
        :type security_trigger: SecurityTrigger

        :param slack_trigger: Trigger a workflow VIA Slack. The workflow must be published.
        :type slack_trigger: dict

        :param workflow_trigger: Trigger a workflow VIA the Datadog UI. Only required if no other trigger exists.
        :type workflow_trigger: dict
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.api_trigger_wrapper import APITriggerWrapper
        from datadog_api_client.v2.model.app_trigger_wrapper import AppTriggerWrapper
        from datadog_api_client.v2.model.case_trigger_wrapper import CaseTriggerWrapper
        from datadog_api_client.v2.model.change_event_trigger_wrapper import ChangeEventTriggerWrapper
        from datadog_api_client.v2.model.dashboard_trigger_wrapper import DashboardTriggerWrapper
        from datadog_api_client.v2.model.github_webhook_trigger_wrapper import GithubWebhookTriggerWrapper
        from datadog_api_client.v2.model.incident_trigger_wrapper import IncidentTriggerWrapper
        from datadog_api_client.v2.model.monitor_trigger_wrapper import MonitorTriggerWrapper
        from datadog_api_client.v2.model.schedule_trigger_wrapper import ScheduleTriggerWrapper
        from datadog_api_client.v2.model.security_trigger_wrapper import SecurityTriggerWrapper
        from datadog_api_client.v2.model.slack_trigger_wrapper import SlackTriggerWrapper
        from datadog_api_client.v2.model.workflow_trigger_wrapper import WorkflowTriggerWrapper

        return {
            "oneOf": [
                APITriggerWrapper,
                AppTriggerWrapper,
                CaseTriggerWrapper,
                ChangeEventTriggerWrapper,
                DashboardTriggerWrapper,
                GithubWebhookTriggerWrapper,
                IncidentTriggerWrapper,
                MonitorTriggerWrapper,
                ScheduleTriggerWrapper,
                SecurityTriggerWrapper,
                SlackTriggerWrapper,
                WorkflowTriggerWrapper,
            ],
        }
