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
    from datadog_api_client.v2.model.maintenance_data_attributes import MaintenanceDataAttributes
    from datadog_api_client.v2.model.maintenance_data_relationships import MaintenanceDataRelationships
    from datadog_api_client.v2.model.patch_maintenance_request_data_type import PatchMaintenanceRequestDataType


class MaintenanceData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.maintenance_data_attributes import MaintenanceDataAttributes
        from datadog_api_client.v2.model.maintenance_data_relationships import MaintenanceDataRelationships
        from datadog_api_client.v2.model.patch_maintenance_request_data_type import PatchMaintenanceRequestDataType

        return {
            "attributes": (MaintenanceDataAttributes,),
            "id": (UUID,),
            "relationships": (MaintenanceDataRelationships,),
            "type": (PatchMaintenanceRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: PatchMaintenanceRequestDataType,
        attributes: Union[MaintenanceDataAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        relationships: Union[MaintenanceDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes: The attributes of a maintenance.
        :type attributes: MaintenanceDataAttributes, optional

        :param id: The ID of the maintenance.
        :type id: UUID, optional

        :param relationships: The relationships of a maintenance.
        :type relationships: MaintenanceDataRelationships, optional

        :param type: Maintenances resource type.
        :type type: PatchMaintenanceRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
