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
    from datadog_api_client.v2.model.widget_type import WidgetType


class Definition(ModelNormal):
    validations = {
        "title": {
            "max_length": 100,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.widget_type import WidgetType

        return {
            "title": (str,),
            "type": (WidgetType,),
        }

    attribute_map = {
        "title": "title",
        "type": "type",
    }

    def __init__(self_, title: str, type: WidgetType, **kwargs):
        """
        The definition of a widget, including its type and configuration.

        :param title: The display title of the widget.
        :type title: str

        :param type: Widget types that are allowed to be stored as individual records in the 'widget' PG table.

            This is not a complete list of dashboards/notebooks widget types.
        :type type: WidgetType
        """
        super().__init__(kwargs)

        self_.title = title
        self_.type = type
