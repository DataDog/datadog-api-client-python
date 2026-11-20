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
    from datadog_api_client.v1_20270101.model.formula_apm_metrics_query_data_source import (
        FormulaApmMetricsQueryDataSource,
    )
    from datadog_api_client.v1_20270101.model.formula_semantic_mode import FormulaSemanticMode
    from datadog_api_client.v1_20270101.model.span_kind import SpanKind
    from datadog_api_client.v1_20270101.model.apm_metric_stat import ApmMetricStat


class FormulaApmMetricsQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.formula_apm_metrics_query_data_source import (
            FormulaApmMetricsQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.formula_semantic_mode import FormulaSemanticMode
        from datadog_api_client.v1_20270101.model.span_kind import SpanKind
        from datadog_api_client.v1_20270101.model.apm_metric_stat import ApmMetricStat

        return {
            "byoc_cluster": (str,),
            "data_source": (FormulaApmMetricsQueryDataSource,),
            "group_by": ([str],),
            "name": (str,),
            "operation_mode": (str,),
            "operation_name": (str,),
            "peer_tags": ([str],),
            "query_filter": (str,),
            "resource_hash": (str,),
            "resource_name": (str,),
            "semantic_mode": (FormulaSemanticMode,),
            "service": (str,),
            "span_kind": (SpanKind,),
            "stat": (ApmMetricStat,),
        }

    attribute_map = {
        "byoc_cluster": "byoc_cluster",
        "data_source": "data_source",
        "group_by": "group_by",
        "name": "name",
        "operation_mode": "operation_mode",
        "operation_name": "operation_name",
        "peer_tags": "peer_tags",
        "query_filter": "query_filter",
        "resource_hash": "resource_hash",
        "resource_name": "resource_name",
        "semantic_mode": "semantic_mode",
        "service": "service",
        "span_kind": "span_kind",
        "stat": "stat",
    }

    def __init__(
        self_,
        data_source: FormulaApmMetricsQueryDataSource,
        name: str,
        stat: ApmMetricStat,
        byoc_cluster: Union[str, UnsetType] = unset,
        group_by: Union[List[str], UnsetType] = unset,
        operation_mode: Union[str, UnsetType] = unset,
        operation_name: Union[str, UnsetType] = unset,
        peer_tags: Union[List[str], UnsetType] = unset,
        query_filter: Union[str, UnsetType] = unset,
        resource_hash: Union[str, UnsetType] = unset,
        resource_name: Union[str, UnsetType] = unset,
        semantic_mode: Union[FormulaSemanticMode, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        span_kind: Union[SpanKind, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param byoc_cluster: Test-only generated schema for the dashboard versioning proof of concept.
        :type byoc_cluster: str, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaApmMetricsQueryDataSource

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [str], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param operation_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type operation_mode: str, optional

        :param operation_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type operation_name: str, optional

        :param peer_tags: Test-only generated schema for the dashboard versioning proof of concept.
        :type peer_tags: [str], optional

        :param query_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_filter: str, optional

        :param resource_hash: Test-only generated schema for the dashboard versioning proof of concept.
        :type resource_hash: str, optional

        :param resource_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type resource_name: str, optional

        :param semantic_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type semantic_mode: FormulaSemanticMode, optional

        :param service: Test-only generated schema for the dashboard versioning proof of concept.
        :type service: str, optional

        :param span_kind: Test-only generated schema for the dashboard versioning proof of concept.
        :type span_kind: SpanKind, optional

        :param stat: Test-only generated schema for the dashboard versioning proof of concept.
        :type stat: ApmMetricStat
        """
        if byoc_cluster is not unset:
            kwargs["byoc_cluster"] = byoc_cluster
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if operation_mode is not unset:
            kwargs["operation_mode"] = operation_mode
        if operation_name is not unset:
            kwargs["operation_name"] = operation_name
        if peer_tags is not unset:
            kwargs["peer_tags"] = peer_tags
        if query_filter is not unset:
            kwargs["query_filter"] = query_filter
        if resource_hash is not unset:
            kwargs["resource_hash"] = resource_hash
        if resource_name is not unset:
            kwargs["resource_name"] = resource_name
        if semantic_mode is not unset:
            kwargs["semantic_mode"] = semantic_mode
        if service is not unset:
            kwargs["service"] = service
        if span_kind is not unset:
            kwargs["span_kind"] = span_kind
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.stat = stat
