# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.saved_filter_attributes import SavedFilterAttributes
    from datadog_api_client.v2.model.saved_filter_data_type import SavedFilterDataType


class SavedFilterData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saved_filter_attributes import SavedFilterAttributes
        from datadog_api_client.v2.model.saved_filter_data_type import SavedFilterDataType

        return {
            "attributes": (SavedFilterAttributes,),
            "id": (UUID,),
            "type": (SavedFilterDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: SavedFilterAttributes, id: UUID, type: SavedFilterDataType, **kwargs):
        """
        A saved filter resource.

        :param attributes: Saved filter details, including the full targeting rules and conditions.
        :type attributes: SavedFilterAttributes

        :param id: The ID of the saved filter.
        :type id: UUID

        :param type: The saved filter resource type.
        :type type: SavedFilterDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
