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
    from datadog_api_client.v2.model.status_page_as_included_relationships_created_by_user import (
        StatusPageAsIncludedRelationshipsCreatedByUser,
    )
    from datadog_api_client.v2.model.status_page_as_included_relationships_last_modified_by_user import (
        StatusPageAsIncludedRelationshipsLastModifiedByUser,
    )


class StatusPageAsIncludedRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_page_as_included_relationships_created_by_user import (
            StatusPageAsIncludedRelationshipsCreatedByUser,
        )
        from datadog_api_client.v2.model.status_page_as_included_relationships_last_modified_by_user import (
            StatusPageAsIncludedRelationshipsLastModifiedByUser,
        )

        return {
            "created_by_user": (StatusPageAsIncludedRelationshipsCreatedByUser,),
            "last_modified_by_user": (StatusPageAsIncludedRelationshipsLastModifiedByUser,),
        }

    attribute_map = {
        "created_by_user": "created_by_user",
        "last_modified_by_user": "last_modified_by_user",
    }

    def __init__(
        self_,
        created_by_user: Union[StatusPageAsIncludedRelationshipsCreatedByUser, UnsetType] = unset,
        last_modified_by_user: Union[StatusPageAsIncludedRelationshipsLastModifiedByUser, UnsetType] = unset,
        **kwargs,
    ):
        """
        The relationships of a status page.

        :param created_by_user:
        :type created_by_user: StatusPageAsIncludedRelationshipsCreatedByUser, optional

        :param last_modified_by_user:
        :type last_modified_by_user: StatusPageAsIncludedRelationshipsLastModifiedByUser, optional
        """
        if created_by_user is not unset:
            kwargs["created_by_user"] = created_by_user
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        super().__init__(kwargs)
