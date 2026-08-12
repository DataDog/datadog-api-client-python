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
    from datadog_api_client.v2.model.notification_rule_target_configuration_recipient import (
        NotificationRuleTargetConfigurationRecipient,
    )


class NotificationRuleTargetConfiguration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_rule_target_configuration_recipient import (
            NotificationRuleTargetConfigurationRecipient,
        )

        return {
            "channel": (str,),
            "channel_id": (str,),
            "channel_name": (str,),
            "connector_name": (str,),
            "recipient": (NotificationRuleTargetConfigurationRecipient,),
            "service_name": (str,),
            "team_id": (str,),
            "team_name": (str,),
            "tenant_id": (str,),
            "tenant_name": (str,),
            "username": (str,),
            "webhook_name": (str,),
            "workspace": (str,),
            "workspace_id": (str,),
        }

    attribute_map = {
        "channel": "channel",
        "channel_id": "channel_id",
        "channel_name": "channel_name",
        "connector_name": "connector_name",
        "recipient": "recipient",
        "service_name": "service_name",
        "team_id": "team_id",
        "team_name": "team_name",
        "tenant_id": "tenant_id",
        "tenant_name": "tenant_name",
        "username": "username",
        "webhook_name": "webhook_name",
        "workspace": "workspace",
        "workspace_id": "workspace_id",
    }

    def __init__(
        self_,
        channel: Union[str, UnsetType] = unset,
        channel_id: Union[str, UnsetType] = unset,
        channel_name: Union[str, UnsetType] = unset,
        connector_name: Union[str, UnsetType] = unset,
        recipient: Union[NotificationRuleTargetConfigurationRecipient, UnsetType] = unset,
        service_name: Union[str, UnsetType] = unset,
        team_id: Union[str, UnsetType] = unset,
        team_name: Union[str, UnsetType] = unset,
        tenant_id: Union[str, UnsetType] = unset,
        tenant_name: Union[str, UnsetType] = unset,
        username: Union[str, UnsetType] = unset,
        webhook_name: Union[str, UnsetType] = unset,
        workspace: Union[str, UnsetType] = unset,
        workspace_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration for a notification target. Which fields apply depends on the target's ``type``.

        :param channel: Slack channel name, for a ``SLACK_CHANNEL`` target.
        :type channel: str, optional

        :param channel_id: Slack channel ID for a ``SLACK_CHANNEL`` target, or Microsoft Teams channel ID
            for an ``MS_TEAMS_CHANNEL`` target.
        :type channel_id: str, optional

        :param channel_name: Microsoft Teams channel name, for an ``MS_TEAMS_CHANNEL`` target.
        :type channel_name: str, optional

        :param connector_name: Microsoft Teams connector name, for an ``MS_TEAMS_CHANNEL`` target.
        :type connector_name: str, optional

        :param recipient: Recipient for an ``EMAIL`` target.
        :type recipient: NotificationRuleTargetConfigurationRecipient, optional

        :param service_name: PagerDuty service name, for a ``PAGERDUTY_SERVICE`` target.
        :type service_name: str, optional

        :param team_id: Microsoft Teams team ID, for an ``MS_TEAMS_CHANNEL`` target.
        :type team_id: str, optional

        :param team_name: Microsoft Teams team name, for an ``MS_TEAMS_CHANNEL`` target.
        :type team_name: str, optional

        :param tenant_id: Microsoft Teams tenant ID, for an ``MS_TEAMS_CHANNEL`` target.
        :type tenant_id: str, optional

        :param tenant_name: Microsoft Teams tenant name, for an ``MS_TEAMS_CHANNEL`` target.
        :type tenant_name: str, optional

        :param username: Slack username, for a ``SLACK_USER`` target.
        :type username: str, optional

        :param webhook_name: Name of the configured webhook, for a ``WEBHOOK`` target.
        :type webhook_name: str, optional

        :param workspace: Slack workspace name, for a ``SLACK_CHANNEL`` or ``SLACK_USER`` target.
        :type workspace: str, optional

        :param workspace_id: Slack workspace ID, for a ``SLACK_CHANNEL`` target.
        :type workspace_id: str, optional
        """
        if channel is not unset:
            kwargs["channel"] = channel
        if channel_id is not unset:
            kwargs["channel_id"] = channel_id
        if channel_name is not unset:
            kwargs["channel_name"] = channel_name
        if connector_name is not unset:
            kwargs["connector_name"] = connector_name
        if recipient is not unset:
            kwargs["recipient"] = recipient
        if service_name is not unset:
            kwargs["service_name"] = service_name
        if team_id is not unset:
            kwargs["team_id"] = team_id
        if team_name is not unset:
            kwargs["team_name"] = team_name
        if tenant_id is not unset:
            kwargs["tenant_id"] = tenant_id
        if tenant_name is not unset:
            kwargs["tenant_name"] = tenant_name
        if username is not unset:
            kwargs["username"] = username
        if webhook_name is not unset:
            kwargs["webhook_name"] = webhook_name
        if workspace is not unset:
            kwargs["workspace"] = workspace
        if workspace_id is not unset:
            kwargs["workspace_id"] = workspace_id
        super().__init__(kwargs)
