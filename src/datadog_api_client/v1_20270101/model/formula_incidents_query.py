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
    from datadog_api_client.v1_20270101.model.formula_and_function_event_query_definition_compute import (
        FormulaAndFunctionEventQueryDefinitionCompute,
    )
    from datadog_api_client.v1_20270101.model.formula_incidents_query_data_source import FormulaIncidentsQueryDataSource
    from datadog_api_client.v1_20270101.model.formula_and_function_event_query_group_by import (
        FormulaAndFunctionEventQueryGroupBy,
    )
    from datadog_api_client.v1_20270101.model.formula_incidents_query_search import FormulaIncidentsQuerySearch


class FormulaIncidentsQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.formula_and_function_event_query_definition_compute import (
            FormulaAndFunctionEventQueryDefinitionCompute,
        )
        from datadog_api_client.v1_20270101.model.formula_incidents_query_data_source import (
            FormulaIncidentsQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.formula_and_function_event_query_group_by import (
            FormulaAndFunctionEventQueryGroupBy,
        )
        from datadog_api_client.v1_20270101.model.formula_incidents_query_search import FormulaIncidentsQuerySearch

        return {
            "compute": (FormulaAndFunctionEventQueryDefinitionCompute,),
            "data_source": (FormulaIncidentsQueryDataSource,),
            "group_by": ([FormulaAndFunctionEventQueryGroupBy],),
            "indexes": ([str],),
            "name": (str,),
            "search": (FormulaIncidentsQuerySearch,),
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
        data_source: FormulaIncidentsQueryDataSource,
        name: str,
        group_by: Union[List[FormulaAndFunctionEventQueryGroupBy], UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        search: Union[FormulaIncidentsQuerySearch, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: FormulaAndFunctionEventQueryDefinitionCompute

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaIncidentsQueryDataSource

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [FormulaAndFunctionEventQueryGroupBy], optional

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: FormulaIncidentsQuerySearch, optional
        """
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if search is not unset:
            kwargs["search"] = search
        super().__init__(kwargs)

        self_.compute = compute
        self_.data_source = data_source
        self_.name = name
