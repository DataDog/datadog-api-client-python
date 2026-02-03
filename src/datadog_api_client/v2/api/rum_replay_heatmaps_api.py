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
from datadog_api_client.v2.model.snapshot_array import SnapshotArray
from datadog_api_client.v2.model.snapshot import Snapshot
from datadog_api_client.v2.model.snapshot_create_request import SnapshotCreateRequest
from datadog_api_client.v2.model.snapshot_update_request import SnapshotUpdateRequest


class RumReplayHeatmapsApi:
    """
    Manage heatmap snapshots for RUM replay sessions. Create, update, delete, and retrieve snapshots to visualize user interactions on specific views.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_replay_heatmap_snapshot_endpoint = _Endpoint(
            settings={
                "response_type": (Snapshot,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/replay/heatmap/snapshots",
                "operation_id": "create_replay_heatmap_snapshot",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SnapshotCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_replay_heatmap_snapshot_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/replay/heatmap/snapshots/{snapshot_id}",
                "operation_id": "delete_replay_heatmap_snapshot",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "snapshot_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "snapshot_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._list_replay_heatmap_snapshots_endpoint = _Endpoint(
            settings={
                "response_type": (SnapshotArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/replay/heatmap/snapshots",
                "operation_id": "list_replay_heatmap_snapshots",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_device_type": {
                    "openapi_types": (str,),
                    "attribute": "filter[device_type]",
                    "location": "query",
                },
                "filter_view_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "filter[view_name]",
                    "location": "query",
                },
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
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

        self._update_replay_heatmap_snapshot_endpoint = _Endpoint(
            settings={
                "response_type": (Snapshot,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/replay/heatmap/snapshots/{snapshot_id}",
                "operation_id": "update_replay_heatmap_snapshot",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "snapshot_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "snapshot_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SnapshotUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_replay_heatmap_snapshot(
        self,
        body: SnapshotCreateRequest,
    ) -> Snapshot:
        """Create replay heatmap snapshot.

        Create a heatmap snapshot.

        :type body: SnapshotCreateRequest
        :rtype: Snapshot
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_replay_heatmap_snapshot_endpoint.call_with_http_info(**kwargs)

    def delete_replay_heatmap_snapshot(
        self,
        snapshot_id: str,
    ) -> None:
        """Delete replay heatmap snapshot.

        Delete a heatmap snapshot.

        :param snapshot_id: Unique identifier of the heatmap snapshot.
        :type snapshot_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["snapshot_id"] = snapshot_id

        return self._delete_replay_heatmap_snapshot_endpoint.call_with_http_info(**kwargs)

    def list_replay_heatmap_snapshots(
        self,
        filter_view_name: str,
        *,
        filter_device_type: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        filter_application_id: Union[str, UnsetType] = unset,
    ) -> SnapshotArray:
        """List replay heatmap snapshots.

        List heatmap snapshots.

        :param filter_view_name: View name to filter snapshots.
        :type filter_view_name: str
        :param filter_device_type: Device type to filter snapshots.
        :type filter_device_type: str, optional
        :param page_limit: Maximum number of snapshots to return.
        :type page_limit: int, optional
        :param filter_application_id: Filter by application ID.
        :type filter_application_id: str, optional
        :rtype: SnapshotArray
        """
        kwargs: Dict[str, Any] = {}
        if filter_device_type is not unset:
            kwargs["filter_device_type"] = filter_device_type

        kwargs["filter_view_name"] = filter_view_name

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if filter_application_id is not unset:
            kwargs["filter_application_id"] = filter_application_id

        return self._list_replay_heatmap_snapshots_endpoint.call_with_http_info(**kwargs)

    def update_replay_heatmap_snapshot(
        self,
        snapshot_id: str,
        body: SnapshotUpdateRequest,
    ) -> Snapshot:
        """Update replay heatmap snapshot.

        Update a heatmap snapshot.

        :param snapshot_id: Unique identifier of the heatmap snapshot.
        :type snapshot_id: str
        :type body: SnapshotUpdateRequest
        :rtype: Snapshot
        """
        kwargs: Dict[str, Any] = {}
        kwargs["snapshot_id"] = snapshot_id

        kwargs["body"] = body

        return self._update_replay_heatmap_snapshot_endpoint.call_with_http_info(**kwargs)
