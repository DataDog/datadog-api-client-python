# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.list_external_user_group_response_resources_items import (
        ListExternalUserGroupResponseResourcesItems,
    )


class ListExternalUserGroupResponse(ModelNormal):
    validations = {
        "items_per_page": {
            "inclusive_maximum": 4294967295,
            "inclusive_minimum": 0,
        },
        "start_index": {
            "inclusive_maximum": 4294967295,
            "inclusive_minimum": 0,
        },
        "total_results": {
            "inclusive_maximum": 4294967295,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_external_user_group_response_resources_items import (
            ListExternalUserGroupResponseResourcesItems,
        )

        return {
            "resources": ([ListExternalUserGroupResponseResourcesItems],),
            "items_per_page": (int,),
            "schemas": ([str],),
            "start_index": (int,),
            "total_results": (int,),
        }

    attribute_map = {
        "resources": "Resources",
        "items_per_page": "itemsPerPage",
        "schemas": "schemas",
        "start_index": "startIndex",
        "total_results": "totalResults",
    }

    def __init__(
        self_,
        resources: Union[List[ListExternalUserGroupResponseResourcesItems], UnsetType] = unset,
        items_per_page: Union[int, UnsetType] = unset,
        schemas: Union[List[str], UnsetType] = unset,
        start_index: Union[int, UnsetType] = unset,
        total_results: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        List SCIM groups response object.

        :param resources: List of SCIM groups matching the request criteria.
        :type resources: [ListExternalUserGroupResponseResourcesItems], optional

        :param items_per_page: Number of SCIM groups returned per page.
        :type items_per_page: int, optional

        :param schemas: List response JSON Schemas.
        :type schemas: [str], optional

        :param start_index: Starting index of the SCIM groups for this page (1-indexed).
        :type start_index: int, optional

        :param total_results: Total number of SCIM groups matching the request criteria.
        :type total_results: int, optional
        """
        if resources is not unset:
            kwargs["resources"] = resources
        if items_per_page is not unset:
            kwargs["items_per_page"] = items_per_page
        if schemas is not unset:
            kwargs["schemas"] = schemas
        if start_index is not unset:
            kwargs["start_index"] = start_index
        if total_results is not unset:
            kwargs["total_results"] = total_results
        super().__init__(kwargs)
