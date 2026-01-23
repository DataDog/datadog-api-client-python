# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WidgetStyleOrderBy(ModelSimple):
    """
    How to order series in timeseries visualizations.
        - `tags`: Order series alphabetically by tag name (default behavior)
        - `values`: Order series by their current metric values (typically descending)

    :param value: Must be one of ["tags", "values"].
    :type value: str
    """

    allowed_values = {
        "tags",
        "values",
    }
    TAGS: ClassVar["WidgetStyleOrderBy"]
    VALUES: ClassVar["WidgetStyleOrderBy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetStyleOrderBy.TAGS = WidgetStyleOrderBy("tags")
WidgetStyleOrderBy.VALUES = WidgetStyleOrderBy("values")
