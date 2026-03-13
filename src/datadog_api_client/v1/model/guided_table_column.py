# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class GuidedTableColumn(ModelComposed):
    def __init__(self, **kwargs):
        """
        Definition of a single column in a guided table widget. A column can be a computed value, a preset comparison, or a formula.

        :param alias: Display name shown as the column header.
        :type alias: str, optional

        :param comparison: Comparison to display in a guided table column.
        :type comparison: GuidedTableColumnComparison, optional

        :param compute: Aggregation configuration.
        :type compute: GuidedTableComputeColumnCompute

        :param format: Visual formatting applied to values in a guided table column. Supports number/bar mode and trend mode.
        :type format: GuidedTableColumnFormat

        :param functions: Functions to apply sequentially to the computed value.
        :type functions: [GuidedTableColumnFunction], optional

        :param is_hidden: Whether this column is hidden in the rendered table.
        :type is_hidden: bool, optional

        :param name: Auto-generated name used to refer to this column.
        :type name: str

        :param type:
        :type type: GuidedTableComputeColumnType

        :param preset: Preset configuration.
        :type preset: GuidedTablePresetColumnPreset

        :param formula: The formula expression to evaluate.
        :type formula: str
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1.model.guided_table_compute_column import GuidedTableComputeColumn
        from datadog_api_client.v1.model.guided_table_preset_column import GuidedTablePresetColumn
        from datadog_api_client.v1.model.guided_table_formula_column import GuidedTableFormulaColumn

        return {
            "oneOf": [
                GuidedTableComputeColumn,
                GuidedTablePresetColumn,
                GuidedTableFormulaColumn,
            ],
        }
