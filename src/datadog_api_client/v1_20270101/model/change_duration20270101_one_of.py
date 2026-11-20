# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.fixed_span2 import FixedSpan2
    from datadog_api_client.v1_20270101.model.change_duration_any_of_any_of_item_type import (
        ChangeDurationAnyOfAnyOfItemType,
    )


class ChangeDuration20270101OneOf(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.fixed_span2 import FixedSpan2
        from datadog_api_client.v1_20270101.model.change_duration_any_of_any_of_item_type import (
            ChangeDurationAnyOfAnyOfItemType,
        )

        return {
            "custom_timeframe": (FixedSpan2,),
            "type": (ChangeDurationAnyOfAnyOfItemType,),
        }

    attribute_map = {
        "custom_timeframe": "custom_timeframe",
        "type": "type",
    }

    def __init__(self_, custom_timeframe: FixedSpan2, type: ChangeDurationAnyOfAnyOfItemType, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param custom_timeframe: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_timeframe: FixedSpan2

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: ChangeDurationAnyOfAnyOfItemType
        """
        super().__init__(kwargs)

        self_.custom_timeframe = custom_timeframe
        self_.type = type
