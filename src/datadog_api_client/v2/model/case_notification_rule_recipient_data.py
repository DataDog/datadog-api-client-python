# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CaseNotificationRuleRecipientData(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "channel": (str,),
            "channel_id": (str,),
            "channel_name": (str,),
            "connector_name": (str,),
            "email": (str,),
            "name": (str,),
            "service_name": (str,),
            "team_id": (str,),
            "team_name": (str,),
            "tenant_id": (str,),
            "tenant_name": (str,),
            "workspace": (str,),
            "workspace_id": (str,),
        }

    attribute_map = {
        "channel": "channel",
        "channel_id": "channel_id",
        "channel_name": "channel_name",
        "connector_name": "connector_name",
        "email": "email",
        "name": "name",
        "service_name": "service_name",
        "team_id": "team_id",
        "team_name": "team_name",
        "tenant_id": "tenant_id",
        "tenant_name": "tenant_name",
        "workspace": "workspace",
        "workspace_id": "workspace_id",
    }

    def __init__(
        self_,
        channel: Union[str, UnsetType] = unset,
        channel_id: Union[str, UnsetType] = unset,
        channel_name: Union[str, UnsetType] = unset,
        connector_name: Union[str, UnsetType] = unset,
        email: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        service_name: Union[str, UnsetType] = unset,
        team_id: Union[str, UnsetType] = unset,
        team_name: Union[str, UnsetType] = unset,
        tenant_id: Union[str, UnsetType] = unset,
        tenant_name: Union[str, UnsetType] = unset,
        workspace: Union[str, UnsetType] = unset,
        workspace_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Recipient data

        :param channel: Slack channel name
        :type channel: str, optional

        :param channel_id: Slack channel ID
        :type channel_id: str, optional

        :param channel_name: Microsoft Teams channel name
        :type channel_name: str, optional

        :param connector_name: Microsoft Teams connector name
        :type connector_name: str, optional

        :param email: Email address
        :type email: str, optional

        :param name: HTTP webhook name
        :type name: str, optional

        :param service_name: PagerDuty service name
        :type service_name: str, optional

        :param team_id: Microsoft Teams team ID
        :type team_id: str, optional

        :param team_name: Microsoft Teams team name
        :type team_name: str, optional

        :param tenant_id: Microsoft Teams tenant ID
        :type tenant_id: str, optional

        :param tenant_name: Microsoft Teams tenant name
        :type tenant_name: str, optional

        :param workspace: Slack workspace name
        :type workspace: str, optional

        :param workspace_id: Slack workspace ID
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
        if email is not unset:
            kwargs["email"] = email
        if name is not unset:
            kwargs["name"] = name
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
        if workspace is not unset:
            kwargs["workspace"] = workspace
        if workspace_id is not unset:
            kwargs["workspace_id"] = workspace_id
        super().__init__(kwargs)
