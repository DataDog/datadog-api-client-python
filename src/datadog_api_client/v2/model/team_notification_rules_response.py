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
    from datadog_api_client.v2.model.team_notification_rule import TeamNotificationRule
    from datadog_api_client.v2.model.team_notification_rules_response_meta import TeamNotificationRulesResponseMeta


class TeamNotificationRulesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_notification_rule import TeamNotificationRule
        from datadog_api_client.v2.model.team_notification_rules_response_meta import TeamNotificationRulesResponseMeta

        return {
            "data": ([TeamNotificationRule],),
            "meta": (TeamNotificationRulesResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[TeamNotificationRule], UnsetType] = unset,
        meta: Union[TeamNotificationRulesResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Team notification rules response

        :param data: Team notification rules response data
        :type data: [TeamNotificationRule], optional

        :param meta: Metadata that is included in the response when querying the team notification rules
        :type meta: TeamNotificationRulesResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
