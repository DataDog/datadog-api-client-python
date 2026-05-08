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
from datadog_api_client.v2.model.replay_summary_response import ReplaySummaryResponse
from datadog_api_client.v2.model.replay_summary_request import ReplaySummaryRequest


class RumReplayApi:
    """
    Generate and retrieve AI-powered summaries of RUM replay sessions.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._generate_replay_summary_endpoint = _Endpoint(
            settings={
                "response_type": (ReplaySummaryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/replay/summary/{session_id}",
                "operation_id": "generate_replay_summary",
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
                "data_source": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "data_source",
                    "location": "query",
                },
                "ts": {
                    "openapi_types": (int,),
                    "attribute": "ts",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ReplaySummaryRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def generate_replay_summary(
        self,
        session_id: str,
        data_source: str,
        body: ReplaySummaryRequest,
        *,
        ts: Union[int, UnsetType] = unset,
    ) -> ReplaySummaryResponse:
        """Generate replay summary.

        Generate an AI-powered summary for a RUM replay session, including chapter breakdowns and behavioral analysis.

        :param session_id: Unique identifier of the session.
        :type session_id: str
        :param data_source: Data source for the session. Valid values are ``rum`` , ``product_analytics`` , and ``replay``.
        :type data_source: str
        :type body: ReplaySummaryRequest
        :param ts: Server-side timestamp in milliseconds.
        :type ts: int, optional
        :rtype: ReplaySummaryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["session_id"] = session_id

        kwargs["data_source"] = data_source

        if ts is not unset:
            kwargs["ts"] = ts

        kwargs["body"] = body

        return self._generate_replay_summary_endpoint.call_with_http_info(**kwargs)
