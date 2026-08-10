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
    from datadog_api_client.v2.model.maintenance_update_data_relationships_user import (
        MaintenanceUpdateDataRelationshipsUser,
    )
    from datadog_api_client.v2.model.maintenance_update_data_relationships_maintenance import (
        MaintenanceUpdateDataRelationshipsMaintenance,
    )


class MaintenanceUpdateDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.maintenance_update_data_relationships_user import (
            MaintenanceUpdateDataRelationshipsUser,
        )
        from datadog_api_client.v2.model.maintenance_update_data_relationships_maintenance import (
            MaintenanceUpdateDataRelationshipsMaintenance,
        )

        return {
            "created_by_user": (MaintenanceUpdateDataRelationshipsUser,),
            "last_modified_by_user": (MaintenanceUpdateDataRelationshipsUser,),
            "maintenance": (MaintenanceUpdateDataRelationshipsMaintenance,),
        }

    attribute_map = {
        "created_by_user": "created_by_user",
        "last_modified_by_user": "last_modified_by_user",
        "maintenance": "maintenance",
    }

    def __init__(
        self_,
        created_by_user: Union[MaintenanceUpdateDataRelationshipsUser, UnsetType] = unset,
        last_modified_by_user: Union[MaintenanceUpdateDataRelationshipsUser, UnsetType] = unset,
        maintenance: Union[MaintenanceUpdateDataRelationshipsMaintenance, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships of a maintenance update resource.

        :param created_by_user: A user relationship of a maintenance update.
        :type created_by_user: MaintenanceUpdateDataRelationshipsUser, optional

        :param last_modified_by_user: A user relationship of a maintenance update.
        :type last_modified_by_user: MaintenanceUpdateDataRelationshipsUser, optional

        :param maintenance: The parent maintenance of the update.
        :type maintenance: MaintenanceUpdateDataRelationshipsMaintenance, optional
        """
        if created_by_user is not unset:
            kwargs["created_by_user"] = created_by_user
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        if maintenance is not unset:
            kwargs["maintenance"] = maintenance
        super().__init__(kwargs)
