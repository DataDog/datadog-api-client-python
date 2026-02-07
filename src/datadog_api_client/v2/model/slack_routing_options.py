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


class SlackRoutingOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "channel_id": (str,),
            "channel_name": (str,),
            "workspace_id": (str,),
            "workspace_name": (str,),
        }

    attribute_map = {
        "channel_id": "channel_id",
        "channel_name": "channel_name",
        "workspace_id": "workspace_id",
        "workspace_name": "workspace_name",
    }

    def __init__(
        self_,
        channel_id: Union[str, UnsetType] = unset,
        channel_name: Union[str, UnsetType] = unset,
        workspace_id: Union[str, UnsetType] = unset,
        workspace_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Slack routing options for report delivery.

        :param channel_id: Slack channel ID.
        :type channel_id: str, optional

        :param channel_name: Slack channel name.
        :type channel_name: str, optional

        :param workspace_id: Slack workspace ID.
        :type workspace_id: str, optional

        :param workspace_name: Slack workspace name.
        :type workspace_name: str, optional
        """
        if channel_id is not unset:
            kwargs["channel_id"] = channel_id
        if channel_name is not unset:
            kwargs["channel_name"] = channel_name
        if workspace_id is not unset:
            kwargs["workspace_id"] = workspace_id
        if workspace_name is not unset:
            kwargs["workspace_name"] = workspace_name
        super().__init__(kwargs)
