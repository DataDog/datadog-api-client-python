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
    from datadog_api_client.v2.model.maintenance_data_relationships_created_by_user import (
        MaintenanceDataRelationshipsCreatedByUser,
    )
    from datadog_api_client.v2.model.maintenance_data_relationships_last_modified_by_user import (
        MaintenanceDataRelationshipsLastModifiedByUser,
    )
    from datadog_api_client.v2.model.maintenance_data_relationships_status_page import (
        MaintenanceDataRelationshipsStatusPage,
    )


class MaintenanceDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.maintenance_data_relationships_created_by_user import (
            MaintenanceDataRelationshipsCreatedByUser,
        )
        from datadog_api_client.v2.model.maintenance_data_relationships_last_modified_by_user import (
            MaintenanceDataRelationshipsLastModifiedByUser,
        )
        from datadog_api_client.v2.model.maintenance_data_relationships_status_page import (
            MaintenanceDataRelationshipsStatusPage,
        )

        return {
            "created_by_user": (MaintenanceDataRelationshipsCreatedByUser,),
            "last_modified_by_user": (MaintenanceDataRelationshipsLastModifiedByUser,),
            "status_page": (MaintenanceDataRelationshipsStatusPage,),
        }

    attribute_map = {
        "created_by_user": "created_by_user",
        "last_modified_by_user": "last_modified_by_user",
        "status_page": "status_page",
    }

    def __init__(
        self_,
        created_by_user: Union[MaintenanceDataRelationshipsCreatedByUser, UnsetType] = unset,
        last_modified_by_user: Union[MaintenanceDataRelationshipsLastModifiedByUser, UnsetType] = unset,
        status_page: Union[MaintenanceDataRelationshipsStatusPage, UnsetType] = unset,
        **kwargs,
    ):
        """
        The relationships of a maintenance.

        :param created_by_user:
        :type created_by_user: MaintenanceDataRelationshipsCreatedByUser, optional

        :param last_modified_by_user:
        :type last_modified_by_user: MaintenanceDataRelationshipsLastModifiedByUser, optional

        :param status_page:
        :type status_page: MaintenanceDataRelationshipsStatusPage, optional
        """
        if created_by_user is not unset:
            kwargs["created_by_user"] = created_by_user
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        if status_page is not unset:
            kwargs["status_page"] = status_page
        super().__init__(kwargs)
