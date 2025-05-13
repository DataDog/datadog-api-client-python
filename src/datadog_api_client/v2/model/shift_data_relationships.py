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
    from datadog_api_client.v2.model.shift_data_relationships_user import ShiftDataRelationshipsUser


class ShiftDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.shift_data_relationships_user import ShiftDataRelationshipsUser

        return {
            "user": (ShiftDataRelationshipsUser,),
        }

    attribute_map = {
        "user": "user",
    }

    def __init__(self_, user: Union[ShiftDataRelationshipsUser, UnsetType] = unset, **kwargs):
        """
        The definition of ``ShiftDataRelationships`` object.

        :param user: Defines the relationship between a shift and the user who is working that shift.
        :type user: ShiftDataRelationshipsUser, optional
        """
        if user is not unset:
            kwargs["user"] = user
        super().__init__(kwargs)
