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
    from datadog_api_client.v2.model.escalation_relationships_responders import EscalationRelationshipsResponders


class EscalationRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_relationships_responders import EscalationRelationshipsResponders

        return {
            "responders": (EscalationRelationshipsResponders,),
        }

    attribute_map = {
        "responders": "responders",
    }

    def __init__(self_, responders: Union[EscalationRelationshipsResponders, UnsetType] = unset, **kwargs):
        """
        Contains the relationships of an escalation object, including its responders.

        :param responders: Lists the users involved in a specific step of the escalation policy.
        :type responders: EscalationRelationshipsResponders, optional
        """
        if responders is not unset:
            kwargs["responders"] = responders
        super().__init__(kwargs)
