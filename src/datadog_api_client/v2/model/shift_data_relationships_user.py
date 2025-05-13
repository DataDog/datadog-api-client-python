# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.shift_data_relationships_user_data import ShiftDataRelationshipsUserData


class ShiftDataRelationshipsUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.shift_data_relationships_user_data import ShiftDataRelationshipsUserData

        return {
            "data": (ShiftDataRelationshipsUserData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ShiftDataRelationshipsUserData, **kwargs):
        """
        Defines the relationship between a shift and the user who is working that shift.

        :param data: Represents a reference to the user assigned to this shift, containing the user's ID and resource type.
        :type data: ShiftDataRelationshipsUserData
        """
        super().__init__(kwargs)

        self_.data = data
