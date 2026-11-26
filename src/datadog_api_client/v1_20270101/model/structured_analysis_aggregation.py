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
    from datadog_api_client.v1_20270101.model.structured_analysis_compute import StructuredAnalysisCompute
    from datadog_api_client.v1_20270101.model.structured_analysis_group_by import StructuredAnalysisGroupBy
    from datadog_api_client.v1_20270101.model.analysis_aggregation_sort import AnalysisAggregationSort
    from datadog_api_client.v1_20270101.model.structured_analysis_time_aggregation import (
        StructuredAnalysisTimeAggregation,
    )
    from datadog_api_client.v1_20270101.model.structured_analysis_aggregation_type import (
        StructuredAnalysisAggregationType,
    )


class StructuredAnalysisAggregation(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.structured_analysis_compute import StructuredAnalysisCompute
        from datadog_api_client.v1_20270101.model.structured_analysis_group_by import StructuredAnalysisGroupBy
        from datadog_api_client.v1_20270101.model.analysis_aggregation_sort import AnalysisAggregationSort
        from datadog_api_client.v1_20270101.model.structured_analysis_time_aggregation import (
            StructuredAnalysisTimeAggregation,
        )
        from datadog_api_client.v1_20270101.model.structured_analysis_aggregation_type import (
            StructuredAnalysisAggregationType,
        )

        return {
            "compute": ([StructuredAnalysisCompute],),
            "group_by": ([StructuredAnalysisGroupBy],),
            "limit": (float,),
            "sort": (AnalysisAggregationSort,),
            "time_aggregation": (StructuredAnalysisTimeAggregation,),
            "type": (StructuredAnalysisAggregationType,),
        }

    attribute_map = {
        "compute": "compute",
        "group_by": "group_by",
        "limit": "limit",
        "sort": "sort",
        "time_aggregation": "time_aggregation",
        "type": "type",
    }

    def __init__(
        self_,
        type: StructuredAnalysisAggregationType,
        compute: Union[List[StructuredAnalysisCompute], UnsetType] = unset,
        group_by: Union[List[StructuredAnalysisGroupBy], UnsetType] = unset,
        limit: Union[float, UnsetType] = unset,
        sort: Union[AnalysisAggregationSort, UnsetType] = unset,
        time_aggregation: Union[StructuredAnalysisTimeAggregation, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: [StructuredAnalysisCompute], optional

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [StructuredAnalysisGroupBy], optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: AnalysisAggregationSort, optional

        :param time_aggregation: Test-only generated schema for the dashboard versioning proof of concept.
        :type time_aggregation: StructuredAnalysisTimeAggregation, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: StructuredAnalysisAggregationType
        """
        if compute is not unset:
            kwargs["compute"] = compute
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if limit is not unset:
            kwargs["limit"] = limit
        if sort is not unset:
            kwargs["sort"] = sort
        if time_aggregation is not unset:
            kwargs["time_aggregation"] = time_aggregation
        super().__init__(kwargs)

        self_.type = type
