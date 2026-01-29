# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.auto_close_inactive_cases import AutoCloseInactiveCases
    from datadog_api_client.v2.model.auto_transition_assigned_cases import AutoTransitionAssignedCases
    from datadog_api_client.v2.model.integration_incident import IntegrationIncident
    from datadog_api_client.v2.model.integration_jira import IntegrationJira
    from datadog_api_client.v2.model.integration_monitor import IntegrationMonitor
    from datadog_api_client.v2.model.integration_on_call import IntegrationOnCall
    from datadog_api_client.v2.model.integration_service_now import IntegrationServiceNow
    from datadog_api_client.v2.model.project_notification_settings import ProjectNotificationSettings


class ProjectSettings(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.auto_close_inactive_cases import AutoCloseInactiveCases
        from datadog_api_client.v2.model.auto_transition_assigned_cases import AutoTransitionAssignedCases
        from datadog_api_client.v2.model.integration_incident import IntegrationIncident
        from datadog_api_client.v2.model.integration_jira import IntegrationJira
        from datadog_api_client.v2.model.integration_monitor import IntegrationMonitor
        from datadog_api_client.v2.model.integration_on_call import IntegrationOnCall
        from datadog_api_client.v2.model.integration_service_now import IntegrationServiceNow
        from datadog_api_client.v2.model.project_notification_settings import ProjectNotificationSettings

        return {
            "auto_close_inactive_cases": (AutoCloseInactiveCases,),
            "auto_transition_assigned_cases": (AutoTransitionAssignedCases,),
            "integration_incident": (IntegrationIncident,),
            "integration_jira": (IntegrationJira,),
            "integration_monitor": (IntegrationMonitor,),
            "integration_on_call": (IntegrationOnCall,),
            "integration_service_now": (IntegrationServiceNow,),
            "notification": (ProjectNotificationSettings,),
        }

    attribute_map = {
        "auto_close_inactive_cases": "auto_close_inactive_cases",
        "auto_transition_assigned_cases": "auto_transition_assigned_cases",
        "integration_incident": "integration_incident",
        "integration_jira": "integration_jira",
        "integration_monitor": "integration_monitor",
        "integration_on_call": "integration_on_call",
        "integration_service_now": "integration_service_now",
        "notification": "notification",
    }

    def __init__(
        self_,
        auto_close_inactive_cases: Union[AutoCloseInactiveCases, UnsetType] = unset,
        auto_transition_assigned_cases: Union[AutoTransitionAssignedCases, UnsetType] = unset,
        integration_incident: Union[IntegrationIncident, UnsetType] = unset,
        integration_jira: Union[IntegrationJira, UnsetType] = unset,
        integration_monitor: Union[IntegrationMonitor, UnsetType] = unset,
        integration_on_call: Union[IntegrationOnCall, UnsetType] = unset,
        integration_service_now: Union[IntegrationServiceNow, UnsetType] = unset,
        notification: Union[ProjectNotificationSettings, UnsetType] = unset,
        **kwargs,
    ):
        """
        Project settings

        :param auto_close_inactive_cases: Auto-close inactive cases settings
        :type auto_close_inactive_cases: AutoCloseInactiveCases, optional

        :param auto_transition_assigned_cases: Auto-transition assigned cases settings
        :type auto_transition_assigned_cases: AutoTransitionAssignedCases, optional

        :param integration_incident: Incident integration settings
        :type integration_incident: IntegrationIncident, optional

        :param integration_jira: Jira integration settings
        :type integration_jira: IntegrationJira, optional

        :param integration_monitor: Monitor integration settings
        :type integration_monitor: IntegrationMonitor, optional

        :param integration_on_call: On-Call integration settings
        :type integration_on_call: IntegrationOnCall, optional

        :param integration_service_now: ServiceNow integration settings
        :type integration_service_now: IntegrationServiceNow, optional

        :param notification: Project notification settings
        :type notification: ProjectNotificationSettings, optional
        """
        if auto_close_inactive_cases is not unset:
            kwargs["auto_close_inactive_cases"] = auto_close_inactive_cases
        if auto_transition_assigned_cases is not unset:
            kwargs["auto_transition_assigned_cases"] = auto_transition_assigned_cases
        if integration_incident is not unset:
            kwargs["integration_incident"] = integration_incident
        if integration_jira is not unset:
            kwargs["integration_jira"] = integration_jira
        if integration_monitor is not unset:
            kwargs["integration_monitor"] = integration_monitor
        if integration_on_call is not unset:
            kwargs["integration_on_call"] = integration_on_call
        if integration_service_now is not unset:
            kwargs["integration_service_now"] = integration_service_now
        if notification is not unset:
            kwargs["notification"] = notification
        super().__init__(kwargs)
