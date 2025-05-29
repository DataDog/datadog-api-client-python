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
    from datadog_api_client.v2.model.team_on_call_responders_data_relationships_escalations import (
        TeamOnCallRespondersDataRelationshipsEscalations,
    )
    from datadog_api_client.v2.model.team_on_call_responders_data_relationships_responders import (
        TeamOnCallRespondersDataRelationshipsResponders,
    )


class TeamOnCallRespondersDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_on_call_responders_data_relationships_escalations import (
            TeamOnCallRespondersDataRelationshipsEscalations,
        )
        from datadog_api_client.v2.model.team_on_call_responders_data_relationships_responders import (
            TeamOnCallRespondersDataRelationshipsResponders,
        )

        return {
            "escalations": (TeamOnCallRespondersDataRelationshipsEscalations,),
            "responders": (TeamOnCallRespondersDataRelationshipsResponders,),
        }

    attribute_map = {
        "escalations": "escalations",
        "responders": "responders",
    }

    def __init__(
        self_,
        escalations: Union[TeamOnCallRespondersDataRelationshipsEscalations, UnsetType] = unset,
        responders: Union[TeamOnCallRespondersDataRelationshipsResponders, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``TeamOnCallRespondersDataRelationships`` object.

        :param escalations: The definition of ``TeamOnCallRespondersDataRelationshipsEscalations`` object.
        :type escalations: TeamOnCallRespondersDataRelationshipsEscalations, optional

        :param responders: The definition of ``TeamOnCallRespondersDataRelationshipsResponders`` object.
        :type responders: TeamOnCallRespondersDataRelationshipsResponders, optional
        """
        if escalations is not unset:
            kwargs["escalations"] = escalations
        if responders is not unset:
            kwargs["responders"] = responders
        super().__init__(kwargs)
