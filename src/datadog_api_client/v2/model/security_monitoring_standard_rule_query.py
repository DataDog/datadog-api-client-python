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
    from datadog_api_client.v2.model.security_monitoring_rule_query_aggregation import (
        SecurityMonitoringRuleQueryAggregation,
    )
    from datadog_api_client.v2.model.security_monitoring_standard_data_source import (
        SecurityMonitoringStandardDataSource,
    )


class SecurityMonitoringStandardRuleQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_query_aggregation import (
            SecurityMonitoringRuleQueryAggregation,
        )
        from datadog_api_client.v2.model.security_monitoring_standard_data_source import (
            SecurityMonitoringStandardDataSource,
        )

        return {
            "aggregation": (SecurityMonitoringRuleQueryAggregation,),
            "custom_query_extension": (str,),
            "data_source": (SecurityMonitoringStandardDataSource,),
            "distinct_fields": ([str],),
            "group_by_fields": ([str],),
            "has_optional_group_by_fields": (bool,),
            "metric": (str,),
            "metrics": ([str],),
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "custom_query_extension": "customQueryExtension",
        "data_source": "dataSource",
        "distinct_fields": "distinctFields",
        "group_by_fields": "groupByFields",
        "has_optional_group_by_fields": "hasOptionalGroupByFields",
        "metric": "metric",
        "metrics": "metrics",
        "name": "name",
        "query": "query",
    }
    read_only_vars = {
        "has_optional_group_by_fields",
    }

    def __init__(
        self_,
        aggregation: Union[SecurityMonitoringRuleQueryAggregation, UnsetType] = unset,
        custom_query_extension: Union[str, UnsetType] = unset,
        data_source: Union[SecurityMonitoringStandardDataSource, UnsetType] = unset,
        distinct_fields: Union[List[str], UnsetType] = unset,
        group_by_fields: Union[List[str], UnsetType] = unset,
        has_optional_group_by_fields: Union[bool, UnsetType] = unset,
        metric: Union[str, UnsetType] = unset,
        metrics: Union[List[str], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Query for matching rule.

        :param aggregation: The aggregation type.
        :type aggregation: SecurityMonitoringRuleQueryAggregation, optional

        :param custom_query_extension: Query extension to append to the logs query.
        :type custom_query_extension: str, optional

        :param data_source: Source of events, either logs, audit trail, or Datadog events.
        :type data_source: SecurityMonitoringStandardDataSource, optional

        :param distinct_fields: Field for which the cardinality is measured. Sent as an array.
        :type distinct_fields: [str], optional

        :param group_by_fields: Fields to group by.
        :type group_by_fields: [str], optional

        :param has_optional_group_by_fields: When false, events without a group-by value are ignored by the rule. When true, events with missing group-by fields are processed with ``N/A`` , replacing the missing values.
        :type has_optional_group_by_fields: bool, optional

        :param metric: (Deprecated) The target field to aggregate over when using the sum or max
            aggregations. ``metrics`` field should be used instead. **Deprecated**.
        :type metric: str, optional

        :param metrics: Group of target fields to aggregate over when using the sum, max, geo data, or new value aggregations. The sum, max, and geo data aggregations only accept one value in this list, whereas the new value aggregation accepts up to five values.
        :type metrics: [str], optional

        :param name: Name of the query.
        :type name: str, optional

        :param query: Query to run on logs.
        :type query: str, optional
        """
        if aggregation is not unset:
            kwargs["aggregation"] = aggregation
        if custom_query_extension is not unset:
            kwargs["custom_query_extension"] = custom_query_extension
        if data_source is not unset:
            kwargs["data_source"] = data_source
        if distinct_fields is not unset:
            kwargs["distinct_fields"] = distinct_fields
        if group_by_fields is not unset:
            kwargs["group_by_fields"] = group_by_fields
        if has_optional_group_by_fields is not unset:
            kwargs["has_optional_group_by_fields"] = has_optional_group_by_fields
        if metric is not unset:
            kwargs["metric"] = metric
        if metrics is not unset:
            kwargs["metrics"] = metrics
        if name is not unset:
            kwargs["name"] = name
        if query is not unset:
            kwargs["query"] = query
        super().__init__(kwargs)
