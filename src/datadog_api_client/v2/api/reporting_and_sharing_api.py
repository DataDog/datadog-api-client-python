# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.create_snapshot_response import CreateSnapshotResponse
from datadog_api_client.v2.model.create_snapshot_request import CreateSnapshotRequest


class ReportingAndSharingApi:
    """
    The Reporting and Sharing endpoints allow you to create snapshots of graph widgets and other shareable resources.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_snapshot_endpoint = _Endpoint(
            settings={
                "response_type": (CreateSnapshotResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/snapshot",
                "operation_id": "create_snapshot",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateSnapshotRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_snapshot(
        self,
        body: CreateSnapshotRequest,
    ) -> CreateSnapshotResponse:
        """Create a graph snapshot.

        Create a snapshot of a graph widget. The snapshot is rendered asynchronously; the returned URL can be polled until the image is ready.

        :type body: CreateSnapshotRequest
        :rtype: CreateSnapshotResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_snapshot_endpoint.call_with_http_info(**kwargs)
