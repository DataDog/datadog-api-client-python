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


class RumReplaySessionsApi:
    """
    Retrieve segments for RUM replay sessions. Access session replay data stored in event platform or blob storage.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_segments_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/replay/sessions/{session_id}/views/{view_id}/segments",
                "operation_id": "get_segments",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "view_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "view_id",
                    "location": "path",
                },
                "source": {
                    "openapi_types": (str,),
                    "attribute": "source",
                    "location": "query",
                },
                "session_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "session_id",
                    "location": "path",
                },
                "ts": {
                    "openapi_types": (int,),
                    "attribute": "ts",
                    "location": "query",
                },
                "max_list_size": {
                    "openapi_types": (int,),
                    "attribute": "max_list_size",
                    "location": "query",
                },
                "paging": {
                    "openapi_types": (str,),
                    "attribute": "paging",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

    def get_segments(
        self,
        view_id: str,
        session_id: str,
        *,
        source: Union[str, UnsetType] = unset,
        ts: Union[int, UnsetType] = unset,
        max_list_size: Union[int, UnsetType] = unset,
        paging: Union[str, UnsetType] = unset,
    ) -> None:
        """Get segments.

        Get segments for a view.

        :param view_id: Unique identifier of the view.
        :type view_id: str
        :param session_id: Unique identifier of the session.
        :type session_id: str
        :param source: Storage source: 'event_platform' or 'blob'.
        :type source: str, optional
        :param ts: Server-side timestamp in milliseconds.
        :type ts: int, optional
        :param max_list_size: Maximum size in bytes for the segment list.
        :type max_list_size: int, optional
        :param paging: Paging token for pagination.
        :type paging: str, optional
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["view_id"] = view_id

        if source is not unset:
            kwargs["source"] = source

        kwargs["session_id"] = session_id

        if ts is not unset:
            kwargs["ts"] = ts

        if max_list_size is not unset:
            kwargs["max_list_size"] = max_list_size

        if paging is not unset:
            kwargs["paging"] = paging

        return self._get_segments_endpoint.call_with_http_info(**kwargs)
