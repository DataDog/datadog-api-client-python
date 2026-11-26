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
    from datadog_api_client.v1_20270101.model.table_column_comparison import TableColumnComparison
    from datadog_api_client.v1_20270101.model.number_bar_table_column_format import NumberBarTableColumnFormat
    from datadog_api_client.v1_20270101.model.table_column_function import TableColumnFunction
    from datadog_api_client.v1_20270101.model.number_reference_table_column_reference import (
        NumberReferenceTableColumnReference,
    )
    from datadog_api_client.v1_20270101.model.number_reference_table_column_type import NumberReferenceTableColumnType
    from datadog_api_client.v1_20270101.model.table_column_comparison_with_self import TableColumnComparisonWithSelf
    from datadog_api_client.v1_20270101.model.table_column_comparison_with_other_column_diff_from import (
        TableColumnComparisonWithOtherColumnDiffFrom,
    )
    from datadog_api_client.v1_20270101.model.table_column_comparison_with_other_column_percent_of import (
        TableColumnComparisonWithOtherColumnPercentOf,
    )
    from datadog_api_client.v1_20270101.model.table_column_comparison_with_other_column_percent_diff_from import (
        TableColumnComparisonWithOtherColumnPercentDiffFrom,
    )


class NumberReferenceTableColumn(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.table_column_comparison import TableColumnComparison
        from datadog_api_client.v1_20270101.model.number_bar_table_column_format import NumberBarTableColumnFormat
        from datadog_api_client.v1_20270101.model.table_column_function import TableColumnFunction
        from datadog_api_client.v1_20270101.model.number_reference_table_column_reference import (
            NumberReferenceTableColumnReference,
        )
        from datadog_api_client.v1_20270101.model.number_reference_table_column_type import (
            NumberReferenceTableColumnType,
        )

        return {
            "alias": (str,),
            "comparison": (TableColumnComparison,),
            "format": (NumberBarTableColumnFormat,),
            "functions": ([TableColumnFunction],),
            "is_hidden": (bool,),
            "name": (str,),
            "reference": (NumberReferenceTableColumnReference,),
            "type": (NumberReferenceTableColumnType,),
        }

    attribute_map = {
        "alias": "alias",
        "comparison": "comparison",
        "format": "format",
        "functions": "functions",
        "is_hidden": "is_hidden",
        "name": "name",
        "reference": "reference",
        "type": "type",
    }

    def __init__(
        self_,
        format: NumberBarTableColumnFormat,
        name: str,
        reference: NumberReferenceTableColumnReference,
        type: NumberReferenceTableColumnType,
        alias: Union[str, UnsetType] = unset,
        comparison: Union[
            TableColumnComparison,
            TableColumnComparisonWithSelf,
            TableColumnComparisonWithOtherColumnDiffFrom,
            TableColumnComparisonWithOtherColumnPercentOf,
            TableColumnComparisonWithOtherColumnPercentDiffFrom,
            UnsetType,
        ] = unset,
        functions: Union[List[TableColumnFunction], UnsetType] = unset,
        is_hidden: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param comparison: Test-only generated schema for the dashboard versioning proof of concept.
        :type comparison: TableColumnComparison, optional

        :param format: Test-only generated schema for the dashboard versioning proof of concept.
        :type format: NumberBarTableColumnFormat

        :param functions: Test-only generated schema for the dashboard versioning proof of concept.
        :type functions: [TableColumnFunction], optional

        :param is_hidden: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_hidden: bool, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param reference: Test-only generated schema for the dashboard versioning proof of concept.
        :type reference: NumberReferenceTableColumnReference

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: NumberReferenceTableColumnType
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if comparison is not unset:
            kwargs["comparison"] = comparison
        if functions is not unset:
            kwargs["functions"] = functions
        if is_hidden is not unset:
            kwargs["is_hidden"] = is_hidden
        super().__init__(kwargs)

        self_.format = format
        self_.name = name
        self_.reference = reference
        self_.type = type
