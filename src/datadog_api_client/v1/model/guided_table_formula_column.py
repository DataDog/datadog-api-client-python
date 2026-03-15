# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.guided_table_column_comparison import GuidedTableColumnComparison
    from datadog_api_client.v1.model.guided_table_column_format import GuidedTableColumnFormat
    from datadog_api_client.v1.model.formula_type import FormulaType
    from datadog_api_client.v1.model.guided_table_column_comparison_with_self import GuidedTableColumnComparisonWithSelf
    from datadog_api_client.v1.model.guided_table_column_comparison_with_other_column import (
        GuidedTableColumnComparisonWithOtherColumn,
    )
    from datadog_api_client.v1.model.guided_table_number_bar_column_format import GuidedTableNumberBarColumnFormat
    from datadog_api_client.v1.model.guided_table_trend_column_format import GuidedTableTrendColumnFormat


class GuidedTableFormulaColumn(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.guided_table_column_comparison import GuidedTableColumnComparison
        from datadog_api_client.v1.model.guided_table_column_format import GuidedTableColumnFormat
        from datadog_api_client.v1.model.formula_type import FormulaType

        return {
            "alias": (str,),
            "comparison": (GuidedTableColumnComparison,),
            "format": (GuidedTableColumnFormat,),
            "formula": (str,),
            "is_hidden": (bool,),
            "name": (str,),
            "type": (FormulaType,),
        }

    attribute_map = {
        "alias": "alias",
        "comparison": "comparison",
        "format": "format",
        "formula": "formula",
        "is_hidden": "is_hidden",
        "name": "name",
        "type": "type",
    }

    def __init__(
        self_,
        format: Union[GuidedTableColumnFormat, GuidedTableNumberBarColumnFormat, GuidedTableTrendColumnFormat],
        formula: str,
        name: str,
        type: FormulaType,
        alias: Union[str, UnsetType] = unset,
        comparison: Union[
            GuidedTableColumnComparison,
            GuidedTableColumnComparisonWithSelf,
            GuidedTableColumnComparisonWithOtherColumn,
            UnsetType,
        ] = unset,
        is_hidden: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        A guided table column that displays the result of evaluating a formula over other columns.

        :param alias: Display name shown as the column header.
        :type alias: str, optional

        :param comparison: Comparison to display in a guided table column.
        :type comparison: GuidedTableColumnComparison, optional

        :param format: Visual formatting applied to values in a guided table column. Supports number/bar mode and trend mode.
        :type format: GuidedTableColumnFormat

        :param formula: The formula expression to evaluate.
        :type formula: str

        :param is_hidden: Whether this column is hidden in the rendered table.
        :type is_hidden: bool, optional

        :param name: Auto-generated name used to refer to this column.
        :type name: str

        :param type: Set the sort type to formula.
        :type type: FormulaType
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if comparison is not unset:
            kwargs["comparison"] = comparison
        if is_hidden is not unset:
            kwargs["is_hidden"] = is_hidden
        super().__init__(kwargs)

        self_.format = format
        self_.formula = formula
        self_.name = name
        self_.type = type
