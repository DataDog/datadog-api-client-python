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


class HistoricalJobQuery(ModelNormal):
    validations = {
        "correlated_query_index": {
            "inclusive_maximum": 9,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_query_aggregation import (
            SecurityMonitoringRuleQueryAggregation,
        )
        from datadog_api_client.v2.model.security_monitoring_standard_data_source import (
            SecurityMonitoringStandardDataSource,
        )

        return {
            "additional_filters": (str,),
            "aggregation": (SecurityMonitoringRuleQueryAggregation,),
            "correlated_by_fields": ([str],),
            "correlated_query_index": (int,),
            "custom_query_extension": (str,),
            "data_source": (SecurityMonitoringStandardDataSource,),
            "dataset_ids": ([str],),
            "distinct_fields": ([str],),
            "group_by_fields": ([str],),
            "has_optional_group_by_fields": (bool,),
            "index": (str,),
            "indexes": ([str],),
            "metrics": ([str],),
            "name": (str,),
            "query": (str,),
            "query_language": (str,),
        }

    attribute_map = {
        "additional_filters": "additionalFilters",
        "aggregation": "aggregation",
        "correlated_by_fields": "correlatedByFields",
        "correlated_query_index": "correlatedQueryIndex",
        "custom_query_extension": "customQueryExtension",
        "data_source": "dataSource",
        "dataset_ids": "datasetIds",
        "distinct_fields": "distinctFields",
        "group_by_fields": "groupByFields",
        "has_optional_group_by_fields": "hasOptionalGroupByFields",
        "index": "index",
        "indexes": "indexes",
        "metrics": "metrics",
        "name": "name",
        "query": "query",
        "query_language": "queryLanguage",
    }

    def __init__(
        self_,
        additional_filters: Union[str, UnsetType] = unset,
        aggregation: Union[SecurityMonitoringRuleQueryAggregation, UnsetType] = unset,
        correlated_by_fields: Union[List[str], UnsetType] = unset,
        correlated_query_index: Union[int, UnsetType] = unset,
        custom_query_extension: Union[str, UnsetType] = unset,
        data_source: Union[SecurityMonitoringStandardDataSource, UnsetType] = unset,
        dataset_ids: Union[List[str], UnsetType] = unset,
        distinct_fields: Union[List[str], UnsetType] = unset,
        group_by_fields: Union[List[str], UnsetType] = unset,
        has_optional_group_by_fields: Union[bool, UnsetType] = unset,
        index: Union[str, UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        metrics: Union[List[str], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        query_language: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Query for selecting logs analyzed by the historical job.

        :param additional_filters: Additional filters appended to the query at evaluation time.
        :type additional_filters: str, optional

        :param aggregation: The aggregation type.
        :type aggregation: SecurityMonitoringRuleQueryAggregation, optional

        :param correlated_by_fields: Fields used to correlate results across queries in sequence detection rules.
        :type correlated_by_fields: [str], optional

        :param correlated_query_index: Zero-based index of the query to correlate with in sequence detection rules. Up to 10 queries are supported, so valid values are 0 to 9.
        :type correlated_query_index: int, optional

        :param custom_query_extension: Custom query extension used to refine the base query.
        :type custom_query_extension: str, optional

        :param data_source: Source of events, either logs, audit trail, security signals, or Datadog events. ``app_sec_spans`` is deprecated in favor of ``spans``.
        :type data_source: SecurityMonitoringStandardDataSource, optional

        :param dataset_ids: IDs of reference datasets used by this query.
        :type dataset_ids: [str], optional

        :param distinct_fields: Field for which the cardinality is measured. Sent as an array.
        :type distinct_fields: [str], optional

        :param group_by_fields: Fields to group by.
        :type group_by_fields: [str], optional

        :param has_optional_group_by_fields: When false, events without a group-by value are ignored by the query. When true, events with missing group-by fields are processed with ``N/A`` , replacing the missing values.
        :type has_optional_group_by_fields: bool, optional

        :param index: Index used to load the data for this query.
        :type index: str, optional

        :param indexes: Indexes used to load the data for this query. Mutually exclusive with ``index``.
        :type indexes: [str], optional

        :param metrics: Group of target fields to aggregate over when using the sum, max, geo data, or new value aggregations. The sum, max, and geo data aggregations only accept one value in this list, whereas the new value aggregation accepts up to five values.
        :type metrics: [str], optional

        :param name: Name of the query.
        :type name: str, optional

        :param query: Query to run on logs.
        :type query: str, optional

        :param query_language: Language used to parse the query string.
        :type query_language: str, optional
        """
        if additional_filters is not unset:
            kwargs["additional_filters"] = additional_filters
        if aggregation is not unset:
            kwargs["aggregation"] = aggregation
        if correlated_by_fields is not unset:
            kwargs["correlated_by_fields"] = correlated_by_fields
        if correlated_query_index is not unset:
            kwargs["correlated_query_index"] = correlated_query_index
        if custom_query_extension is not unset:
            kwargs["custom_query_extension"] = custom_query_extension
        if data_source is not unset:
            kwargs["data_source"] = data_source
        if dataset_ids is not unset:
            kwargs["dataset_ids"] = dataset_ids
        if distinct_fields is not unset:
            kwargs["distinct_fields"] = distinct_fields
        if group_by_fields is not unset:
            kwargs["group_by_fields"] = group_by_fields
        if has_optional_group_by_fields is not unset:
            kwargs["has_optional_group_by_fields"] = has_optional_group_by_fields
        if index is not unset:
            kwargs["index"] = index
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if metrics is not unset:
            kwargs["metrics"] = metrics
        if name is not unset:
            kwargs["name"] = name
        if query is not unset:
            kwargs["query"] = query
        if query_language is not unset:
            kwargs["query_language"] = query_language
        super().__init__(kwargs)
