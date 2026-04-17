# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class TimeseriesQuery(ModelComposed):
    def __init__(self, **kwargs):
        """
        An individual timeseries query to one of the basic Datadog data sources.

        :param data_source: A data source that is powered by the Metrics platform.
        :type data_source: MetricsDataSource

        :param name: The variable name for use in formulas.
        :type name: str, optional

        :param query: A classic metrics query string.
        :type query: str

        :param compute: The instructions for what to compute for this query.
        :type compute: EventsCompute

        :param group_by: The list of facets on which to split results.
        :type group_by: EventsQueryGroupBys, optional

        :param indexes: The indexes in which to search.
        :type indexes: [str], optional

        :param search: Configuration of the search/filter for an events query.
        :type search: EventsSearch, optional

        :param env: The environment to query.
        :type env: str

        :param operation_name: The APM operation name.
        :type operation_name: str, optional

        :param primary_tag_name: Name of the second primary tag used within APM. Required when `primary_tag_value` is specified. See https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog
        :type primary_tag_name: str, optional

        :param primary_tag_value: Value of the second primary tag by which to filter APM data. `primary_tag_name` must also be specified.
        :type primary_tag_value: str, optional

        :param resource_name: The resource name to filter by.
        :type resource_name: str, optional

        :param service: The service name to filter by.
        :type service: str

        :param stat: The APM resource statistic to query.
        :type stat: ApmResourceStatName

        :param operation_mode: Optional operation mode to aggregate across operation names.
        :type operation_mode: str, optional

        :param peer_tags: Tags to query for a specific downstream entity (peer.service, peer.db_instance, peer.s3, peer.s3.bucket, etc.).
        :type peer_tags: [str], optional

        :param query_filter: Additional filters for the query using metrics query syntax (for example, env, primary_tag).
        :type query_filter: str, optional

        :param resource_hash: The resource hash for exact matching.
        :type resource_hash: str, optional

        :param span_kind: Describes the relationship between the span, its parents, and its children in a trace.
        :type span_kind: ApmMetricsSpanKind, optional

        :param is_upstream: Determines whether stats for upstream or downstream dependencies should be queried.
        :type is_upstream: bool, optional

        :param additional_query_filters: Additional filters applied to the SLO query.
        :type additional_query_filters: str, optional

        :param group_mode: How SLO results are grouped in the response.
        :type group_mode: SlosGroupMode, optional

        :param measure: The SLO measurement to retrieve.
        :type measure: SlosMeasure

        :param slo_id: The unique identifier of the SLO to query.
        :type slo_id: str

        :param slo_query_type: The type of SLO definition being queried.
        :type slo_query_type: SlosQueryType, optional

        :param is_normalized_cpu: Whether CPU metrics should be normalized by core count.
        :type is_normalized_cpu: bool, optional

        :param limit: Maximum number of results to return.
        :type limit: int, optional

        :param metric: The process metric to query.
        :type metric: str

        :param sort: Direction of sort.
        :type sort: QuerySortOrder, optional

        :param tag_filters: Tag filters to narrow down processes.
        :type tag_filters: [str], optional

        :param text_filter: A full-text search filter to match process names or commands.
        :type text_filter: str, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.metrics_timeseries_query import MetricsTimeseriesQuery
        from datadog_api_client.v2.model.events_timeseries_query import EventsTimeseriesQuery
        from datadog_api_client.v2.model.apm_resource_stats_query import ApmResourceStatsQuery
        from datadog_api_client.v2.model.apm_metrics_query import ApmMetricsQuery
        from datadog_api_client.v2.model.apm_dependency_stats_query import ApmDependencyStatsQuery
        from datadog_api_client.v2.model.slo_query import SloQuery
        from datadog_api_client.v2.model.process_timeseries_query import ProcessTimeseriesQuery
        from datadog_api_client.v2.model.container_timeseries_query import ContainerTimeseriesQuery

        return {
            "oneOf": [
                MetricsTimeseriesQuery,
                EventsTimeseriesQuery,
                ApmResourceStatsQuery,
                ApmMetricsQuery,
                ApmDependencyStatsQuery,
                SloQuery,
                ProcessTimeseriesQuery,
                ContainerTimeseriesQuery,
            ],
        }
