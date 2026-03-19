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
    from datadog_api_client.v1.model.formula_and_function_apm_metrics_data_source import (
        FormulaAndFunctionApmMetricsDataSource,
    )
    from datadog_api_client.v1.model.formula_and_function_apm_metrics_span_kind import (
        FormulaAndFunctionApmMetricsSpanKind,
    )
    from datadog_api_client.v1.model.formula_and_function_apm_metric_stat_name import (
        FormulaAndFunctionApmMetricStatName,
    )


class FormulaAndFunctionApmMetricsQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.formula_and_function_apm_metrics_data_source import (
            FormulaAndFunctionApmMetricsDataSource,
        )
        from datadog_api_client.v1.model.formula_and_function_apm_metrics_span_kind import (
            FormulaAndFunctionApmMetricsSpanKind,
        )
        from datadog_api_client.v1.model.formula_and_function_apm_metric_stat_name import (
            FormulaAndFunctionApmMetricStatName,
        )

        return {
            "data_source": (FormulaAndFunctionApmMetricsDataSource,),
            "group_by": ([str],),
            "name": (str,),
            "operation_mode": (str,),
            "operation_name": (str,),
            "peer_tags": ([str],),
            "query_filter": (str,),
            "resource_hash": (str,),
            "resource_name": (str,),
            "service": (str,),
            "span_kind": (FormulaAndFunctionApmMetricsSpanKind,),
            "stat": (FormulaAndFunctionApmMetricStatName,),
        }

    attribute_map = {
        "data_source": "data_source",
        "group_by": "group_by",
        "name": "name",
        "operation_mode": "operation_mode",
        "operation_name": "operation_name",
        "peer_tags": "peer_tags",
        "query_filter": "query_filter",
        "resource_hash": "resource_hash",
        "resource_name": "resource_name",
        "service": "service",
        "span_kind": "span_kind",
        "stat": "stat",
    }

    def __init__(
        self_,
        data_source: FormulaAndFunctionApmMetricsDataSource,
        name: str,
        stat: FormulaAndFunctionApmMetricStatName,
        group_by: Union[List[str], UnsetType] = unset,
        operation_mode: Union[str, UnsetType] = unset,
        operation_name: Union[str, UnsetType] = unset,
        peer_tags: Union[List[str], UnsetType] = unset,
        query_filter: Union[str, UnsetType] = unset,
        resource_hash: Union[str, UnsetType] = unset,
        resource_name: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        span_kind: Union[FormulaAndFunctionApmMetricsSpanKind, UnsetType] = unset,
        **kwargs,
    ):
        """
        A formula and functions APM metrics query.

        :param data_source: Data source for APM metrics queries.
        :type data_source: FormulaAndFunctionApmMetricsDataSource

        :param group_by: Optional fields to group the query results by.
        :type group_by: [str], optional

        :param name: Name of this query to use in formulas.
        :type name: str

        :param operation_mode: Optional operation mode to aggregate across operation names.
        :type operation_mode: str, optional

        :param operation_name: Name of operation on service. If not provided, the primary operation name is used.
        :type operation_name: str, optional

        :param peer_tags: Tags to query for a specific downstream entity (peer.service, peer.db_instance, peer.s3, peer.s3.bucket, etc.).
        :type peer_tags: [str], optional

        :param query_filter: Additional filters for the query using metrics query syntax (e.g., env, primary_tag).
        :type query_filter: str, optional

        :param resource_hash: The hash of a specific resource to filter by.
        :type resource_hash: str, optional

        :param resource_name: The full name of a specific resource to filter by.
        :type resource_name: str, optional

        :param service: APM service name.
        :type service: str, optional

        :param span_kind: Describes the relationship between the span, its parents, and its children in a trace.
        :type span_kind: FormulaAndFunctionApmMetricsSpanKind, optional

        :param stat: APM metric stat name.
        :type stat: FormulaAndFunctionApmMetricStatName
        """
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
        if service is not unset:
            kwargs["service"] = service
        if span_kind is not unset:
            kwargs["span_kind"] = span_kind
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.stat = stat
