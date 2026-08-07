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
    from datadog_api_client.v2.model.maintenance_update_data_attributes import MaintenanceUpdateDataAttributes
    from datadog_api_client.v2.model.maintenance_update_data_relationships import MaintenanceUpdateDataRelationships
    from datadog_api_client.v2.model.patch_maintenance_update_request_data_type import (
        PatchMaintenanceUpdateRequestDataType,
    )


class MaintenanceUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.maintenance_update_data_attributes import MaintenanceUpdateDataAttributes
        from datadog_api_client.v2.model.maintenance_update_data_relationships import MaintenanceUpdateDataRelationships
        from datadog_api_client.v2.model.patch_maintenance_update_request_data_type import (
            PatchMaintenanceUpdateRequestDataType,
        )

        return {
            "attributes": (MaintenanceUpdateDataAttributes,),
            "id": (UUID,),
            "relationships": (MaintenanceUpdateDataRelationships,),
            "type": (PatchMaintenanceUpdateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: PatchMaintenanceUpdateRequestDataType,
        attributes: Union[MaintenanceUpdateDataAttributes, UnsetType] = unset,
        relationships: Union[MaintenanceUpdateDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object for a maintenance update.

        :param attributes: Attributes of a maintenance update resource.
        :type attributes: MaintenanceUpdateDataAttributes, optional

        :param id: The ID of the maintenance update.
        :type id: UUID

        :param relationships: Relationships of a maintenance update resource.
        :type relationships: MaintenanceUpdateDataRelationships, optional

        :param type: Maintenance updates resource type.
        :type type: PatchMaintenanceUpdateRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
