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
    from datadog_api_client.v1_20270101.model.formula_dataset_data_source import FormulaDatasetDataSource
    from datadog_api_client.v1_20270101.model.formula_dataset_formulas_items import FormulaDatasetFormulasItems
    from datadog_api_client.v1_20270101.model.dashboard_inline_schema40 import DashboardInlineSchema40
    from datadog_api_client.v1_20270101.model.formula_dataset_response_format import FormulaDatasetResponseFormat
    from datadog_api_client.v1_20270101.model.time_window import TimeWindow
    from datadog_api_client.v1_20270101.model.formula_dataset_metric_query import FormulaDatasetMetricQuery
    from datadog_api_client.v1_20270101.model.formula_dataset_apm_metrics_query import FormulaDatasetApmMetricsQuery


class FormulaDataset(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.formula_dataset_data_source import FormulaDatasetDataSource
        from datadog_api_client.v1_20270101.model.formula_dataset_formulas_items import FormulaDatasetFormulasItems
        from datadog_api_client.v1_20270101.model.dashboard_inline_schema40 import DashboardInlineSchema40
        from datadog_api_client.v1_20270101.model.formula_dataset_response_format import FormulaDatasetResponseFormat
        from datadog_api_client.v1_20270101.model.time_window import TimeWindow

        return {
            "data_source": (FormulaDatasetDataSource,),
            "formulas": ([FormulaDatasetFormulasItems],),
            "name": (str,),
            "queries": ([DashboardInlineSchema40],),
            "response_format": (FormulaDatasetResponseFormat,),
            "time_window": (TimeWindow,),
        }

    attribute_map = {
        "data_source": "data_source",
        "formulas": "formulas",
        "name": "name",
        "queries": "queries",
        "response_format": "response_format",
        "time_window": "time_window",
    }

    def __init__(
        self_,
        data_source: FormulaDatasetDataSource,
        formulas: List[FormulaDatasetFormulasItems],
        name: str,
        queries: List[Union[DashboardInlineSchema40, FormulaDatasetMetricQuery, FormulaDatasetApmMetricsQuery]],
        response_format: FormulaDatasetResponseFormat,
        time_window: Union[TimeWindow, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaDatasetDataSource

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [FormulaDatasetFormulasItems]

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [DashboardInlineSchema40]

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: FormulaDatasetResponseFormat

        :param time_window: Test-only generated schema for the dashboard versioning proof of concept.
        :type time_window: TimeWindow, optional
        """
        if time_window is not unset:
            kwargs["time_window"] = time_window
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.formulas = formulas
        self_.name = name
        self_.queries = queries
        self_.response_format = response_format
