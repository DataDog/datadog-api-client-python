# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.on_prem_management_service_create_enrollment_response import (
    OnPremManagementServiceCreateEnrollmentResponse,
)
from datadog_api_client.v2.model.on_prem_management_service_create_enrollment_request import (
    OnPremManagementServiceCreateEnrollmentRequest,
)
from datadog_api_client.v2.model.on_prem_management_service_get_enrollment_response import (
    OnPremManagementServiceGetEnrollmentResponse,
)
from datadog_api_client.v2.model.on_prem_management_service_register_token_response import (
    OnPremManagementServiceRegisterTokenResponse,
)
from datadog_api_client.v2.model.on_prem_management_service_register_token_request import (
    OnPremManagementServiceRegisterTokenRequest,
)


class OnPremManagementServiceApi:
    """
    Manage on-premises runners for workflow automation and app builder. Use these endpoints to enroll runners, check enrollment status, and register tokens for query execution.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_on_prem_management_service_enrollment_endpoint = _Endpoint(
            settings={
                "response_type": (OnPremManagementServiceCreateEnrollmentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/on-prem-management-service/enrollments",
                "operation_id": "create_on_prem_management_service_enrollment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OnPremManagementServiceCreateEnrollmentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_on_prem_management_service_enrollment_endpoint = _Endpoint(
            settings={
                "response_type": (OnPremManagementServiceGetEnrollmentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/on-prem-management-service/enrollments/{token_hash}",
                "operation_id": "get_on_prem_management_service_enrollment",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "token_hash": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "token_hash",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._register_on_prem_management_service_token_endpoint = _Endpoint(
            settings={
                "response_type": (OnPremManagementServiceRegisterTokenResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/on-prem-management-service/tokens/register",
                "operation_id": "register_on_prem_management_service_token",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OnPremManagementServiceRegisterTokenRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_on_prem_management_service_enrollment(
        self,
        body: OnPremManagementServiceCreateEnrollmentRequest,
    ) -> OnPremManagementServiceCreateEnrollmentResponse:
        """Create an enrollment.

        Create a new enrollment for an on-prem runner. This endpoint initiates the enrollment process and returns a token that the runner will use to complete the enrollment.

        :type body: OnPremManagementServiceCreateEnrollmentRequest
        :rtype: OnPremManagementServiceCreateEnrollmentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_on_prem_management_service_enrollment_endpoint.call_with_http_info(**kwargs)

    def get_on_prem_management_service_enrollment(
        self,
        token_hash: str,
    ) -> OnPremManagementServiceGetEnrollmentResponse:
        """Get enrollment status.

        Get the status of an enrollment for an on-prem runner using the enrollment token hash.

        :param token_hash: The enrollment token hash.
        :type token_hash: str
        :rtype: OnPremManagementServiceGetEnrollmentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["token_hash"] = token_hash

        return self._get_on_prem_management_service_enrollment_endpoint.call_with_http_info(**kwargs)

    def register_on_prem_management_service_token(
        self,
        body: OnPremManagementServiceRegisterTokenRequest,
    ) -> OnPremManagementServiceRegisterTokenResponse:
        """Register a token.

        Register a token for query execution. This endpoint allows an on-prem runner to register a token that will be used to execute queries on a specific connection.

        :type body: OnPremManagementServiceRegisterTokenRequest
        :rtype: OnPremManagementServiceRegisterTokenResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._register_on_prem_management_service_token_endpoint.call_with_http_info(**kwargs)
