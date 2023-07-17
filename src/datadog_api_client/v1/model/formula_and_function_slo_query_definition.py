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
    from datadog_api_client.v1.model.formula_and_function_slo_data_source import FormulaAndFunctionSLODataSource
    from datadog_api_client.v1.model.formula_and_function_slo_group_mode import FormulaAndFunctionSLOGroupMode
    from datadog_api_client.v1.model.formula_and_function_slo_measure import FormulaAndFunctionSLOMeasure
    from datadog_api_client.v1.model.formula_and_function_slo_query_type import FormulaAndFunctionSLOQueryType


class FormulaAndFunctionSLOQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.formula_and_function_slo_data_source import FormulaAndFunctionSLODataSource
        from datadog_api_client.v1.model.formula_and_function_slo_group_mode import FormulaAndFunctionSLOGroupMode
        from datadog_api_client.v1.model.formula_and_function_slo_measure import FormulaAndFunctionSLOMeasure
        from datadog_api_client.v1.model.formula_and_function_slo_query_type import FormulaAndFunctionSLOQueryType

        return {
            "additional_query_filters": (str,),
            "data_source": (FormulaAndFunctionSLODataSource,),
            "group_mode": (FormulaAndFunctionSLOGroupMode,),
            "measure": (FormulaAndFunctionSLOMeasure,),
            "name": (str,),
            "slo_id": (str,),
            "slo_query_type": (FormulaAndFunctionSLOQueryType,),
        }

    attribute_map = {
        "additional_query_filters": "additional_query_filters",
        "data_source": "data_source",
        "group_mode": "group_mode",
        "measure": "measure",
        "name": "name",
        "slo_id": "slo_id",
        "slo_query_type": "slo_query_type",
    }

    def __init__(
        self_,
        data_source: FormulaAndFunctionSLODataSource,
        measure: FormulaAndFunctionSLOMeasure,
        slo_id: str,
        additional_query_filters: Union[str, UnsetType] = unset,
        group_mode: Union[FormulaAndFunctionSLOGroupMode, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        slo_query_type: Union[FormulaAndFunctionSLOQueryType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A formula and functions metrics query.

        :param additional_query_filters: Additional filters applied to the SLO query.
        :type additional_query_filters: str, optional

        :param data_source: Data source for SLO measures queries.
        :type data_source: FormulaAndFunctionSLODataSource

        :param group_mode: Group mode to query measures.
        :type group_mode: FormulaAndFunctionSLOGroupMode, optional

        :param measure: SLO measures queries.
        :type measure: FormulaAndFunctionSLOMeasure

        :param name: Name of the query for use in formulas.
        :type name: str, optional

        :param slo_id: ID of an SLO to query measures.
        :type slo_id: str

        :param slo_query_type: Name of the query for use in formulas.
        :type slo_query_type: FormulaAndFunctionSLOQueryType, optional
        """
        if additional_query_filters is not unset:
            kwargs["additional_query_filters"] = additional_query_filters
        if group_mode is not unset:
            kwargs["group_mode"] = group_mode
        if name is not unset:
            kwargs["name"] = name
        if slo_query_type is not unset:
            kwargs["slo_query_type"] = slo_query_type
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.measure = measure
        self_.slo_id = slo_id
