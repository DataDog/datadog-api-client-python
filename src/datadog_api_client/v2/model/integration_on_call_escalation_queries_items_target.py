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


class IntegrationOnCallEscalationQueriesItemsTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "dynamic_team_paging": (bool,),
            "team_id": (str,),
            "user_id": (str,),
        }

    attribute_map = {
        "dynamic_team_paging": "dynamic_team_paging",
        "team_id": "team_id",
        "user_id": "user_id",
    }

    def __init__(
        self_,
        dynamic_team_paging: Union[bool, UnsetType] = unset,
        team_id: Union[str, UnsetType] = unset,
        user_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param dynamic_team_paging:
        :type dynamic_team_paging: bool, optional

        :param team_id:
        :type team_id: str, optional

        :param user_id:
        :type user_id: str, optional
        """
        if dynamic_team_paging is not unset:
            kwargs["dynamic_team_paging"] = dynamic_team_paging
        if team_id is not unset:
            kwargs["team_id"] = team_id
        if user_id is not unset:
            kwargs["user_id"] = user_id
        super().__init__(kwargs)
