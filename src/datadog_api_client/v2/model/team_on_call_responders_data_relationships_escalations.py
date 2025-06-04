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
    from datadog_api_client.v2.model.team_on_call_responders_data_relationships_escalations_data_items import (
        TeamOnCallRespondersDataRelationshipsEscalationsDataItems,
    )


class TeamOnCallRespondersDataRelationshipsEscalations(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_on_call_responders_data_relationships_escalations_data_items import (
            TeamOnCallRespondersDataRelationshipsEscalationsDataItems,
        )

        return {
            "data": ([TeamOnCallRespondersDataRelationshipsEscalationsDataItems],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(
        self_, data: Union[List[TeamOnCallRespondersDataRelationshipsEscalationsDataItems], UnsetType] = unset, **kwargs
    ):
        """
        Defines the escalation policy steps linked to the team's on-call configuration.

        :param data: Array of escalation step references.
        :type data: [TeamOnCallRespondersDataRelationshipsEscalationsDataItems], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
