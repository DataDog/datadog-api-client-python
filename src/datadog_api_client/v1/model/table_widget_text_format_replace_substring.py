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
    from datadog_api_client.v1.model.table_widget_text_format_replace_substring_type import (
        TableWidgetTextFormatReplaceSubstringType,
    )


class TableWidgetTextFormatReplaceSubstring(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.table_widget_text_format_replace_substring_type import (
            TableWidgetTextFormatReplaceSubstringType,
        )

        return {
            "substring": (str,),
            "type": (TableWidgetTextFormatReplaceSubstringType,),
            "_with": (str,),
        }

    attribute_map = {
        "substring": "substring",
        "type": "type",
        "_with": "with",
    }

    def __init__(self_, substring: str, type: TableWidgetTextFormatReplaceSubstringType, _with: str, **kwargs):
        """
        Match Sub-string definition.

        :param substring: Text that will be replaced.
        :type substring: str

        :param type: Table widget text format replace sub-string type.
        :type type: TableWidgetTextFormatReplaceSubstringType

        :param _with: Text that will replace original sub-string.
        :type _with: str
        """
        super().__init__(kwargs)

        self_.substring = substring
        self_.type = type
        self_._with = _with
