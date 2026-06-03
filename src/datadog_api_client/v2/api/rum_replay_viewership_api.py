# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.watcher_array import WatcherArray
from datadog_api_client.v2.model.watch import Watch
from datadog_api_client.v2.model.viewership_history_session_array import ViewershipHistorySessionArray


class RumReplayViewershipApi:
    """
    Track and manage RUM replay session viewership. Monitor who watches replay sessions and maintain watch history for audit and analytics purposes.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_rum_replay_session_watch_endpoint = _Endpoint(
            settings={
                "response_type": (Watch,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/replay/sessions/{session_id}/watches",
                "operation_id": "create_rum_replay_session_watch",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "session_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "session_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (Watch,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_rum_replay_session_watch_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/replay/sessions/{session_id}/watches",
                "operation_id": "delete_rum_replay_session_watch",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "session_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "session_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._list_rum_replay_session_watchers_endpoint = _Endpoint(
            settings={
                "response_type": (WatcherArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/replay/sessions/{session_id}/watchers",
                "operation_id": "list_rum_replay_session_watchers",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "session_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "session_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_rum_replay_viewership_history_sessions_endpoint = _Endpoint(
            settings={
                "response_type": (ViewershipHistorySessionArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/replay/viewership-history/sessions",
                "operation_id": "list_rum_replay_viewership_history_sessions",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_watched_at_start": {
                    "openapi_types": (int,),
                    "attribute": "filter[watched_at][start]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "filter_created_by": {
                    "openapi_types": (str,),
                    "attribute": "filter[created_by]",
                    "location": "query",
                },
                "filter_watched_at_end": {
                    "openapi_types": (int,),
                    "attribute": "filter[watched_at][end]",
                    "location": "query",
                },
                "filter_session_ids": {
                    "openapi_types": (str,),
                    "attribute": "filter[session_ids]",
                    "location": "query",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "filter_application_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[application_id]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def create_rum_replay_session_watch(
        self,
        session_id: str,
        body: Watch,
    ) -> Watch:
        """Create rum replay session watch.

        Record a session watch.

        :param session_id: Unique identifier of the session.
        :type session_id: str
        :type body: Watch
        :rtype: Watch
        """
        kwargs: Dict[str, Any] = {}
        kwargs["session_id"] = session_id

        kwargs["body"] = body

        return self._create_rum_replay_session_watch_endpoint.call_with_http_info(**kwargs)

    def delete_rum_replay_session_watch(
        self,
        session_id: str,
    ) -> None:
        """Delete rum replay session watch.

        Delete session watch history.

        :param session_id: Unique identifier of the session.
        :type session_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["session_id"] = session_id

        return self._delete_rum_replay_session_watch_endpoint.call_with_http_info(**kwargs)

    def list_rum_replay_session_watchers(
        self,
        session_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> WatcherArray:
        """List rum replay session watchers.

        List session watchers.

        :param session_id: Unique identifier of the session.
        :type session_id: str
        :param page_size: Number of items per page.
        :type page_size: int, optional
        :param page_number: Page number for pagination (0-indexed).
        :type page_number: int, optional
        :rtype: WatcherArray
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        kwargs["session_id"] = session_id

        return self._list_rum_replay_session_watchers_endpoint.call_with_http_info(**kwargs)

    def list_rum_replay_viewership_history_sessions(
        self,
        *,
        filter_watched_at_start: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        filter_created_by: Union[str, UnsetType] = unset,
        filter_watched_at_end: Union[int, UnsetType] = unset,
        filter_session_ids: Union[str, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        filter_application_id: Union[str, UnsetType] = unset,
    ) -> ViewershipHistorySessionArray:
        """List rum replay viewership history sessions.

        List watched sessions.

        :param filter_watched_at_start: Start timestamp in milliseconds for watched_at filter.
        :type filter_watched_at_start: int, optional
        :param page_number: Page number for pagination (0-indexed).
        :type page_number: int, optional
        :param filter_created_by: Filter by user UUID. Defaults to current user if not specified.
        :type filter_created_by: str, optional
        :param filter_watched_at_end: End timestamp in milliseconds for watched_at filter.
        :type filter_watched_at_end: int, optional
        :param filter_session_ids: Comma-separated list of session IDs to filter by.
        :type filter_session_ids: str, optional
        :param page_size: Number of items per page.
        :type page_size: int, optional
        :param filter_application_id: Filter by application ID.
        :type filter_application_id: str, optional
        :rtype: ViewershipHistorySessionArray
        """
        kwargs: Dict[str, Any] = {}
        if filter_watched_at_start is not unset:
            kwargs["filter_watched_at_start"] = filter_watched_at_start

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if filter_created_by is not unset:
            kwargs["filter_created_by"] = filter_created_by

        if filter_watched_at_end is not unset:
            kwargs["filter_watched_at_end"] = filter_watched_at_end

        if filter_session_ids is not unset:
            kwargs["filter_session_ids"] = filter_session_ids

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if filter_application_id is not unset:
            kwargs["filter_application_id"] = filter_application_id

        return self._list_rum_replay_viewership_history_sessions_endpoint.call_with_http_info(**kwargs)
