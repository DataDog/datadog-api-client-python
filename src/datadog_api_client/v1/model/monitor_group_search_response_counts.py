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
    from datadog_api_client.v1.model.monitor_search_count_item import MonitorSearchCountItem


class MonitorGroupSearchResponseCounts(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_search_count_item import MonitorSearchCountItem

        return {
            "status": ([MonitorSearchCountItem],),
            "type": ([MonitorSearchCountItem],),
        }

    attribute_map = {
        "status": "status",
        "type": "type",
    }

    def __init__(
        self_,
        status: Union[List[MonitorSearchCountItem], UnsetType] = unset,
        type: Union[List[MonitorSearchCountItem], UnsetType] = unset,
        **kwargs,
    ):
        """
        The counts of monitor groups per different criteria.

        :param status: Search facets.
        :type status: [MonitorSearchCountItem], optional

        :param type: Search facets.
        :type type: [MonitorSearchCountItem], optional
        """
        if status is not unset:
            kwargs["status"] = status
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
