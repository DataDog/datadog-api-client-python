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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_maintenance_request_data_attributes import (
        CreateMaintenanceRequestDataAttributes,
    )
    from datadog_api_client.v2.model.create_maintenance_request_data_relationships import (
        CreateMaintenanceRequestDataRelationships,
    )
    from datadog_api_client.v2.model.patch_maintenance_request_data_type import PatchMaintenanceRequestDataType


class CreateMaintenanceRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_maintenance_request_data_attributes import (
            CreateMaintenanceRequestDataAttributes,
        )
        from datadog_api_client.v2.model.create_maintenance_request_data_relationships import (
            CreateMaintenanceRequestDataRelationships,
        )
        from datadog_api_client.v2.model.patch_maintenance_request_data_type import PatchMaintenanceRequestDataType

        return {
            "attributes": (CreateMaintenanceRequestDataAttributes,),
            "relationships": (CreateMaintenanceRequestDataRelationships,),
            "type": (PatchMaintenanceRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CreateMaintenanceRequestDataAttributes,
        type: PatchMaintenanceRequestDataType,
        relationships: Union[CreateMaintenanceRequestDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object for creating a maintenance.

        :param attributes: The supported attributes for creating a maintenance.
        :type attributes: CreateMaintenanceRequestDataAttributes

        :param relationships: The supported relationships for creating a maintenance.
        :type relationships: CreateMaintenanceRequestDataRelationships, optional

        :param type: Maintenances resource type.
        :type type: PatchMaintenanceRequestDataType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
