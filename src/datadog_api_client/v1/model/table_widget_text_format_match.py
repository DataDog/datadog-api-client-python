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
    from datadog_api_client.v1.model.table_widget_text_format_match_type import TableWidgetTextFormatMatchType


class TableWidgetTextFormatMatch(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.table_widget_text_format_match_type import TableWidgetTextFormatMatchType

        return {
            "type": (TableWidgetTextFormatMatchType,),
            "value": (str,),
        }

    attribute_map = {
        "type": "type",
        "value": "value",
    }

    def __init__(self_, type: TableWidgetTextFormatMatchType, value: str, **kwargs):
        """
        Match rule for the table widget text format.

        :param type: Match or compare option.
        :type type: TableWidgetTextFormatMatchType

        :param value: Table Widget Match String.
        :type value: str
        """
        super().__init__(kwargs)

        self_.type = type
        self_.value = value
