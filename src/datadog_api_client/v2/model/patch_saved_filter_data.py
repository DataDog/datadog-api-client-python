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
    from datadog_api_client.v2.model.patch_saved_filter_attributes import PatchSavedFilterAttributes
    from datadog_api_client.v2.model.saved_filter_data_type import SavedFilterDataType


class PatchSavedFilterData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_saved_filter_attributes import PatchSavedFilterAttributes
        from datadog_api_client.v2.model.saved_filter_data_type import SavedFilterDataType

        return {
            "attributes": (PatchSavedFilterAttributes,),
            "type": (SavedFilterDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: PatchSavedFilterAttributes, type: SavedFilterDataType, **kwargs):
        """
        The saved filter fields to update.

        :param attributes: Fields to update. At least one of ``name`` , ``description`` , or ``targeting_rules`` must have a non-null value. Omitted or null fields are preserved. The creation type cannot be changed.
        :type attributes: PatchSavedFilterAttributes

        :param type: The saved filter resource type.
        :type type: SavedFilterDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
