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
    from datadog_api_client.v2.model.status_pages_component_group_relationships_created_by_user import (
        StatusPagesComponentGroupRelationshipsCreatedByUser,
    )
    from datadog_api_client.v2.model.status_pages_component_group_relationships_group import (
        StatusPagesComponentGroupRelationshipsGroup,
    )
    from datadog_api_client.v2.model.status_pages_component_group_relationships_last_modified_by_user import (
        StatusPagesComponentGroupRelationshipsLastModifiedByUser,
    )
    from datadog_api_client.v2.model.status_pages_component_group_relationships_status_page import (
        StatusPagesComponentGroupRelationshipsStatusPage,
    )


class StatusPagesComponentGroupRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_pages_component_group_relationships_created_by_user import (
            StatusPagesComponentGroupRelationshipsCreatedByUser,
        )
        from datadog_api_client.v2.model.status_pages_component_group_relationships_group import (
            StatusPagesComponentGroupRelationshipsGroup,
        )
        from datadog_api_client.v2.model.status_pages_component_group_relationships_last_modified_by_user import (
            StatusPagesComponentGroupRelationshipsLastModifiedByUser,
        )
        from datadog_api_client.v2.model.status_pages_component_group_relationships_status_page import (
            StatusPagesComponentGroupRelationshipsStatusPage,
        )

        return {
            "created_by_user": (StatusPagesComponentGroupRelationshipsCreatedByUser,),
            "group": (StatusPagesComponentGroupRelationshipsGroup,),
            "last_modified_by_user": (StatusPagesComponentGroupRelationshipsLastModifiedByUser,),
            "status_page": (StatusPagesComponentGroupRelationshipsStatusPage,),
        }

    attribute_map = {
        "created_by_user": "created_by_user",
        "group": "group",
        "last_modified_by_user": "last_modified_by_user",
        "status_page": "status_page",
    }

    def __init__(
        self_,
        created_by_user: Union[StatusPagesComponentGroupRelationshipsCreatedByUser, UnsetType] = unset,
        group: Union[StatusPagesComponentGroupRelationshipsGroup, UnsetType] = unset,
        last_modified_by_user: Union[StatusPagesComponentGroupRelationshipsLastModifiedByUser, UnsetType] = unset,
        status_page: Union[StatusPagesComponentGroupRelationshipsStatusPage, UnsetType] = unset,
        **kwargs,
    ):
        """
        The relationships of a component group.

        :param created_by_user: The Datadog user who created the component group.
        :type created_by_user: StatusPagesComponentGroupRelationshipsCreatedByUser, optional

        :param group: The group the component group belongs to.
        :type group: StatusPagesComponentGroupRelationshipsGroup, optional

        :param last_modified_by_user: The Datadog user who last modified the component group.
        :type last_modified_by_user: StatusPagesComponentGroupRelationshipsLastModifiedByUser, optional

        :param status_page: The status page the component group belongs to.
        :type status_page: StatusPagesComponentGroupRelationshipsStatusPage, optional
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
