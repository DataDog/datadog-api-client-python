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
    from datadog_api_client.v2.model.team_notification_rule_attributes import TeamNotificationRuleAttributes


class TeamNotificationRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_notification_rule_attributes import TeamNotificationRuleAttributes

        return {
            "attributes": (TeamNotificationRuleAttributes,),
            "id": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
    }

    def __init__(
        self_,
        attributes: Union[TeamNotificationRuleAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Team notification rule

        :param attributes: Team notification rule attributes
        :type attributes: TeamNotificationRuleAttributes, optional

        :param id: The identifier of the team notification rule
        :type id: str, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)
