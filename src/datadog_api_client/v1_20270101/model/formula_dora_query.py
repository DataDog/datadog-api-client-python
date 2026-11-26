# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.formula_and_function_event_query_definition_compute import (
        FormulaAndFunctionEventQueryDefinitionCompute,
    )
    from datadog_api_client.v1_20270101.model.formula_dora_query_data_source import FormulaDoraQueryDataSource
    from datadog_api_client.v1_20270101.model.formula_and_function_event_query_group_by import (
        FormulaAndFunctionEventQueryGroupBy,
    )
    from datadog_api_client.v1_20270101.model.formula_dora_query_search import FormulaDoraQuerySearch


class FormulaDoraQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.formula_and_function_event_query_definition_compute import (
            FormulaAndFunctionEventQueryDefinitionCompute,
        )
        from datadog_api_client.v1_20270101.model.formula_dora_query_data_source import FormulaDoraQueryDataSource
        from datadog_api_client.v1_20270101.model.formula_and_function_event_query_group_by import (
            FormulaAndFunctionEventQueryGroupBy,
        )
        from datadog_api_client.v1_20270101.model.formula_dora_query_search import FormulaDoraQuerySearch

        return {
            "compute": (FormulaAndFunctionEventQueryDefinitionCompute,),
            "data_source": (FormulaDoraQueryDataSource,),
            "group_by": ([FormulaAndFunctionEventQueryGroupBy],),
            "indexes": ([bool, date, datetime, dict, float, int, list, str, UUID, none_type],),
            "name": (str,),
            "search": (FormulaDoraQuerySearch,),
        }

    attribute_map = {
        "compute": "compute",
        "data_source": "data_source",
        "group_by": "group_by",
        "indexes": "indexes",
        "name": "name",
        "search": "search",
    }

    def __init__(
        self_,
        compute: FormulaAndFunctionEventQueryDefinitionCompute,
        data_source: FormulaDoraQueryDataSource,
        indexes: List[Any],
        name: str,
        group_by: Union[List[FormulaAndFunctionEventQueryGroupBy], UnsetType] = unset,
        search: Union[FormulaDoraQuerySearch, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: FormulaAndFunctionEventQueryDefinitionCompute

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaDoraQueryDataSource

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [FormulaAndFunctionEventQueryGroupBy], optional

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [bool, date, datetime, dict, float, int, list, str, UUID, none_type]

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: FormulaDoraQuerySearch, optional
        """
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if search is not unset:
            kwargs["search"] = search
        super().__init__(kwargs)

        self_.compute = compute
        self_.data_source = data_source
        self_.indexes = indexes
        self_.name = name
