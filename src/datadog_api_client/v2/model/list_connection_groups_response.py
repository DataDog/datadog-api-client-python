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
    from datadog_api_client.v2.model.connection_group_data_response import ConnectionGroupDataResponse
    from datadog_api_client.v2.model.list_connection_groups_response_meta import ListConnectionGroupsResponseMeta


class ListConnectionGroupsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.connection_group_data_response import ConnectionGroupDataResponse
        from datadog_api_client.v2.model.list_connection_groups_response_meta import ListConnectionGroupsResponseMeta

        return {
            "data": ([ConnectionGroupDataResponse],),
            "meta": (ListConnectionGroupsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[ConnectionGroupDataResponse],
        meta: Union[ListConnectionGroupsResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for listing connection groups.

        :param data: An array of connection groups.
        :type data: [ConnectionGroupDataResponse]

        :param meta: Metadata for the list connection groups response.
        :type meta: ListConnectionGroupsResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
