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
    from datadog_api_client.v2.model.user import User
    from datadog_api_client.v2.model.downtime_monitor_included_item import DowntimeMonitorIncludedItem


class DowntimeResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_response_data import DowntimeResponseData
        from datadog_api_client.v2.model.downtime_response_included_item import DowntimeResponseIncludedItem

        return {
            "data": (DowntimeResponseData,),
            "included": ([DowntimeResponseIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[DowntimeResponseData, UnsetType] = unset,
        included: Union[
            List[Union[DowntimeResponseIncludedItem, User, DowntimeMonitorIncludedItem]], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Downtiming gives you greater control over monitor notifications by
        allowing you to globally exclude scopes from alerting.
        Downtime settings, which can be scheduled with start and end times,
        prevent all alerting related to specified Datadog tags.

        :param data: Downtime data.
        :type data: DowntimeResponseData, optional

        :param included: Array of objects related to the downtime that the user requested.
        :type included: [DowntimeResponseIncludedItem], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
