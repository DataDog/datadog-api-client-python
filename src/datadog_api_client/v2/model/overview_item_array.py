# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.overview_item_data import OverviewItemData


class OverviewItemArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.overview_item_data import OverviewItemData

        return {
            "data": ([OverviewItemData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[OverviewItemData], **kwargs):
        """
        Response body for the overview endpoint, returning the tiles shown on the
        End User Device Monitoring overview dashboard.

        :param data: List of overview tiles.
        :type data: [OverviewItemData]
        """
        super().__init__(kwargs)

        self_.data = data
