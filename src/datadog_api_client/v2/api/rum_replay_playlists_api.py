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
from datadog_api_client.v2.model.playlist_array import PlaylistArray
from datadog_api_client.v2.model.playlist import Playlist
from datadog_api_client.v2.model.session_id_array import SessionIdArray
from datadog_api_client.v2.model.playlists_session_array import PlaylistsSessionArray
from datadog_api_client.v2.model.playlists_session import PlaylistsSession


class RumReplayPlaylistsApi:
    """
    Create and manage playlists of RUM replay sessions. Organize, categorize, and share collections of replay sessions for analysis and collaboration.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._add_rum_replay_session_to_playlist_endpoint = _Endpoint(
            settings={
                "response_type": (PlaylistsSession,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id}",
                "operation_id": "add_rum_replay_session_to_playlist",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "data_source": {
                    "openapi_types": (str,),
                    "attribute": "data_source",
                    "location": "query",
                },
                "ts": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "ts",
                    "location": "query",
                },
                "playlist_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "playlist_id",
                    "location": "path",
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

        self._bulk_remove_rum_replay_playlist_sessions_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/replay/playlists/{playlist_id}/sessions",
                "operation_id": "bulk_remove_rum_replay_playlist_sessions",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "playlist_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "playlist_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SessionIdArray,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_rum_replay_playlist_endpoint = _Endpoint(
            settings={
                "response_type": (Playlist,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/replay/playlists",
                "operation_id": "create_rum_replay_playlist",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (Playlist,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_rum_replay_playlist_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/replay/playlists/{playlist_id}",
                "operation_id": "delete_rum_replay_playlist",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "playlist_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "playlist_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_rum_replay_playlist_endpoint = _Endpoint(
            settings={
                "response_type": (Playlist,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/replay/playlists/{playlist_id}",
                "operation_id": "get_rum_replay_playlist",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "playlist_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "playlist_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_rum_replay_playlists_endpoint = _Endpoint(
            settings={
                "response_type": (PlaylistArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/replay/playlists",
                "operation_id": "list_rum_replay_playlists",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_created_by_uuid": {
                    "openapi_types": (str,),
                    "attribute": "filter[created_by_uuid]",
                    "location": "query",
                },
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_rum_replay_playlist_sessions_endpoint = _Endpoint(
            settings={
                "response_type": (PlaylistsSessionArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/replay/playlists/{playlist_id}/sessions",
                "operation_id": "list_rum_replay_playlist_sessions",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "playlist_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "playlist_id",
                    "location": "path",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._remove_rum_replay_session_from_playlist_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/replay/playlists/{playlist_id}/sessions/{session_id}",
                "operation_id": "remove_rum_replay_session_from_playlist",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "playlist_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "playlist_id",
                    "location": "path",
                },
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

        self._update_rum_replay_playlist_endpoint = _Endpoint(
            settings={
                "response_type": (Playlist,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/replay/playlists/{playlist_id}",
                "operation_id": "update_rum_replay_playlist",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "playlist_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "playlist_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (Playlist,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def add_rum_replay_session_to_playlist(
        self,
        ts: int,
        playlist_id: int,
        session_id: str,
        *,
        data_source: Union[str, UnsetType] = unset,
    ) -> PlaylistsSession:
        """Add rum replay session to playlist.

        Add a session to a playlist.

        :param ts: Server-side timestamp in milliseconds.
        :type ts: int
        :param playlist_id: Unique identifier of the playlist.
        :type playlist_id: int
        :param session_id: Unique identifier of the session.
        :type session_id: str
        :param data_source: Data source type. Valid values: 'rum' or 'product_analytics'. Defaults to 'rum'.
        :type data_source: str, optional
        :rtype: PlaylistsSession
        """
        kwargs: Dict[str, Any] = {}
        if data_source is not unset:
            kwargs["data_source"] = data_source

        kwargs["ts"] = ts

        kwargs["playlist_id"] = playlist_id

        kwargs["session_id"] = session_id

        return self._add_rum_replay_session_to_playlist_endpoint.call_with_http_info(**kwargs)

    def bulk_remove_rum_replay_playlist_sessions(
        self,
        playlist_id: int,
        body: SessionIdArray,
    ) -> None:
        """Bulk remove rum replay playlist sessions.

        Remove sessions from a playlist.

        :param playlist_id: Unique identifier of the playlist.
        :type playlist_id: int
        :type body: SessionIdArray
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["playlist_id"] = playlist_id

        kwargs["body"] = body

        return self._bulk_remove_rum_replay_playlist_sessions_endpoint.call_with_http_info(**kwargs)

    def create_rum_replay_playlist(
        self,
        body: Playlist,
    ) -> Playlist:
        """Create rum replay playlist.

        Create a playlist.

        :type body: Playlist
        :rtype: Playlist
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_rum_replay_playlist_endpoint.call_with_http_info(**kwargs)

    def delete_rum_replay_playlist(
        self,
        playlist_id: int,
    ) -> None:
        """Delete rum replay playlist.

        Delete a playlist.

        :param playlist_id: Unique identifier of the playlist.
        :type playlist_id: int
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["playlist_id"] = playlist_id

        return self._delete_rum_replay_playlist_endpoint.call_with_http_info(**kwargs)

    def get_rum_replay_playlist(
        self,
        playlist_id: int,
    ) -> Playlist:
        """Get rum replay playlist.

        Get a playlist.

        :param playlist_id: Unique identifier of the playlist.
        :type playlist_id: int
        :rtype: Playlist
        """
        kwargs: Dict[str, Any] = {}
        kwargs["playlist_id"] = playlist_id

        return self._get_rum_replay_playlist_endpoint.call_with_http_info(**kwargs)

    def list_rum_replay_playlists(
        self,
        *,
        filter_created_by_uuid: Union[str, UnsetType] = unset,
        filter_query: Union[str, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
    ) -> PlaylistArray:
        """List rum replay playlists.

        List playlists.

        :param filter_created_by_uuid: Filter playlists by the UUID of the user who created them.
        :type filter_created_by_uuid: str, optional
        :param filter_query: Search query to filter playlists by name.
        :type filter_query: str, optional
        :param page_number: Page number for pagination (0-indexed).
        :type page_number: int, optional
        :param page_size: Number of items per page.
        :type page_size: int, optional
        :rtype: PlaylistArray
        """
        kwargs: Dict[str, Any] = {}
        if filter_created_by_uuid is not unset:
            kwargs["filter_created_by_uuid"] = filter_created_by_uuid

        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        return self._list_rum_replay_playlists_endpoint.call_with_http_info(**kwargs)

    def list_rum_replay_playlist_sessions(
        self,
        playlist_id: int,
        *,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
    ) -> PlaylistsSessionArray:
        """List rum replay playlist sessions.

        List sessions in a playlist.

        :param playlist_id: Unique identifier of the playlist.
        :type playlist_id: int
        :param page_number: Page number for pagination (0-indexed).
        :type page_number: int, optional
        :param page_size: Number of items per page.
        :type page_size: int, optional
        :rtype: PlaylistsSessionArray
        """
        kwargs: Dict[str, Any] = {}
        kwargs["playlist_id"] = playlist_id

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        return self._list_rum_replay_playlist_sessions_endpoint.call_with_http_info(**kwargs)

    def remove_rum_replay_session_from_playlist(
        self,
        playlist_id: int,
        session_id: str,
    ) -> None:
        """Remove rum replay session from playlist.

        Remove a session from a playlist.

        :param playlist_id: Unique identifier of the playlist.
        :type playlist_id: int
        :param session_id: Unique identifier of the session.
        :type session_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["playlist_id"] = playlist_id

        kwargs["session_id"] = session_id

        return self._remove_rum_replay_session_from_playlist_endpoint.call_with_http_info(**kwargs)

    def update_rum_replay_playlist(
        self,
        playlist_id: int,
        body: Playlist,
    ) -> Playlist:
        """Update rum replay playlist.

        Update a playlist.

        :param playlist_id: Unique identifier of the playlist.
        :type playlist_id: int
        :type body: Playlist
        :rtype: Playlist
        """
        kwargs: Dict[str, Any] = {}
        kwargs["playlist_id"] = playlist_id

        kwargs["body"] = body

        return self._update_rum_replay_playlist_endpoint.call_with_http_info(**kwargs)
