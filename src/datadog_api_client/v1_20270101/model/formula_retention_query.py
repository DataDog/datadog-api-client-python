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
    from datadog_api_client.v1_20270101.model.computation_scope import ComputationScope
    from datadog_api_client.v1_20270101.model.retention_compute import RetentionCompute
    from datadog_api_client.v1_20270101.model.formula_retention_query_data_source import FormulaRetentionQueryDataSource
    from datadog_api_client.v1_20270101.model.retention_group_by_items import RetentionGroupByItems
    from datadog_api_client.v1_20270101.model.formula_retention_query_sampling import FormulaRetentionQuerySampling
    from datadog_api_client.v1_20270101.model.retention_search import RetentionSearch
    from datadog_api_client.v1_20270101.model.cohort_scope import CohortScope
    from datadog_api_client.v1_20270101.model.return_period_scope import ReturnPeriodScope
    from datadog_api_client.v1_20270101.model.cell_scope import CellScope


class FormulaRetentionQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.computation_scope import ComputationScope
        from datadog_api_client.v1_20270101.model.retention_compute import RetentionCompute
        from datadog_api_client.v1_20270101.model.formula_retention_query_data_source import (
            FormulaRetentionQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.retention_group_by_items import RetentionGroupByItems
        from datadog_api_client.v1_20270101.model.formula_retention_query_sampling import FormulaRetentionQuerySampling
        from datadog_api_client.v1_20270101.model.retention_search import RetentionSearch

        return {
            "computation_scope": (ComputationScope,),
            "compute": (RetentionCompute,),
            "data_source": (FormulaRetentionQueryDataSource,),
            "exclude_anonymous_traffic": (bool,),
            "group_by": ([RetentionGroupByItems],),
            "name": (str,),
            "sampling": (FormulaRetentionQuerySampling,),
            "search": (RetentionSearch,),
        }

    attribute_map = {
        "computation_scope": "computation_scope",
        "compute": "compute",
        "data_source": "data_source",
        "exclude_anonymous_traffic": "exclude_anonymous_traffic",
        "group_by": "group_by",
        "name": "name",
        "sampling": "sampling",
        "search": "search",
    }

    def __init__(
        self_,
        compute: RetentionCompute,
        data_source: FormulaRetentionQueryDataSource,
        name: str,
        search: RetentionSearch,
        computation_scope: Union[ComputationScope, CohortScope, ReturnPeriodScope, CellScope, UnsetType] = unset,
        exclude_anonymous_traffic: Union[bool, UnsetType] = unset,
        group_by: Union[List[RetentionGroupByItems], UnsetType] = unset,
        sampling: Union[FormulaRetentionQuerySampling, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param computation_scope: Test-only generated schema for the dashboard versioning proof of concept.
        :type computation_scope: ComputationScope, optional

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: RetentionCompute

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaRetentionQueryDataSource

        :param exclude_anonymous_traffic: Test-only generated schema for the dashboard versioning proof of concept.
        :type exclude_anonymous_traffic: bool, optional

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [RetentionGroupByItems], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param sampling: Test-only generated schema for the dashboard versioning proof of concept.
        :type sampling: FormulaRetentionQuerySampling, optional

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: RetentionSearch
        """
        if computation_scope is not unset:
            kwargs["computation_scope"] = computation_scope
        if exclude_anonymous_traffic is not unset:
            kwargs["exclude_anonymous_traffic"] = exclude_anonymous_traffic
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if sampling is not unset:
            kwargs["sampling"] = sampling
        super().__init__(kwargs)

        self_.compute = compute
        self_.data_source = data_source
        self_.name = name
        self_.search = search
