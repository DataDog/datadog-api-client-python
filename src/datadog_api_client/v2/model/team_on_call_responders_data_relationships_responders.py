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
    from datadog_api_client.v2.model.team_on_call_responders_data_relationships_responders_data_items import (
        TeamOnCallRespondersDataRelationshipsRespondersDataItems,
    )


class TeamOnCallRespondersDataRelationshipsResponders(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_on_call_responders_data_relationships_responders_data_items import (
            TeamOnCallRespondersDataRelationshipsRespondersDataItems,
        )

        return {
            "data": ([TeamOnCallRespondersDataRelationshipsRespondersDataItems],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(
        self_, data: Union[List[TeamOnCallRespondersDataRelationshipsRespondersDataItems], UnsetType] = unset, **kwargs
    ):
        """
        Defines the list of users assigned as on-call responders for the team.

        :param data: Array of user references associated as responders.
        :type data: [TeamOnCallRespondersDataRelationshipsRespondersDataItems], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
