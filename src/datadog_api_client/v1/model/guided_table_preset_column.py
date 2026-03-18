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
    from datadog_api_client.v1.model.guided_table_column_comparison import GuidedTableColumnComparison
    from datadog_api_client.v1.model.guided_table_column_format import GuidedTableColumnFormat
    from datadog_api_client.v1.model.guided_table_column_function import GuidedTableColumnFunction
    from datadog_api_client.v1.model.guided_table_preset_column_preset import GuidedTablePresetColumnPreset
    from datadog_api_client.v1.model.guided_table_preset_column_type import GuidedTablePresetColumnType
    from datadog_api_client.v1.model.guided_table_column_comparison_with_self import GuidedTableColumnComparisonWithSelf
    from datadog_api_client.v1.model.guided_table_column_comparison_with_other_column import (
        GuidedTableColumnComparisonWithOtherColumn,
    )
    from datadog_api_client.v1.model.guided_table_number_bar_column_format import GuidedTableNumberBarColumnFormat
    from datadog_api_client.v1.model.guided_table_trend_column_format import GuidedTableTrendColumnFormat


class GuidedTablePresetColumn(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.guided_table_column_comparison import GuidedTableColumnComparison
        from datadog_api_client.v1.model.guided_table_column_format import GuidedTableColumnFormat
        from datadog_api_client.v1.model.guided_table_column_function import GuidedTableColumnFunction
        from datadog_api_client.v1.model.guided_table_preset_column_preset import GuidedTablePresetColumnPreset
        from datadog_api_client.v1.model.guided_table_preset_column_type import GuidedTablePresetColumnType

        return {
            "alias": (str,),
            "comparison": (GuidedTableColumnComparison,),
            "format": (GuidedTableColumnFormat,),
            "functions": ([GuidedTableColumnFunction],),
            "is_hidden": (bool,),
            "name": (str,),
            "preset": (GuidedTablePresetColumnPreset,),
            "type": (GuidedTablePresetColumnType,),
        }

    attribute_map = {
        "alias": "alias",
        "comparison": "comparison",
        "format": "format",
        "functions": "functions",
        "is_hidden": "is_hidden",
        "name": "name",
        "preset": "preset",
        "type": "type",
    }

    def __init__(
        self_,
        format: Union[GuidedTableColumnFormat, GuidedTableNumberBarColumnFormat, GuidedTableTrendColumnFormat],
        name: str,
        preset: GuidedTablePresetColumnPreset,
        type: GuidedTablePresetColumnType,
        alias: Union[str, UnsetType] = unset,
        comparison: Union[
            GuidedTableColumnComparison,
            GuidedTableColumnComparisonWithSelf,
            GuidedTableColumnComparisonWithOtherColumn,
            UnsetType,
        ] = unset,
        functions: Union[List[GuidedTableColumnFunction], UnsetType] = unset,
        is_hidden: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        A guided table column that displays values for the previous time period based on another column's full query.

        :param alias: Display name shown as the column header.
        :type alias: str, optional

        :param comparison: Comparison to display in a guided table column.
        :type comparison: GuidedTableColumnComparison, optional

        :param format: Visual formatting applied to values in a guided table column. Supports number/bar mode and trend mode.
        :type format: GuidedTableColumnFormat

        :param functions: Functions to apply sequentially to the computed value.
        :type functions: [GuidedTableColumnFunction], optional

        :param is_hidden: Whether this column is hidden in the rendered table.
        :type is_hidden: bool, optional

        :param name: Auto-generated name used to refer to this column.
        :type name: str

        :param preset: Preset configuration.
        :type preset: GuidedTablePresetColumnPreset

        :param type:
        :type type: GuidedTablePresetColumnType
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
        self_.preset = preset
        self_.type = type
