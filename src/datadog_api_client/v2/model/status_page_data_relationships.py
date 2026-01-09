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
    from datadog_api_client.v2.model.status_page_data_relationships_created_by_user import (
        StatusPageDataRelationshipsCreatedByUser,
    )
    from datadog_api_client.v2.model.status_page_data_relationships_last_modified_by_user import (
        StatusPageDataRelationshipsLastModifiedByUser,
    )


class StatusPageDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_page_data_relationships_created_by_user import (
            StatusPageDataRelationshipsCreatedByUser,
        )
        from datadog_api_client.v2.model.status_page_data_relationships_last_modified_by_user import (
            StatusPageDataRelationshipsLastModifiedByUser,
        )

        return {
            "created_by_user": (StatusPageDataRelationshipsCreatedByUser,),
            "last_modified_by_user": (StatusPageDataRelationshipsLastModifiedByUser,),
        }

    attribute_map = {
        "created_by_user": "created_by_user",
        "last_modified_by_user": "last_modified_by_user",
    }

    def __init__(
        self_,
        created_by_user: Union[StatusPageDataRelationshipsCreatedByUser, UnsetType] = unset,
        last_modified_by_user: Union[StatusPageDataRelationshipsLastModifiedByUser, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param created_by_user:
        :type created_by_user: StatusPageDataRelationshipsCreatedByUser, optional

        :param last_modified_by_user:
        :type last_modified_by_user: StatusPageDataRelationshipsLastModifiedByUser, optional
        """
        if created_by_user is not unset:
            kwargs["created_by_user"] = created_by_user
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        super().__init__(kwargs)
