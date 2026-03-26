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
    from datadog_api_client.v1.model.wildcard_widget_specification_type import WildcardWidgetSpecificationType


class WildcardWidgetSpecification(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.wildcard_widget_specification_type import WildcardWidgetSpecificationType

        return {
            "contents": (dict,),
            "type": (WildcardWidgetSpecificationType,),
        }

    attribute_map = {
        "contents": "contents",
        "type": "type",
    }

    def __init__(self_, contents: dict, type: WildcardWidgetSpecificationType, **kwargs):
        """
        Vega or Vega-Lite specification for custom visualization rendering. See https://vega.github.io/vega-lite/ for the full grammar reference.

        :param contents: The Vega or Vega-Lite JSON specification object.
        :type contents: dict

        :param type: Type of specification used by the wildcard widget.
        :type type: WildcardWidgetSpecificationType
        """
        super().__init__(kwargs)

        self_.contents = contents
        self_.type = type
