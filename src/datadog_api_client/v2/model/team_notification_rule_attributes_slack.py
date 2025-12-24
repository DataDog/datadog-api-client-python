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


class TeamNotificationRuleAttributesSlack(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "channel": (str,),
            "workspace": (str,),
        }

    attribute_map = {
        "channel": "channel",
        "workspace": "workspace",
    }

    def __init__(self_, channel: Union[str, UnsetType] = unset, workspace: Union[str, UnsetType] = unset, **kwargs):
        """
        Slack notification settings for the team

        :param channel: Channel for Slack notification
        :type channel: str, optional

        :param workspace: Workspace for Slack notification
        :type workspace: str, optional
        """
        if channel is not unset:
            kwargs["channel"] = channel
        if workspace is not unset:
            kwargs["workspace"] = workspace
        super().__init__(kwargs)
