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
    from datadog_api_client.v2.model.custom_forecast_entry_tag_filter import CustomForecastEntryTagFilter


class CustomForecastEntry(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_forecast_entry_tag_filter import CustomForecastEntryTagFilter

        return {
            "amount": (float,),
            "month": (int,),
            "tag_filters": ([CustomForecastEntryTagFilter],),
        }

    attribute_map = {
        "amount": "amount",
        "month": "month",
        "tag_filters": "tag_filters",
    }

    def __init__(self_, amount: float, month: int, tag_filters: List[CustomForecastEntryTagFilter], **kwargs):
        """
        A monthly entry of a custom budget forecast.

        :param amount: Forecast amount for the month.
        :type amount: float

        :param month: Month the custom forecast entry applies to, in ``YYYYMM`` format.
        :type month: int

        :param tag_filters: Tag filters that scope this custom forecast entry to specific resources.
        :type tag_filters: [CustomForecastEntryTagFilter]
        """
        super().__init__(kwargs)

        self_.amount = amount
        self_.month = month
        self_.tag_filters = tag_filters
