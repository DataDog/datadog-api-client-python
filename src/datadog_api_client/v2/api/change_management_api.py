# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.change_request_response import ChangeRequestResponse
from datadog_api_client.v2.model.change_request_create_request import ChangeRequestCreateRequest
from datadog_api_client.v2.model.change_request_update_request import ChangeRequestUpdateRequest
from datadog_api_client.v2.model.change_request_branch_create_request import ChangeRequestBranchCreateRequest
from datadog_api_client.v2.model.change_request_decision_update_request import ChangeRequestDecisionUpdateRequest


class ChangeManagementApi:
    """
    View and manage change requests within Change Management. See the `Case Management page <https://docs.datadoghq.com/service_management/case_management/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_change_request_endpoint = _Endpoint(
            settings={
                "response_type": (ChangeRequestResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/change-management/change-request",
                "operation_id": "create_change_request",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ChangeRequestCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_change_request_branch_endpoint = _Endpoint(
            settings={
                "response_type": (ChangeRequestResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/change-management/change-request/{change_request_id}/branch",
                "operation_id": "create_change_request_branch",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "change_request_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "change_request_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ChangeRequestBranchCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_change_request_decision_endpoint = _Endpoint(
            settings={
                "response_type": (ChangeRequestResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id}",
                "operation_id": "delete_change_request_decision",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "change_request_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "change_request_id",
                    "location": "path",
                },
                "decision_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "decision_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_change_request_endpoint = _Endpoint(
            settings={
                "response_type": (ChangeRequestResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/change-management/change-request/{change_request_id}",
                "operation_id": "get_change_request",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "change_request_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "change_request_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_change_request_endpoint = _Endpoint(
            settings={
                "response_type": (ChangeRequestResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/change-management/change-request/{change_request_id}",
                "operation_id": "update_change_request",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "change_request_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "change_request_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ChangeRequestUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_change_request_decision_endpoint = _Endpoint(
            settings={
                "response_type": (ChangeRequestResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id}",
                "operation_id": "update_change_request_decision",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "change_request_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "change_request_id",
                    "location": "path",
                },
                "decision_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "decision_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ChangeRequestDecisionUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_change_request(
        self,
        body: ChangeRequestCreateRequest,
    ) -> ChangeRequestResponse:
        """Create a change request.

        Create a new change request.

        :param body: Change request payload.
        :type body: ChangeRequestCreateRequest
        :rtype: ChangeRequestResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_change_request_endpoint.call_with_http_info(**kwargs)

    def create_change_request_branch(
        self,
        change_request_id: str,
        body: ChangeRequestBranchCreateRequest,
    ) -> ChangeRequestResponse:
        """Create a change request branch.

        Create a new branch in a repository for a change request.

        :param change_request_id: The identifier of the change request.
        :type change_request_id: str
        :param body: Branch creation payload.
        :type body: ChangeRequestBranchCreateRequest
        :rtype: ChangeRequestResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["change_request_id"] = change_request_id

        kwargs["body"] = body

        return self._create_change_request_branch_endpoint.call_with_http_info(**kwargs)

    def delete_change_request_decision(
        self,
        change_request_id: str,
        decision_id: str,
    ) -> ChangeRequestResponse:
        """Delete a change request decision.

        Delete a decision from a change request.

        :param change_request_id: The identifier of the change request.
        :type change_request_id: str
        :param decision_id: The identifier of the change request decision.
        :type decision_id: str
        :rtype: ChangeRequestResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["change_request_id"] = change_request_id

        kwargs["decision_id"] = decision_id

        return self._delete_change_request_decision_endpoint.call_with_http_info(**kwargs)

    def get_change_request(
        self,
        change_request_id: str,
    ) -> ChangeRequestResponse:
        """Get a change request.

        Get the details of a change request by its ID.

        :param change_request_id: The identifier of the change request.
        :type change_request_id: str
        :rtype: ChangeRequestResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["change_request_id"] = change_request_id

        return self._get_change_request_endpoint.call_with_http_info(**kwargs)

    def update_change_request(
        self,
        change_request_id: str,
        body: ChangeRequestUpdateRequest,
    ) -> ChangeRequestResponse:
        """Update a change request.

        Update the properties of a change request.

        :param change_request_id: The identifier of the change request.
        :type change_request_id: str
        :param body: Change request update payload.
        :type body: ChangeRequestUpdateRequest
        :rtype: ChangeRequestResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["change_request_id"] = change_request_id

        kwargs["body"] = body

        return self._update_change_request_endpoint.call_with_http_info(**kwargs)

    def update_change_request_decision(
        self,
        change_request_id: str,
        decision_id: str,
        body: ChangeRequestDecisionUpdateRequest,
    ) -> ChangeRequestResponse:
        """Update a change request decision.

        Update a decision on a change request, such as approving or declining it.

        :param change_request_id: The identifier of the change request.
        :type change_request_id: str
        :param decision_id: The identifier of the change request decision.
        :type decision_id: str
        :param body: Decision update payload.
        :type body: ChangeRequestDecisionUpdateRequest
        :rtype: ChangeRequestResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["change_request_id"] = change_request_id

        kwargs["decision_id"] = decision_id

        kwargs["body"] = body

        return self._update_change_request_decision_endpoint.call_with_http_info(**kwargs)
