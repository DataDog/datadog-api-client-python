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
    from datadog_api_client.v1.model.user_journey_search_target import UserJourneySearchTarget


class UserJourneySearchGraphFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.user_journey_search_target import UserJourneySearchTarget

        return {
            "name": (str,),
            "operator": (str,),
            "target": (UserJourneySearchTarget,),
            "value": (int,),
        }

    attribute_map = {
        "name": "name",
        "operator": "operator",
        "target": "target",
        "value": "value",
    }

    def __init__(
        self_,
        name: Union[str, UnsetType] = unset,
        operator: Union[str, UnsetType] = unset,
        target: Union[UserJourneySearchTarget, UnsetType] = unset,
        value: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Graph filter for user journey search.

        :param name: Filter name.
        :type name: str, optional

        :param operator: Filter operator.
        :type operator: str, optional

        :param target: Target for user journey search.
        :type target: UserJourneySearchTarget, optional

        :param value: Filter value.
        :type value: int, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if operator is not unset:
            kwargs["operator"] = operator
        if target is not unset:
            kwargs["target"] = target
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
