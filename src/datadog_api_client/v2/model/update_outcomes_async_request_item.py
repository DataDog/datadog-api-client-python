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
    from datadog_api_client.v2.model.state import State


class UpdateOutcomesAsyncRequestItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.state import State

        return {
            "entity_reference": (str,),
            "remarks": (str,),
            "rule_id": (str,),
            "state": (State,),
        }

    attribute_map = {
        "entity_reference": "entity_reference",
        "remarks": "remarks",
        "rule_id": "rule_id",
        "state": "state",
    }

    def __init__(
        self_, entity_reference: str, rule_id: str, state: State, remarks: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Scorecard outcome for a single entity and rule.

        :param entity_reference: The unique reference for an IDP entity.
        :type entity_reference: str

        :param remarks: Any remarks regarding the scorecard rule's evaluation. Supports HTML hyperlinks.
        :type remarks: str, optional

        :param rule_id: The unique ID for a scorecard rule.
        :type rule_id: str

        :param state: The state of the rule evaluation.
        :type state: State
        """
        if remarks is not unset:
            kwargs["remarks"] = remarks
        super().__init__(kwargs)

        self_.entity_reference = entity_reference
        self_.rule_id = rule_id
        self_.state = state
