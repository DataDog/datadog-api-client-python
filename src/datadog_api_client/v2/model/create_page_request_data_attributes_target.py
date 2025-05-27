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
    from datadog_api_client.v2.model.on_call_page_target_type import OnCallPageTargetType


class CreatePageRequestDataAttributesTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_target_type import OnCallPageTargetType

        return {
            "identifier": (str,),
            "type": (OnCallPageTargetType,),
        }

    attribute_map = {
        "identifier": "identifier",
        "type": "type",
    }

    def __init__(
        self_, identifier: Union[str, UnsetType] = unset, type: Union[OnCallPageTargetType, UnsetType] = unset, **kwargs
    ):
        """
        Information about the target to notify (such as a team or user).

        :param identifier: Identifier for the target (for example, team handle or user ID).
        :type identifier: str, optional

        :param type: The kind of target, ``team_id`` | ``team_handle`` | ``user_id``.
        :type type: OnCallPageTargetType, optional
        """
        if identifier is not unset:
            kwargs["identifier"] = identifier
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
