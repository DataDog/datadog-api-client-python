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
    from datadog_api_client.v1.model.list_stream_compute_items import ListStreamComputeItems
    from datadog_api_client.v1.model.list_stream_source import ListStreamSource
    from datadog_api_client.v1.model.widget_event_size import WidgetEventSize
    from datadog_api_client.v1.model.list_stream_group_by_items import ListStreamGroupByItems
    from datadog_api_client.v1.model.list_stream_issue_persona import ListStreamIssuePersona
    from datadog_api_client.v1.model.widget_field_sort import WidgetFieldSort
    from datadog_api_client.v1.model.list_stream_issue_state import ListStreamIssueState
    from datadog_api_client.v1.model.list_stream_query_version import ListStreamQueryVersion


class ListStreamQuery(ModelNormal):
    validations = {
        "compute": {
            "max_items": 5,
            "min_items": 1,
        },
        "group_by": {
            "max_items": 4,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.list_stream_compute_items import ListStreamComputeItems
        from datadog_api_client.v1.model.list_stream_source import ListStreamSource
        from datadog_api_client.v1.model.widget_event_size import WidgetEventSize
        from datadog_api_client.v1.model.list_stream_group_by_items import ListStreamGroupByItems
        from datadog_api_client.v1.model.list_stream_issue_persona import ListStreamIssuePersona
        from datadog_api_client.v1.model.widget_field_sort import WidgetFieldSort
        from datadog_api_client.v1.model.list_stream_issue_state import ListStreamIssueState
        from datadog_api_client.v1.model.list_stream_query_version import ListStreamQueryVersion

        return {
            "assignee_uuids": ([str],),
            "clustering_pattern_field_path": (str,),
            "compute": ([ListStreamComputeItems],),
            "data_source": (ListStreamSource,),
            "env": (str,),
            "event_size": (WidgetEventSize,),
            "group_by": ([ListStreamGroupByItems],),
            "indexes": ([str],),
            "persona": (ListStreamIssuePersona,),
            "query_string": (str,),
            "recommendation_types": ([str],),
            "services": ([str],),
            "sort": (WidgetFieldSort,),
            "states": ([ListStreamIssueState],),
            "statuses": ([str],),
            "storage": (str,),
            "suspected_causes": ([str],),
            "team_handles": ([str],),
            "teams": ([str],),
            "version": (ListStreamQueryVersion,),
        }

    attribute_map = {
        "assignee_uuids": "assignee_uuids",
        "clustering_pattern_field_path": "clustering_pattern_field_path",
        "compute": "compute",
        "data_source": "data_source",
        "env": "env",
        "event_size": "event_size",
        "group_by": "group_by",
        "indexes": "indexes",
        "persona": "persona",
        "query_string": "query_string",
        "recommendation_types": "recommendation_types",
        "services": "services",
        "sort": "sort",
        "states": "states",
        "statuses": "statuses",
        "storage": "storage",
        "suspected_causes": "suspected_causes",
        "team_handles": "team_handles",
        "teams": "teams",
        "version": "version",
    }

    def __init__(
        self_,
        data_source: ListStreamSource,
        query_string: str,
        assignee_uuids: Union[List[str], UnsetType] = unset,
        clustering_pattern_field_path: Union[str, UnsetType] = unset,
        compute: Union[List[ListStreamComputeItems], UnsetType] = unset,
        env: Union[str, UnsetType] = unset,
        event_size: Union[WidgetEventSize, UnsetType] = unset,
        group_by: Union[List[ListStreamGroupByItems], UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        persona: Union[ListStreamIssuePersona, UnsetType] = unset,
        recommendation_types: Union[List[str], UnsetType] = unset,
        services: Union[List[str], UnsetType] = unset,
        sort: Union[WidgetFieldSort, UnsetType] = unset,
        states: Union[List[ListStreamIssueState], UnsetType] = unset,
        statuses: Union[List[str], UnsetType] = unset,
        storage: Union[str, UnsetType] = unset,
        suspected_causes: Union[List[str], UnsetType] = unset,
        team_handles: Union[List[str], UnsetType] = unset,
        teams: Union[List[str], UnsetType] = unset,
        version: Union[ListStreamQueryVersion, UnsetType] = unset,
        **kwargs,
    ):
        """
        Updated list stream widget.

        :param assignee_uuids: Filter by assignee UUIDs. Usable only with ``issue_stream``.
        :type assignee_uuids: [str], optional

        :param clustering_pattern_field_path: Specifies the field for logs pattern clustering. Usable only with logs_pattern_stream.
        :type clustering_pattern_field_path: str, optional

        :param compute: Compute configuration for the List Stream Widget. Compute can be used only with the logs_transaction_stream (from 1 to 5 items) list stream source.
        :type compute: [ListStreamComputeItems], optional

        :param data_source: Source from which to query items to display in the stream. apm_issue_stream, rum_issue_stream, and logs_issue_stream are deprecated. Use issue_stream instead. apm_recommendations_stream is used to query APM recommendations, and supports filtering by environment, services, teams, recommendation types, and status.
        :type data_source: ListStreamSource

        :param env: Filter by APM environment. Usable only with ``apm_recommendations_stream``.
        :type env: str, optional

        :param event_size: Size to use to display an event.
        :type event_size: WidgetEventSize, optional

        :param group_by: Group by configuration for the List Stream Widget. Group by can be used only with logs_pattern_stream (up to 4 items) or logs_transaction_stream (one group by item is required) list stream source.
        :type group_by: [ListStreamGroupByItems], optional

        :param indexes: List of indexes.
        :type indexes: [str], optional

        :param persona: Persona filter for the ``issue_stream`` data source.
        :type persona: ListStreamIssuePersona, optional

        :param query_string: Widget query.
        :type query_string: str

        :param recommendation_types: Filter by recommendation types. Usable only with ``apm_recommendations_stream``.
        :type recommendation_types: [str], optional

        :param services: Filter by service names. Usable only with ``apm_recommendations_stream``.
        :type services: [str], optional

        :param sort: Which column and order to sort by
        :type sort: WidgetFieldSort, optional

        :param states: Filter by issue states. Usable only with ``issue_stream``.
        :type states: [ListStreamIssueState], optional

        :param statuses: Filter by recommendation statuses. Usable only with ``apm_recommendations_stream``.
        :type statuses: [str], optional

        :param storage: Option for storage location. Feature in Private Beta.
        :type storage: str, optional

        :param suspected_causes: Filter by suspected causes. Usable only with ``issue_stream``.
        :type suspected_causes: [str], optional

        :param team_handles: Filter by team handles. Usable only with ``issue_stream``.
        :type team_handles: [str], optional

        :param teams: Filter by team handles. Usable only with ``apm_recommendations_stream``.
        :type teams: [str], optional

        :param version: Version of the query for the logs transaction stream widget. When omitted, v1 query behavior is
            preserved. Set to ``sequential_query`` to use v2 behavior. **This feature is in Preview.**
        :type version: ListStreamQueryVersion, optional
        """
        if assignee_uuids is not unset:
            kwargs["assignee_uuids"] = assignee_uuids
        if clustering_pattern_field_path is not unset:
            kwargs["clustering_pattern_field_path"] = clustering_pattern_field_path
        if compute is not unset:
            kwargs["compute"] = compute
        if env is not unset:
            kwargs["env"] = env
        if event_size is not unset:
            kwargs["event_size"] = event_size
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if persona is not unset:
            kwargs["persona"] = persona
        if recommendation_types is not unset:
            kwargs["recommendation_types"] = recommendation_types
        if services is not unset:
            kwargs["services"] = services
        if sort is not unset:
            kwargs["sort"] = sort
        if states is not unset:
            kwargs["states"] = states
        if statuses is not unset:
            kwargs["statuses"] = statuses
        if storage is not unset:
            kwargs["storage"] = storage
        if suspected_causes is not unset:
            kwargs["suspected_causes"] = suspected_causes
        if team_handles is not unset:
            kwargs["team_handles"] = team_handles
        if teams is not unset:
            kwargs["teams"] = teams
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query_string = query_string
