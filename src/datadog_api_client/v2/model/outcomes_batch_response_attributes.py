# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.state import State


class OutcomesBatchResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.state import State

        return {
            "created_at": (datetime,),
            "modified_at": (datetime,),
            "remarks": (str,),
            "service_name": (str,),
            "state": (State,),
        }

    attribute_map = {
        "created_at": "created_at",
        "modified_at": "modified_at",
        "remarks": "remarks",
        "service_name": "service_name",
        "state": "state",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        remarks: Union[str, UnsetType] = unset,
        service_name: Union[str, UnsetType] = unset,
        state: Union[State, UnsetType] = unset,
        **kwargs,
    ):
        """
        The JSON:API attributes for an outcome.

        :param created_at: Creation time of the rule outcome.
        :type created_at: datetime, optional

        :param modified_at: Time of last rule outcome modification.
        :type modified_at: datetime, optional

        :param remarks: Any remarks regarding the scorecard rule's evaluation, and supports HTML hyperlinks.
        :type remarks: str, optional

        :param service_name: The unique name for a service in the catalog.
        :type service_name: str, optional

        :param state: The state of the rule evaluation.
        :type state: State, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if remarks is not unset:
            kwargs["remarks"] = remarks
        if service_name is not unset:
            kwargs["service_name"] = service_name
        if state is not unset:
            kwargs["state"] = state
        super().__init__(kwargs)
