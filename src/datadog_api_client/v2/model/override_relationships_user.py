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
    from datadog_api_client.v2.model.override_relationships_user_data import OverrideRelationshipsUserData


class OverrideRelationshipsUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.override_relationships_user_data import OverrideRelationshipsUserData

        return {
            "data": (OverrideRelationshipsUserData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OverrideRelationshipsUserData, **kwargs):
        """
        Defines the relationship between an override and one of its associated users.

        :param data: A reference to a user, containing the user's ID and resource type.
        :type data: OverrideRelationshipsUserData
        """
        super().__init__(kwargs)

        self_.data = data
