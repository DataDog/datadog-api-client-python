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
    from datadog_api_client.v2.model.saved_filter_permission_denied_data import SavedFilterPermissionDeniedData


class SavedFilterPermissionDeniedResponse(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saved_filter_permission_denied_data import SavedFilterPermissionDeniedData

        return {
            "data": (SavedFilterPermissionDeniedData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SavedFilterPermissionDeniedData, **kwargs):
        """
        The caller lacks edit permission on one or more feature flags that reference this saved filter.

        :param data: The caller lacks edit permission on one or more feature flags that reference this saved filter.
        :type data: SavedFilterPermissionDeniedData
        """
        super().__init__(kwargs)

        self_.data = data
