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
    from datadog_api_client.v2.model.maintenance_data_relationships_template import MaintenanceDataRelationshipsTemplate


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
        from datadog_api_client.v2.model.maintenance_data_relationships_template import (
            MaintenanceDataRelationshipsTemplate,
        )

        return {
            "created_by_user": (MaintenanceDataRelationshipsCreatedByUser,),
            "last_modified_by_user": (MaintenanceDataRelationshipsLastModifiedByUser,),
            "status_page": (MaintenanceDataRelationshipsStatusPage,),
            "template": (MaintenanceDataRelationshipsTemplate,),
        }

    attribute_map = {
        "created_by_user": "created_by_user",
        "last_modified_by_user": "last_modified_by_user",
        "status_page": "status_page",
        "template": "template",
    }

    def __init__(
        self_,
        created_by_user: Union[MaintenanceDataRelationshipsCreatedByUser, UnsetType] = unset,
        last_modified_by_user: Union[MaintenanceDataRelationshipsLastModifiedByUser, UnsetType] = unset,
        status_page: Union[MaintenanceDataRelationshipsStatusPage, UnsetType] = unset,
        template: Union[MaintenanceDataRelationshipsTemplate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The relationships of a maintenance.

        :param created_by_user: The Datadog user who created the maintenance.
        :type created_by_user: MaintenanceDataRelationshipsCreatedByUser, optional

        :param last_modified_by_user: The Datadog user who last modified the maintenance.
        :type last_modified_by_user: MaintenanceDataRelationshipsLastModifiedByUser, optional

        :param status_page: The status page the maintenance belongs to.
        :type status_page: MaintenanceDataRelationshipsStatusPage, optional

        :param template: The template the maintenance was created from.
        :type template: MaintenanceDataRelationshipsTemplate, optional
        """
        if created_by_user is not unset:
            kwargs["created_by_user"] = created_by_user
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        if status_page is not unset:
            kwargs["status_page"] = status_page
        if template is not unset:
            kwargs["template"] = template
        super().__init__(kwargs)
