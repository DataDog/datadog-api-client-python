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
    from datadog_api_client.v2.model.maintenance_template_data_relationships_created_by_user import (
        MaintenanceTemplateDataRelationshipsCreatedByUser,
    )
    from datadog_api_client.v2.model.maintenance_template_data_relationships_last_modified_by_user import (
        MaintenanceTemplateDataRelationshipsLastModifiedByUser,
    )
    from datadog_api_client.v2.model.maintenance_template_data_relationships_status_page import (
        MaintenanceTemplateDataRelationshipsStatusPage,
    )


class MaintenanceTemplateDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.maintenance_template_data_relationships_created_by_user import (
            MaintenanceTemplateDataRelationshipsCreatedByUser,
        )
        from datadog_api_client.v2.model.maintenance_template_data_relationships_last_modified_by_user import (
            MaintenanceTemplateDataRelationshipsLastModifiedByUser,
        )
        from datadog_api_client.v2.model.maintenance_template_data_relationships_status_page import (
            MaintenanceTemplateDataRelationshipsStatusPage,
        )

        return {
            "created_by_user": (MaintenanceTemplateDataRelationshipsCreatedByUser,),
            "last_modified_by_user": (MaintenanceTemplateDataRelationshipsLastModifiedByUser,),
            "status_page": (MaintenanceTemplateDataRelationshipsStatusPage,),
        }

    attribute_map = {
        "created_by_user": "created_by_user",
        "last_modified_by_user": "last_modified_by_user",
        "status_page": "status_page",
    }

    def __init__(
        self_,
        created_by_user: Union[MaintenanceTemplateDataRelationshipsCreatedByUser, UnsetType] = unset,
        last_modified_by_user: Union[MaintenanceTemplateDataRelationshipsLastModifiedByUser, UnsetType] = unset,
        status_page: Union[MaintenanceTemplateDataRelationshipsStatusPage, UnsetType] = unset,
        **kwargs,
    ):
        """
        The relationships of a maintenance template.

        :param created_by_user: The Datadog user who created the maintenance template.
        :type created_by_user: MaintenanceTemplateDataRelationshipsCreatedByUser, optional

        :param last_modified_by_user: The Datadog user who last modified the maintenance template.
        :type last_modified_by_user: MaintenanceTemplateDataRelationshipsLastModifiedByUser, optional

        :param status_page: The status page the maintenance template belongs to.
        :type status_page: MaintenanceTemplateDataRelationshipsStatusPage, optional
        """
        if created_by_user is not unset:
            kwargs["created_by_user"] = created_by_user
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        if status_page is not unset:
            kwargs["status_page"] = status_page
        super().__init__(kwargs)
