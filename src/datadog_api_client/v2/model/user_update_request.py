# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_update_data import UserUpdateData


@dataclass
class UserUpdateRequestJSON:
    id: str
    disabled: Union[bool, UnsetType] = unset
    email: Union[str, UnsetType] = unset
    name: Union[str, UnsetType] = unset


class UserUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_update_data import UserUpdateData

        return {
            "data": (UserUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = UserUpdateRequestJSON

    def __init__(self_, data: UserUpdateData, **kwargs):
        """
        Update a user.

        :param data: Object to update a user.
        :type data: UserUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
