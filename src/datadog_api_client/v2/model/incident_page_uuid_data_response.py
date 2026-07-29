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
    from datadog_api_client.v2.model.incident_page_uuid_type import IncidentPageUUIDType


class IncidentPageUUIDDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_page_uuid_type import IncidentPageUUIDType

        return {
            "id": (UUID,),
            "type": (IncidentPageUUIDType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: UUID, type: IncidentPageUUIDType, **kwargs):
        """
        Page UUID data in a response.

        :param id: The UUID of the created page.
        :type id: UUID

        :param type: Resource type for a page UUID response.
        :type type: IncidentPageUUIDType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
