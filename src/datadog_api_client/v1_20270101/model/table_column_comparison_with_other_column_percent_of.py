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
    from datadog_api_client.v1_20270101.model.table_column_comparison_with_other_column_percent_of_type import (
        TableColumnComparisonWithOtherColumnPercentOfType,
    )


class TableColumnComparisonWithOtherColumnPercentOf(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.table_column_comparison_with_other_column_percent_of_type import (
            TableColumnComparisonWithOtherColumnPercentOfType,
        )

        return {
            "column": (str,),
            "type": (TableColumnComparisonWithOtherColumnPercentOfType,),
        }

    attribute_map = {
        "column": "column",
        "type": "type",
    }

    def __init__(self_, column: str, type: TableColumnComparisonWithOtherColumnPercentOfType, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: TableColumnComparisonWithOtherColumnPercentOfType
        """
        super().__init__(kwargs)

        self_.column = column
        self_.type = type
