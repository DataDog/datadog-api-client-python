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
    from datadog_api_client.v1.model.table_widget_text_format_replace_all_type import (
        TableWidgetTextFormatReplaceAllType,
    )


class TableWidgetTextFormatReplaceAll(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.table_widget_text_format_replace_all_type import (
            TableWidgetTextFormatReplaceAllType,
        )

        return {
            "type": (TableWidgetTextFormatReplaceAllType,),
            "_with": (str,),
        }

    attribute_map = {
        "type": "type",
        "_with": "with",
    }

    def __init__(self_, type: TableWidgetTextFormatReplaceAllType, _with: str, **kwargs):
        """
        Match All definition.

        :param type: Table widget text format replace all type.
        :type type: TableWidgetTextFormatReplaceAllType

        :param _with: Replace All type.
        :type _with: str
        """
        super().__init__(kwargs)

        self_.type = type
        self_._with = _with
