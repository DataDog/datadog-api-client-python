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
    UUID,
)
from datadog_api_client.v2.model.rum_recovery_count_response import RumRecoveryCountResponse
from datadog_api_client.v2.model.rum_recovery_count_request import RumRecoveryCountRequest
from datadog_api_client.v2.model.rum_recovery_batch_list_response import RumRecoveryBatchListResponse
from datadog_api_client.v2.model.rum_recovery_batch_request_type import RumRecoveryBatchRequestType
from datadog_api_client.v2.model.rum_recovery_create_response import RumRecoveryCreateResponse
from datadog_api_client.v2.model.rum_recovery_create_request import RumRecoveryCreateRequest
from datadog_api_client.v2.model.rum_recovery_request_response import RumRecoveryRequestResponse
from datadog_api_client.v2.model.rum_recovery_cancel_response import RumRecoveryCancelResponse
from datadog_api_client.v2.model.rum_recovery_cancel_request import RumRecoveryCancelRequest
from datadog_api_client.v2.model.rum_archive_sessions_response import RumArchiveSessionsResponse
from datadog_api_client.v2.model.rum_archive_sessions_search_request import RumArchiveSessionsSearchRequest


class RUMRecoveryApi:
    """
    Search archived RUM sessions and recover individual sessions or query-based batches. Your organization must have Managed Archives enabled. Creating, counting, listing, and canceling batches also require batch recovery enablement.

    Requires ``rum_rehydration_filter_read`` for search and request details, or ``rum_rehydration_index`` to create, estimate recoverable sessions, list batches, or cancel recovery requests.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_rum_recovery_request_endpoint = _Endpoint(
            settings={
                "response_type": (RumRecoveryCreateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/recover/requests",
                "operation_id": "create_rum_recovery_request",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RumRecoveryCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_rum_recovery_request_endpoint = _Endpoint(
            settings={
                "response_type": (RumRecoveryRequestResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/recover/requests/{request_id}",
                "operation_id": "get_rum_recovery_request",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "request_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "request_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_rum_recovery_session_count_endpoint = _Endpoint(
            settings={
                "response_type": (RumRecoveryCountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/recover/count",
                "operation_id": "get_rum_recovery_session_count",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RumRecoveryCountRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_rum_recovery_batch_requests_endpoint = _Endpoint(
            settings={
                "response_type": (RumRecoveryBatchListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/recover/requests",
                "operation_id": "list_rum_recovery_batch_requests",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "type": {
                    "required": True,
                    "openapi_types": (RumRecoveryBatchRequestType,),
                    "attribute": "type",
                    "location": "query",
                },
                "limit": {
                    "validation": {
                        "inclusive_maximum": 100,
                    },
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
                "cursor": {
                    "openapi_types": (str,),
                    "attribute": "cursor",
                    "location": "query",
                },
                "_from": {
                    "validation": {
                        "inclusive_maximum": 253402300799999,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "from",
                    "location": "query",
                },
                "to": {
                    "validation": {
                        "inclusive_maximum": 253402300799999,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "to",
                    "location": "query",
                },
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._search_rum_archive_sessions_endpoint = _Endpoint(
            settings={
                "response_type": (RumArchiveSessionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/recover/sessions",
                "operation_id": "search_rum_archive_sessions",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RumArchiveSessionsSearchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_rum_recovery_batch_request_endpoint = _Endpoint(
            settings={
                "response_type": (RumRecoveryCancelResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/recover/requests/{request_id}",
                "operation_id": "update_rum_recovery_batch_request",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "request_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "request_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RumRecoveryCancelRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_rum_recovery_request(
        self,
        body: RumRecoveryCreateRequest,
    ) -> RumRecoveryCreateResponse:
        """Create a recovery request.

        Start targeted or query-based batch recovery. Use the returned ``data.id`` to poll the recovery request for progress. Batch creation checks a fresh recoverable-session estimate against the configured maximum (100,000 by default), accepting estimates equal to the maximum. Use the count operation to check the current maximum; creation can still reject a changed estimate. Narrow the query or time range if the maximum is exceeded.

        Creation is not idempotent. After an uncertain response, check session search or batch listing before retrying.

        :param body: JSON:API request body.
        :type body: RumRecoveryCreateRequest
        :rtype: RumRecoveryCreateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_rum_recovery_request_endpoint.call_with_http_info(**kwargs)

    def get_rum_recovery_request(
        self,
        request_id: UUID,
    ) -> RumRecoveryRequestResponse:
        """Get recovery request progress.

        Get progress for a targeted or batch recovery request. A ``COMPLETED`` request can include failed sessions; check individual session statuses for targeted recovery.

        :param request_id: Recovery request UUID.
        :type request_id: UUID
        :rtype: RumRecoveryRequestResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["request_id"] = request_id

        return self._get_rum_recovery_request_endpoint.call_with_http_info(**kwargs)

    def get_rum_recovery_session_count(
        self,
        body: RumRecoveryCountRequest,
    ) -> RumRecoveryCountResponse:
        """Estimate recoverable sessions.

        Return the full estimated number of recoverable sessions and the configured maximum per batch. The estimate is not capped at that maximum. This endpoint does not create a recovery request. Narrow the query or time range if the estimate exceeds max_recoverable_sessions. Creation checks a fresh estimate and returns 400 if it exceeds the configured maximum.

        :param body: JSON:API request body.
        :type body: RumRecoveryCountRequest
        :rtype: RumRecoveryCountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._get_rum_recovery_session_count_endpoint.call_with_http_info(**kwargs)

    def list_rum_recovery_batch_requests(
        self,
        type: RumRecoveryBatchRequestType,
        *,
        limit: Union[int, UnsetType] = unset,
        cursor: Union[str, UnsetType] = unset,
        _from: Union[int, UnsetType] = unset,
        to: Union[int, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
    ) -> RumRecoveryBatchListResponse:
        """List batch recovery requests.

        List batch recovery requests for your organization. Set ``type=batch``. Optional ``from`` and ``to`` bounds filter request creation time; ``query`` filters the queries stored on recovery requests.
        A filtered page can be empty or contain fewer than ``limit`` results and still include ``meta.next_cursor``. Continue until the cursor is absent, keeping the filters unchanged between pages.

        :param type: Must equal batch.
        :type type: RumRecoveryBatchRequestType
        :param limit: Number of results returned per page, at most 100 (default 50). Omitted, zero, or negative values use 50. Invalid integers return 400.
        :type limit: int, optional
        :param cursor: Opaque next-page cursor. Keep type, from, to, and query unchanged between pages.
        :type cursor: str, optional
        :param _from: Start of the request creation-time range in Unix milliseconds, inclusive. This filters created_at, not the time range of the sessions being recovered. Must be earlier than to when both are provided.
        :type _from: int, optional
        :param to: End of the request creation-time range in Unix milliseconds, exclusive. This filters created_at, not the time range of the sessions being recovered. Must be later than from when both are provided.
        :type to: int, optional
        :param query: Filter recovery requests whose stored query selects matching facet values. Supports facet:value and facet:(A OR B) terms combined with AND, including * and ? wildcards in filter values. Attribute facets keep their leading @. At most 4096 bytes. Exclusions, repeated facets, free text, ranges, and OR between terms return 400. Stored queries that cannot be matched unambiguously are excluded. Blank values apply no query filter.
        :type query: str, optional
        :rtype: RumRecoveryBatchListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["type"] = type

        if limit is not unset:
            kwargs["limit"] = limit

        if cursor is not unset:
            kwargs["cursor"] = cursor

        if _from is not unset:
            kwargs["_from"] = _from

        if to is not unset:
            kwargs["to"] = to

        if query is not unset:
            kwargs["query"] = query

        return self._list_rum_recovery_batch_requests_endpoint.call_with_http_info(**kwargs)

    def search_rum_archive_sessions(
        self,
        body: RumArchiveSessionsSearchRequest,
    ) -> RumArchiveSessionsResponse:
        """Search archived sessions.

        Search archived RUM sessions. Use ``meta.page.next_cursor`` to retrieve the next page.

        :param body: JSON:API request body.
        :type body: RumArchiveSessionsSearchRequest
        :rtype: RumArchiveSessionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._search_rum_archive_sessions_endpoint.call_with_http_info(**kwargs)

    def update_rum_recovery_batch_request(
        self,
        request_id: UUID,
        body: RumRecoveryCancelRequest,
    ) -> RumRecoveryCancelResponse:
        """Cancel a batch recovery request.

        Cancel pending work for a batch recovery request. Work already in progress can finish, and recovered data is not removed. Requests in a terminal state return ``409``.

        :param request_id: Recovery request UUID.
        :type request_id: UUID
        :param body: JSON:API request body.
        :type body: RumRecoveryCancelRequest
        :rtype: RumRecoveryCancelResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["request_id"] = request_id

        kwargs["body"] = body

        return self._update_rum_recovery_batch_request_endpoint.call_with_http_info(**kwargs)
