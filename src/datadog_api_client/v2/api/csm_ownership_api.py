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
from datadog_api_client.v2.model.ownership_inference_list_response import OwnershipInferenceListResponse
from datadog_api_client.v2.model.ownership_history_response import OwnershipHistoryResponse
from datadog_api_client.v2.model.ownership_inference_response import OwnershipInferenceResponse
from datadog_api_client.v2.model.ownership_owner_type import OwnershipOwnerType
from datadog_api_client.v2.model.ownership_evidence_response import OwnershipEvidenceResponse
from datadog_api_client.v2.model.ownership_feedback_response import OwnershipFeedbackResponse
from datadog_api_client.v2.model.ownership_feedback_request import OwnershipFeedbackRequest


class CSMOwnershipApi:
    """
    Datadog Cloud Security Management (CSM) Ownership infers the most likely owner
    for a cloud resource by combining ownership signals from across the platform,
    and lets you review the inference, inspect its evidence, and submit feedback to
    persist, override, or correct the inferred owner.
    For more information, see `Cloud Security Management <https://docs.datadoghq.com/security/cloud_security_management>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_ownership_feedback_endpoint = _Endpoint(
            settings={
                "response_type": (OwnershipFeedbackResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/ownership/{resource_id}/{owner_type}/feedback",
                "operation_id": "create_ownership_feedback",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "resource_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "resource_id",
                    "location": "path",
                },
                "owner_type": {
                    "required": True,
                    "openapi_types": (OwnershipOwnerType,),
                    "attribute": "owner_type",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (OwnershipFeedbackRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_ownership_evidence_endpoint = _Endpoint(
            settings={
                "response_type": (OwnershipEvidenceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/ownership/{resource_id}/{owner_type}/evidence",
                "operation_id": "get_ownership_evidence",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "resource_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "resource_id",
                    "location": "path",
                },
                "owner_type": {
                    "required": True,
                    "openapi_types": (OwnershipOwnerType,),
                    "attribute": "owner_type",
                    "location": "path",
                },
                "if_none_match": {
                    "openapi_types": (str,),
                    "attribute": "If-None-Match",
                    "location": "header",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_ownership_inference_endpoint = _Endpoint(
            settings={
                "response_type": (OwnershipInferenceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/ownership/{resource_id}/{owner_type}",
                "operation_id": "get_ownership_inference",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "resource_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "resource_id",
                    "location": "path",
                },
                "owner_type": {
                    "required": True,
                    "openapi_types": (OwnershipOwnerType,),
                    "attribute": "owner_type",
                    "location": "path",
                },
                "if_none_match": {
                    "openapi_types": (str,),
                    "attribute": "If-None-Match",
                    "location": "header",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ownership_history_endpoint = _Endpoint(
            settings={
                "response_type": (OwnershipHistoryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/ownership/{resource_id}/history",
                "operation_id": "list_ownership_history",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "resource_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "resource_id",
                    "location": "path",
                },
                "cursor": {
                    "openapi_types": (str,),
                    "attribute": "cursor",
                    "location": "query",
                },
                "limit": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ownership_history_by_owner_type_endpoint = _Endpoint(
            settings={
                "response_type": (OwnershipHistoryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/ownership/{resource_id}/{owner_type}/history",
                "operation_id": "list_ownership_history_by_owner_type",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "resource_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "resource_id",
                    "location": "path",
                },
                "owner_type": {
                    "required": True,
                    "openapi_types": (OwnershipOwnerType,),
                    "attribute": "owner_type",
                    "location": "path",
                },
                "cursor": {
                    "openapi_types": (str,),
                    "attribute": "cursor",
                    "location": "query",
                },
                "limit": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ownership_inferences_endpoint = _Endpoint(
            settings={
                "response_type": (OwnershipInferenceListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/ownership/{resource_id}",
                "operation_id": "list_ownership_inferences",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "resource_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "resource_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def create_ownership_feedback(
        self,
        resource_id: str,
        owner_type: OwnershipOwnerType,
        body: OwnershipFeedbackRequest,
    ) -> OwnershipFeedbackResponse:
        """Submit feedback on an ownership inference.

        Submit feedback on the current ownership inference for a resource and owner type. Valid actions are ``confirm`` , ``reject`` , ``correct`` , and ``persist``.

        The request must include the current inference ``checksum`` in ``inference_checksum``. If the checksum does not match the current inference state, the endpoint returns ``409 Conflict``.

        When ``action`` is ``correct`` , ``corrected_owner_handle`` and ``corrected_owner_type`` are required.

        :param resource_id: The identifier of the resource that the feedback applies to.
        :type resource_id: str
        :param owner_type: The type of owner that the feedback applies to.
        :type owner_type: OwnershipOwnerType
        :type body: OwnershipFeedbackRequest
        :rtype: OwnershipFeedbackResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["resource_id"] = resource_id

        kwargs["owner_type"] = owner_type

        kwargs["body"] = body

        return self._create_ownership_feedback_endpoint.call_with_http_info(**kwargs)

    def get_ownership_evidence(
        self,
        resource_id: str,
        owner_type: OwnershipOwnerType,
        *,
        if_none_match: Union[str, UnsetType] = unset,
    ) -> OwnershipEvidenceResponse:
        """Get the evidence for an ownership inference.

        Get the evidence versions backing the current ownership inference for a resource and owner type.

        This endpoint supports weak ETag caching. Pass the previously returned ``ETag`` value in the ``If-None-Match`` request header to receive a ``304 Not Modified`` response when the evidence has not changed.

        :param resource_id: The identifier of the resource to retrieve evidence for.
        :type resource_id: str
        :param owner_type: The owner type of the inference to retrieve evidence for.
        :type owner_type: OwnershipOwnerType
        :param if_none_match: A previously returned weak ``ETag`` value. When supplied and the evidence has not changed, the endpoint returns ``304 Not Modified``.
        :type if_none_match: str, optional
        :rtype: OwnershipEvidenceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["resource_id"] = resource_id

        kwargs["owner_type"] = owner_type

        if if_none_match is not unset:
            kwargs["if_none_match"] = if_none_match

        return self._get_ownership_evidence_endpoint.call_with_http_info(**kwargs)

    def get_ownership_inference(
        self,
        resource_id: str,
        owner_type: OwnershipOwnerType,
        *,
        if_none_match: Union[str, UnsetType] = unset,
    ) -> OwnershipInferenceResponse:
        """Get an ownership inference by owner type.

        Get the current ownership inference for a resource for a specific owner type.

        This endpoint supports ETag-based caching. Pass the previously returned ``ETag`` value in the ``If-None-Match`` request header to receive a ``304 Not Modified`` response when the inference has not changed.

        :param resource_id: The identifier of the resource to retrieve the ownership inference for.
        :type resource_id: str
        :param owner_type: The owner type of the inference to retrieve.
        :type owner_type: OwnershipOwnerType
        :param if_none_match: A previously returned ``ETag`` value. When supplied and the resource has not changed, the endpoint returns ``304 Not Modified``.
        :type if_none_match: str, optional
        :rtype: OwnershipInferenceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["resource_id"] = resource_id

        kwargs["owner_type"] = owner_type

        if if_none_match is not unset:
            kwargs["if_none_match"] = if_none_match

        return self._get_ownership_inference_endpoint.call_with_http_info(**kwargs)

    def list_ownership_history(
        self,
        resource_id: str,
        *,
        cursor: Union[str, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
    ) -> OwnershipHistoryResponse:
        """List ownership inference history for a resource.

        List inference history entries for a resource across all owner types, ordered from most recent to oldest. Uses cursor-based pagination.

        :param resource_id: The identifier of the resource to retrieve inference history for.
        :type resource_id: str
        :param cursor: An opaque, base64-encoded cursor token returned by a previous call in ``pagination.next_cursor``. Omit to fetch the first page.
        :type cursor: str, optional
        :param limit: The maximum number of history entries to return per page.
        :type limit: int, optional
        :rtype: OwnershipHistoryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["resource_id"] = resource_id

        if cursor is not unset:
            kwargs["cursor"] = cursor

        if limit is not unset:
            kwargs["limit"] = limit

        return self._list_ownership_history_endpoint.call_with_http_info(**kwargs)

    def list_ownership_history_by_owner_type(
        self,
        resource_id: str,
        owner_type: OwnershipOwnerType,
        *,
        cursor: Union[str, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
    ) -> OwnershipHistoryResponse:
        """List ownership history by owner type.

        List inference history entries for a resource filtered by owner type, ordered from most recent to oldest. Uses cursor-based pagination.

        :param resource_id: The identifier of the resource to retrieve inference history for.
        :type resource_id: str
        :param owner_type: The owner type to filter history by.
        :type owner_type: OwnershipOwnerType
        :param cursor: An opaque, base64-encoded cursor token returned by a previous call in ``pagination.next_cursor``. Omit to fetch the first page.
        :type cursor: str, optional
        :param limit: The maximum number of history entries to return per page.
        :type limit: int, optional
        :rtype: OwnershipHistoryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["resource_id"] = resource_id

        kwargs["owner_type"] = owner_type

        if cursor is not unset:
            kwargs["cursor"] = cursor

        if limit is not unset:
            kwargs["limit"] = limit

        return self._list_ownership_history_by_owner_type_endpoint.call_with_http_info(**kwargs)

    def list_ownership_inferences(
        self,
        resource_id: str,
    ) -> OwnershipInferenceListResponse:
        """List ownership inferences for a resource.

        Get all current ownership inferences for a resource, one per owner type ( ``user`` , ``team`` , ``service`` , ``unknown`` ).

        :param resource_id: The identifier of the resource to retrieve ownership inferences for.
        :type resource_id: str
        :rtype: OwnershipInferenceListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["resource_id"] = resource_id

        return self._list_ownership_inferences_endpoint.call_with_http_info(**kwargs)
