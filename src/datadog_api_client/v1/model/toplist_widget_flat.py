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
    from datadog_api_client.v1.model.toplist_widget_flat_type import ToplistWidgetFlatType


class ToplistWidgetFlat(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.toplist_widget_flat_type import ToplistWidgetFlatType

        return {
            "type": (ToplistWidgetFlatType,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: ToplistWidgetFlatType, **kwargs):
        """
        Top list widget flat display.

        :param type: Top list widget flat display type.
        :type type: ToplistWidgetFlatType
        """
        super().__init__(kwargs)

        self_.type = type
