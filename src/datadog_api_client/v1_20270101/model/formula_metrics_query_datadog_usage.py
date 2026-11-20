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
    from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator
    from datadog_api_client.v1_20270101.model.formula_metrics_query_datadog_usage_data_source import (
        FormulaMetricsQueryDatadogUsageDataSource,
    )
    from datadog_api_client.v1_20270101.model.formula_semantic_mode import FormulaSemanticMode


class FormulaMetricsQueryDatadogUsage(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator
        from datadog_api_client.v1_20270101.model.formula_metrics_query_datadog_usage_data_source import (
            FormulaMetricsQueryDatadogUsageDataSource,
        )
        from datadog_api_client.v1_20270101.model.formula_semantic_mode import FormulaSemanticMode

        return {
            "aggregator": (ScalarAggregator,),
            "byoc_cluster": (str,),
            "cross_org_uuids": ([str],),
            "data_source": (FormulaMetricsQueryDatadogUsageDataSource,),
            "name": (str,),
            "query": (str,),
            "semantic_mode": (FormulaSemanticMode,),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "byoc_cluster": "byoc_cluster",
        "cross_org_uuids": "cross_org_uuids",
        "data_source": "data_source",
        "name": "name",
        "query": "query",
        "semantic_mode": "semantic_mode",
    }

    def __init__(
        self_,
        data_source: FormulaMetricsQueryDatadogUsageDataSource,
        name: str,
        query: str,
        aggregator: Union[ScalarAggregator, UnsetType] = unset,
        byoc_cluster: Union[str, UnsetType] = unset,
        cross_org_uuids: Union[List[str], UnsetType] = unset,
        semantic_mode: Union[FormulaSemanticMode, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregator: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregator: ScalarAggregator, optional

        :param byoc_cluster: Test-only generated schema for the dashboard versioning proof of concept.
        :type byoc_cluster: str, optional

        :param cross_org_uuids: Test-only generated schema for the dashboard versioning proof of concept.
        :type cross_org_uuids: [str], optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaMetricsQueryDatadogUsageDataSource

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: str

        :param semantic_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type semantic_mode: FormulaSemanticMode, optional
        """
        if aggregator is not unset:
            kwargs["aggregator"] = aggregator
        if byoc_cluster is not unset:
            kwargs["byoc_cluster"] = byoc_cluster
        if cross_org_uuids is not unset:
            kwargs["cross_org_uuids"] = cross_org_uuids
        if semantic_mode is not unset:
            kwargs["semantic_mode"] = semantic_mode
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.query = query
