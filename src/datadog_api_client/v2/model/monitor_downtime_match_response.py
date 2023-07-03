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
    from datadog_api_client.v2.model.monitor_downtime_match_response_data import MonitorDowntimeMatchResponseData
    from datadog_api_client.v2.model.downtime_meta import DowntimeMeta


class MonitorDowntimeMatchResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_downtime_match_response_data import MonitorDowntimeMatchResponseData
        from datadog_api_client.v2.model.downtime_meta import DowntimeMeta

        return {
            "data": ([MonitorDowntimeMatchResponseData],),
            "meta": (DowntimeMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[MonitorDowntimeMatchResponseData], UnsetType] = unset,
        meta: Union[DowntimeMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for retrieving all downtime matches for a monitor.

        :param data: An array of downtime matches.
        :type data: [MonitorDowntimeMatchResponseData], optional

        :param meta: Pagination metadata returned by the API.
        :type meta: DowntimeMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
