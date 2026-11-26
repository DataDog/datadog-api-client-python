# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.text_formatting_rule import TextFormattingRule


class TableRowGroupByFormat(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.text_formatting_rule import TextFormattingRule

        return {
            "text_formats": ([TextFormattingRule],),
        }

    attribute_map = {
        "text_formats": "text_formats",
    }

    def __init__(self_, text_formats: List[TextFormattingRule], **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param text_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_formats: [TextFormattingRule]
        """
        super().__init__(kwargs)

        self_.text_formats = text_formats
