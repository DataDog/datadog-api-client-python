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
    from datadog_api_client.v2.model.status_pages_component_data_relationships_created_by_user import (
        StatusPagesComponentDataRelationshipsCreatedByUser,
    )
    from datadog_api_client.v2.model.status_pages_component_data_relationships_group import (
        StatusPagesComponentDataRelationshipsGroup,
    )
    from datadog_api_client.v2.model.status_pages_component_data_relationships_last_modified_by_user import (
        StatusPagesComponentDataRelationshipsLastModifiedByUser,
    )
    from datadog_api_client.v2.model.status_pages_component_data_relationships_status_page import (
        StatusPagesComponentDataRelationshipsStatusPage,
    )


class StatusPagesComponentDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_pages_component_data_relationships_created_by_user import (
            StatusPagesComponentDataRelationshipsCreatedByUser,
        )
        from datadog_api_client.v2.model.status_pages_component_data_relationships_group import (
            StatusPagesComponentDataRelationshipsGroup,
        )
        from datadog_api_client.v2.model.status_pages_component_data_relationships_last_modified_by_user import (
            StatusPagesComponentDataRelationshipsLastModifiedByUser,
        )
        from datadog_api_client.v2.model.status_pages_component_data_relationships_status_page import (
            StatusPagesComponentDataRelationshipsStatusPage,
        )

        return {
            "created_by_user": (StatusPagesComponentDataRelationshipsCreatedByUser,),
            "group": (StatusPagesComponentDataRelationshipsGroup,),
            "last_modified_by_user": (StatusPagesComponentDataRelationshipsLastModifiedByUser,),
            "status_page": (StatusPagesComponentDataRelationshipsStatusPage,),
        }

    attribute_map = {
        "created_by_user": "created_by_user",
        "group": "group",
        "last_modified_by_user": "last_modified_by_user",
        "status_page": "status_page",
    }

    def __init__(
        self_,
        created_by_user: Union[StatusPagesComponentDataRelationshipsCreatedByUser, UnsetType] = unset,
        group: Union[StatusPagesComponentDataRelationshipsGroup, UnsetType] = unset,
        last_modified_by_user: Union[StatusPagesComponentDataRelationshipsLastModifiedByUser, UnsetType] = unset,
        status_page: Union[StatusPagesComponentDataRelationshipsStatusPage, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param created_by_user:
        :type created_by_user: StatusPagesComponentDataRelationshipsCreatedByUser, optional

        :param group:
        :type group: StatusPagesComponentDataRelationshipsGroup, optional

        :param last_modified_by_user:
        :type last_modified_by_user: StatusPagesComponentDataRelationshipsLastModifiedByUser, optional

        :param status_page:
        :type status_page: StatusPagesComponentDataRelationshipsStatusPage, optional
        """
        if created_by_user is not unset:
            kwargs["created_by_user"] = created_by_user
        if group is not unset:
            kwargs["group"] = group
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        if status_page is not unset:
            kwargs["status_page"] = status_page
        super().__init__(kwargs)
