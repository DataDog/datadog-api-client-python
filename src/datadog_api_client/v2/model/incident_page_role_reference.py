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
    from datadog_api_client.v2.model.incident_page_role_type import IncidentPageRoleType


class IncidentPageRoleReference(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_page_role_type import IncidentPageRoleType

        return {
            "id": (UUID,),
            "type": (IncidentPageRoleType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: UUID, type: IncidentPageRoleType, **kwargs):
        """
        A reference to an incident role for a page.

        :param id: The role identifier.
        :type id: UUID

        :param type: The type of incident role for a page.
        :type type: IncidentPageRoleType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
