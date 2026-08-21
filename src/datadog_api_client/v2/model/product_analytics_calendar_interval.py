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
    from datadog_api_client.v2.model.product_analytics_calendar_interval_type import (
        ProductAnalyticsCalendarIntervalType,
    )


class ProductAnalyticsCalendarInterval(ModelNormal):
    validations = {
        "quantity": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_calendar_interval_type import (
            ProductAnalyticsCalendarIntervalType,
        )

        return {
            "alignment": (str,),
            "quantity": (int,),
            "timezone": (str,),
            "type": (ProductAnalyticsCalendarIntervalType,),
        }

    attribute_map = {
        "alignment": "alignment",
        "quantity": "quantity",
        "timezone": "timezone",
        "type": "type",
    }

    def __init__(
        self_,
        type: ProductAnalyticsCalendarIntervalType,
        alignment: Union[str, UnsetType] = unset,
        quantity: Union[int, UnsetType] = unset,
        timezone: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A calendar-aligned bucket definition, such as "every 1 week starting on Monday".

        :param alignment: Where each bucket starts within the calendar unit. Use an hour for ``day`` (for example ``1am`` or ``14`` ),
            a day name for ``week`` (for example ``monday`` ), or an ordinal for ``month`` (for example ``1st`` ).
        :type alignment: str, optional

        :param quantity: Number of calendar units per bucket.
        :type quantity: int, optional

        :param timezone: Timezone used to align the buckets.
        :type timezone: str, optional

        :param type: Calendar unit used to bucket cohorts.
        :type type: ProductAnalyticsCalendarIntervalType
        """
        if alignment is not unset:
            kwargs["alignment"] = alignment
        if quantity is not unset:
            kwargs["quantity"] = quantity
        if timezone is not unset:
            kwargs["timezone"] = timezone
        super().__init__(kwargs)

        self_.type = type
