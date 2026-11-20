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
    from datadog_api_client.v1_20270101.model.formula_graph_query_compute import FormulaGraphQueryCompute
    from datadog_api_client.v1_20270101.model.formula_graph_query_data_source import FormulaGraphQueryDataSource
    from datadog_api_client.v1_20270101.model.formula_graph_query_group_by_items import FormulaGraphQueryGroupByItems
    from datadog_api_client.v1_20270101.model.graph_query_search import GraphQuerySearch
    from datadog_api_client.v1_20270101.model.formula_semantic_mode import FormulaSemanticMode
    from datadog_api_client.v1_20270101.model.storage_type import StorageType


class FormulaGraphQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.formula_graph_query_compute import FormulaGraphQueryCompute
        from datadog_api_client.v1_20270101.model.formula_graph_query_data_source import FormulaGraphQueryDataSource
        from datadog_api_client.v1_20270101.model.formula_graph_query_group_by_items import (
            FormulaGraphQueryGroupByItems,
        )
        from datadog_api_client.v1_20270101.model.graph_query_search import GraphQuerySearch
        from datadog_api_client.v1_20270101.model.formula_semantic_mode import FormulaSemanticMode
        from datadog_api_client.v1_20270101.model.storage_type import StorageType

        return {
            "compute": (FormulaGraphQueryCompute,),
            "data_source": (FormulaGraphQueryDataSource,),
            "group_by": ([FormulaGraphQueryGroupByItems],),
            "name": (str,),
            "search": (GraphQuerySearch,),
            "semantic_mode": (FormulaSemanticMode,),
            "storage": (StorageType,),
        }

    attribute_map = {
        "compute": "compute",
        "data_source": "data_source",
        "group_by": "group_by",
        "name": "name",
        "search": "search",
        "semantic_mode": "semantic_mode",
        "storage": "storage",
    }

    def __init__(
        self_,
        compute: FormulaGraphQueryCompute,
        data_source: FormulaGraphQueryDataSource,
        name: str,
        search: GraphQuerySearch,
        group_by: Union[List[FormulaGraphQueryGroupByItems], UnsetType] = unset,
        semantic_mode: Union[FormulaSemanticMode, UnsetType] = unset,
        storage: Union[StorageType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: FormulaGraphQueryCompute

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaGraphQueryDataSource

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [FormulaGraphQueryGroupByItems], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: GraphQuerySearch

        :param semantic_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type semantic_mode: FormulaSemanticMode, optional

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional
        """
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if semantic_mode is not unset:
            kwargs["semantic_mode"] = semantic_mode
        if storage is not unset:
            kwargs["storage"] = storage
        super().__init__(kwargs)

        self_.compute = compute
        self_.data_source = data_source
        self_.name = name
        self_.search = search
