# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class TableColumn(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param comparison: Test-only generated schema for the dashboard versioning proof of concept.
        :type comparison: TableColumnComparison, optional

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: ComputeTableColumnCompute

        :param format: Test-only generated schema for the dashboard versioning proof of concept.
        :type format: TableColumnFormat

        :param functions: Test-only generated schema for the dashboard versioning proof of concept.
        :type functions: [TableColumnFunction], optional

        :param is_hidden: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_hidden: bool, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: ComputeTableColumnType

        :param preset: Test-only generated schema for the dashboard versioning proof of concept.
        :type preset: PresetPeriodTableColumnPreset

        :param formula: Test-only generated schema for the dashboard versioning proof of concept.
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
        from datadog_api_client.v1_20270101.model.compute_table_column import ComputeTableColumn
        from datadog_api_client.v1_20270101.model.preset_period_table_column import PresetPeriodTableColumn
        from datadog_api_client.v1_20270101.model.formula_table_column import FormulaTableColumn
        from datadog_api_client.v1_20270101.model.reference_table_column import ReferenceTableColumn

        return {
            "oneOf": [
                ComputeTableColumn,
                PresetPeriodTableColumn,
                FormulaTableColumn,
                ReferenceTableColumn,
            ],
        }
