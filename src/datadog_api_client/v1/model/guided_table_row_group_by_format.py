# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.guided_table_text_formatting_rule import GuidedTableTextFormattingRule


class GuidedTableRowGroupByFormat(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.guided_table_text_formatting_rule import GuidedTableTextFormattingRule

        return {
            "text_formats": ([GuidedTableTextFormattingRule],),
        }

    attribute_map = {
        "text_formats": "text_formats",
    }

    def __init__(self_, text_formats: Union[List[GuidedTableTextFormattingRule], UnsetType] = unset, **kwargs):
        """
        Text formatting configuration for this group-by column.

        :param text_formats:
        :type text_formats: [GuidedTableTextFormattingRule], optional
        """
        if text_formats is not unset:
            kwargs["text_formats"] = text_formats
        super().__init__(kwargs)
