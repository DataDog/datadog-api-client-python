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
    from datadog_api_client.v2.model.saved_filter_permission_denied_attributes import (
        SavedFilterPermissionDeniedAttributes,
    )
    from datadog_api_client.v2.model.saved_filter_permission_denied_type import SavedFilterPermissionDeniedType


class SavedFilterPermissionDeniedData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saved_filter_permission_denied_attributes import (
            SavedFilterPermissionDeniedAttributes,
        )
        from datadog_api_client.v2.model.saved_filter_permission_denied_type import SavedFilterPermissionDeniedType

        return {
            "attributes": (SavedFilterPermissionDeniedAttributes,),
            "id": (UUID,),
            "type": (SavedFilterPermissionDeniedType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SavedFilterPermissionDeniedAttributes,
        id: UUID,
        type: SavedFilterPermissionDeniedType,
        **kwargs,
    ):
        """
        The caller lacks edit permission on one or more feature flags that reference this saved filter.

        :param attributes: The caller lacks edit permission on one or more feature flags that reference this saved filter.
        :type attributes: SavedFilterPermissionDeniedAttributes

        :param id: The ID of the saved filter.
        :type id: UUID

        :param type: The resource type for this saved filter update error.
        :type type: SavedFilterPermissionDeniedType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
