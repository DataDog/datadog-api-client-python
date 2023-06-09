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
    from datadog_api_client.v2.model.downtime_list_item_response import DowntimeListItemResponse
    from datadog_api_client.v2.model.user_response_included_item import UserResponseIncludedItem
    from datadog_api_client.v2.model.downtime_meta import DowntimeMeta
    from datadog_api_client.v2.model.organization import Organization
    from datadog_api_client.v2.model.permission import Permission
    from datadog_api_client.v2.model.role import Role


class ListDowntimesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_list_item_response import DowntimeListItemResponse
        from datadog_api_client.v2.model.user_response_included_item import UserResponseIncludedItem
        from datadog_api_client.v2.model.downtime_meta import DowntimeMeta

        return {
            "data": ([DowntimeListItemResponse],),
            "included": ([UserResponseIncludedItem],),
            "meta": (DowntimeMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[DowntimeListItemResponse], UnsetType] = unset,
        included: Union[List[Union[UserResponseIncludedItem, Organization, Permission, Role]], UnsetType] = unset,
        meta: Union[DowntimeMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for retrieving all downtimes.

        :param data: An array of downtimes.
        :type data: [DowntimeListItemResponse], optional

        :param included: Array of objects related to the users.
        :type included: [UserResponseIncludedItem], optional

        :param meta: Pagination metadata returned by the API.
        :type meta: DowntimeMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
