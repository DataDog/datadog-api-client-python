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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_user_defined_role_patch_data_attributes_request import (
        IncidentUserDefinedRolePatchDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_user_defined_role_type import IncidentUserDefinedRoleType


class IncidentUserDefinedRolePatchDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_role_patch_data_attributes_request import (
            IncidentUserDefinedRolePatchDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_user_defined_role_type import IncidentUserDefinedRoleType

        return {
            "attributes": (IncidentUserDefinedRolePatchDataAttributesRequest,),
            "id": (UUID,),
            "type": (IncidentUserDefinedRoleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: IncidentUserDefinedRoleType,
        attributes: Union[IncidentUserDefinedRolePatchDataAttributesRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for updating an incident user-defined role.

        :param attributes: Attributes for updating an incident user-defined role.
        :type attributes: IncidentUserDefinedRolePatchDataAttributesRequest, optional

        :param id: The ID of the user-defined role to update.
        :type id: UUID

        :param type: Incident user-defined role resource type.
        :type type: IncidentUserDefinedRoleType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
