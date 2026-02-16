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
    from datadog_api_client.v2.model.client_type import ClientType
    from datadog_api_client.v2.model.stability_level import StabilityLevel


class PickActionRequest(ModelNormal):
    validations = {
        "number_of_relevant_actions": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.client_type import ClientType
        from datadog_api_client.v2.model.stability_level import StabilityLevel

        return {
            "client": (ClientType,),
            "number_of_relevant_actions": (int,),
            "stability": (StabilityLevel,),
            "user_prompt": (str,),
        }

    attribute_map = {
        "client": "client",
        "number_of_relevant_actions": "number_of_relevant_actions",
        "stability": "stability",
        "user_prompt": "user_prompt",
    }

    def __init__(
        self_,
        number_of_relevant_actions: int,
        user_prompt: str,
        client: Union[ClientType, UnsetType] = unset,
        stability: Union[StabilityLevel, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param client: The client type for action filtering.
        :type client: ClientType, optional

        :param number_of_relevant_actions: The number of relevant actions to return.
        :type number_of_relevant_actions: int

        :param stability: The stability level for action filtering.
        :type stability: StabilityLevel, optional

        :param user_prompt: The user's prompt to find relevant actions.
        :type user_prompt: str
        """
        if client is not unset:
            kwargs["client"] = client
        if stability is not unset:
            kwargs["stability"] = stability
        super().__init__(kwargs)

        self_.number_of_relevant_actions = number_of_relevant_actions
        self_.user_prompt = user_prompt
