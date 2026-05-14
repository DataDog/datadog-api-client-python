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
    from datadog_api_client.v2.model.incident_reserved_role_data_attributes_response import (
        IncidentReservedRoleDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_reserved_role_type import IncidentReservedRoleType


class IncidentReservedRoleDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_reserved_role_data_attributes_response import (
            IncidentReservedRoleDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_reserved_role_type import IncidentReservedRoleType

        return {
            "attributes": (IncidentReservedRoleDataAttributesResponse,),
            "id": (UUID,),
            "type": (IncidentReservedRoleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentReservedRoleDataAttributesResponse,
        id: UUID,
        type: IncidentReservedRoleType,
        **kwargs,
    ):
        """
        Reserved role data in a response.

        :param attributes: Attributes of a reserved role.
        :type attributes: IncidentReservedRoleDataAttributesResponse

        :param id: The reserved role identifier.
        :type id: UUID

        :param type: Incident reserved role resource type.
        :type type: IncidentReservedRoleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
