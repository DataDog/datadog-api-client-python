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
    from datadog_api_client.v2.model.team_on_call_responders_data import TeamOnCallRespondersData
    from datadog_api_client.v2.model.team_on_call_responders_included import TeamOnCallRespondersIncluded
    from datadog_api_client.v2.model.user import User
    from datadog_api_client.v2.model.escalation import Escalation


class TeamOnCallResponders(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_on_call_responders_data import TeamOnCallRespondersData
        from datadog_api_client.v2.model.team_on_call_responders_included import TeamOnCallRespondersIncluded

        return {
            "data": (TeamOnCallRespondersData,),
            "included": ([TeamOnCallRespondersIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[TeamOnCallRespondersData, UnsetType] = unset,
        included: Union[List[Union[TeamOnCallRespondersIncluded, User, Escalation]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Root object representing a team's on-call responder configuration.

        :param data: Defines the main on-call responder object for a team, including relationships and metadata.
        :type data: TeamOnCallRespondersData, optional

        :param included: The ``TeamOnCallResponders`` ``included``.
        :type included: [TeamOnCallRespondersIncluded], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
