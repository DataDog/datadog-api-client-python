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
    from datadog_api_client.v2.model.downtime_response_data import DowntimeResponseData
    from datadog_api_client.v2.model.downtime_response_included_item import DowntimeResponseIncludedItem
    from datadog_api_client.v2.model.downtime_meta import DowntimeMeta
    from datadog_api_client.v2.model.user import User
    from datadog_api_client.v2.model.downtime_monitor_included_item import DowntimeMonitorIncludedItem


class ListDowntimesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_response_data import DowntimeResponseData
        from datadog_api_client.v2.model.downtime_response_included_item import DowntimeResponseIncludedItem
        from datadog_api_client.v2.model.downtime_meta import DowntimeMeta

        return {
            "data": ([DowntimeResponseData],),
            "included": ([DowntimeResponseIncludedItem],),
            "meta": (DowntimeMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[DowntimeResponseData], UnsetType] = unset,
        included: Union[
            List[Union[DowntimeResponseIncludedItem, User, DowntimeMonitorIncludedItem]], UnsetType
        ] = unset,
        meta: Union[DowntimeMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for retrieving all downtimes.

        :param data: An array of downtimes.
        :type data: [DowntimeResponseData], optional

        :param included: Array of objects related to the downtimes.
        :type included: [DowntimeResponseIncludedItem], optional

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
