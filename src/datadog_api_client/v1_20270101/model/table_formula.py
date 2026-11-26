# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class TableFormula(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param cell_display_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type cell_display_mode: TableFormulaAnyOfAnyOfItemCellDisplayMode, optional

        :param cell_display_mode_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type cell_display_mode_options: dict, optional

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: ConditionalFormats, optional

        :param formula: Test-only generated schema for the dashboard versioning proof of concept.
        :type formula: str

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: TableFormulaAnyOfAnyOfItemLimit, optional

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: WidgetFormulaStyle, optional
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
        from datadog_api_client.v1_20270101.model.table_formula20270101_one_of import TableFormula20270101OneOf
        from datadog_api_client.v1_20270101.model.table_formula20270101_one_of4462669760 import (
            TableFormula20270101OneOf4462669760,
        )

        return {
            "oneOf": [
                TableFormula20270101OneOf,
                TableFormula20270101OneOf4462669760,
            ],
        }
