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
    from datadog_api_client.v1_20270101.model.sunburst_known_legend_any_of_any_of_item_type4452236352 import (
        SunburstKnownLegendAnyOfAnyOfItemType4452236352,
    )


class SunburstKnownLegend20270101OneOf4462657920(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.sunburst_known_legend_any_of_any_of_item_type4452236352 import (
            SunburstKnownLegendAnyOfAnyOfItemType4452236352,
        )

        return {
            "type": (SunburstKnownLegendAnyOfAnyOfItemType4452236352,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: SunburstKnownLegendAnyOfAnyOfItemType4452236352, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: SunburstKnownLegendAnyOfAnyOfItemType4452236352
        """
        super().__init__(kwargs)

        self_.type = type
