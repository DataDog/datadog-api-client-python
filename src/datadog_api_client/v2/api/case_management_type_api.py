# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.case_types_response import CaseTypesResponse
from datadog_api_client.v2.model.case_type_response import CaseTypeResponse
from datadog_api_client.v2.model.case_type_create_request import CaseTypeCreateRequest


class CaseManagementTypeApi:
    """
    View and configure case types within Case Management. See the `Case Management page <https://docs.datadoghq.com/service_management/case_management/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_case_type_endpoint = _Endpoint(
            settings={
                "response_type": (CaseTypeResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cases/types",
                "operation_id": "create_case_type",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CaseTypeCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_case_type_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cases/types/{case_type_id}",
                "operation_id": "delete_case_type",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "case_type_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_type_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_all_case_types_endpoint = _Endpoint(
            settings={
                "response_type": (CaseTypesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cases/types",
                "operation_id": "get_all_case_types",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def create_case_type(
        self,
        body: CaseTypeCreateRequest,
    ) -> CaseTypeResponse:
        """Create a case type.

        Create a Case Type

        :param body: Case type payload
        :type body: CaseTypeCreateRequest
        :rtype: CaseTypeResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_case_type_endpoint.call_with_http_info(**kwargs)

    def delete_case_type(
        self,
        case_type_id: str,
    ) -> None:
        """Delete a case type.

        Delete a case type

        :param case_type_id: Case type's UUID
        :type case_type_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_type_id"] = case_type_id

        return self._delete_case_type_endpoint.call_with_http_info(**kwargs)

    def get_all_case_types(
        self,
    ) -> CaseTypesResponse:
        """Get all case types.

        Get all case types

        :rtype: CaseTypesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_all_case_types_endpoint.call_with_http_info(**kwargs)
