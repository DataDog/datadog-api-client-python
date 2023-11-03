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


class OutcomesBatchRequestItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.state import State

        return {
            "remarks": (str,),
            "rule_id": (str,),
            "service_name": (str,),
            "state": (State,),
        }

    attribute_map = {
        "remarks": "remarks",
        "rule_id": "rule_id",
        "service_name": "service_name",
        "state": "state",
    }

    def __init__(
        self_, rule_id: str, service_name: str, state: State, remarks: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Scorecard outcome for a specific rule, for a given service within a batched update.

        :param remarks: Any remarks regarding the scorecard rule's evaluation, and supports HTML hyperlinks.
        :type remarks: str, optional

        :param rule_id: The unique ID for a scorecard rule.
        :type rule_id: str

        :param service_name: The unique name for a service in the catalog.
        :type service_name: str

        :param state: The state of the rule evaluation.
        :type state: State
        """
        if remarks is not unset:
            kwargs["remarks"] = remarks
        super().__init__(kwargs)

        self_.rule_id = rule_id
        self_.service_name = service_name
        self_.state = state
