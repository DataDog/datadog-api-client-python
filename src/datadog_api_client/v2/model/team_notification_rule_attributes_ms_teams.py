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


class TeamNotificationRuleAttributesMsTeams(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "connector_name": (str,),
        }

    attribute_map = {
        "connector_name": "connector_name",
    }

    def __init__(self_, connector_name: Union[str, UnsetType] = unset, **kwargs):
        """
        MS Teams notification settings for the team

        :param connector_name: Handle for MS Teams
        :type connector_name: str, optional
        """
        if connector_name is not unset:
            kwargs["connector_name"] = connector_name
        super().__init__(kwargs)
