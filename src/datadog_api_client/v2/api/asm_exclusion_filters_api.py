# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.asm_exclusion_filter_list_response import ASMExclusionFilterListResponse
from datadog_api_client.v2.model.asm_exclusion_filter_response import ASMExclusionFilterResponse
from datadog_api_client.v2.model.asm_exclusion_filter_create_request import ASMExclusionFilterCreateRequest
from datadog_api_client.v2.model.asm_exclusion_filter_update_request import ASMExclusionFilterUpdateRequest


class ASMExclusionFiltersApi:
    """
    Exclusion filters in ASM libraries are used to circumvent false positives in protection.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_asm_exclusion_filter_endpoint = _Endpoint(
            settings={
                "response_type": (ASMExclusionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/exclusion_filters",
                "operation_id": "create_asm_exclusion_filter",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ASMExclusionFilterCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_asm_exclusion_filter_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}",
                "operation_id": "delete_asm_exclusion_filter",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "exclusion_filter_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "exclusion_filter_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_asm_exclusion_filters_endpoint = _Endpoint(
            settings={
                "response_type": (ASMExclusionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}",
                "operation_id": "get_asm_exclusion_filters",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "exclusion_filter_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "exclusion_filter_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_asm_exclusion_filters_endpoint = _Endpoint(
            settings={
                "response_type": (ASMExclusionFilterListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/exclusion_filters",
                "operation_id": "list_asm_exclusion_filters",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_asm_exclusion_filter_endpoint = _Endpoint(
            settings={
                "response_type": (ASMExclusionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}",
                "operation_id": "update_asm_exclusion_filter",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "exclusion_filter_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "exclusion_filter_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ASMExclusionFilterUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_asm_exclusion_filter(
        self,
        body: ASMExclusionFilterCreateRequest,
    ) -> ASMExclusionFilterResponse:
        """Create a ASM WAF Exclusion filter.

        Create a new exclusion filter with the given parameters.

        :param body: The definition of the new Exclusion filter.
        :type body: ASMExclusionFilterCreateRequest
        :rtype: ASMExclusionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_asm_exclusion_filter_endpoint.call_with_http_info(**kwargs)

    def delete_asm_exclusion_filter(
        self,
        exclusion_filter_id: str,
    ) -> None:
        """Delete a ASM Exclusion Filter.

        Delete a specific ASM Exclusion filter.

        :param exclusion_filter_id: The ID of the exclusion filter.
        :type exclusion_filter_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exclusion_filter_id"] = exclusion_filter_id

        return self._delete_asm_exclusion_filter_endpoint.call_with_http_info(**kwargs)

    def get_asm_exclusion_filters(
        self,
        exclusion_filter_id: str,
    ) -> ASMExclusionFilterResponse:
        """Get a specific ASM Exclusion Filter.

        Retrieve a specific ASM exclusion filter by ID.

        :param exclusion_filter_id: The ID of the exclusion filter.
        :type exclusion_filter_id: str
        :rtype: ASMExclusionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exclusion_filter_id"] = exclusion_filter_id

        return self._get_asm_exclusion_filters_endpoint.call_with_http_info(**kwargs)

    def list_asm_exclusion_filters(
        self,
    ) -> ASMExclusionFilterListResponse:
        """List ASM Exclusion Filters.

        Retrieve a list of ASM exclusion filters.

        :rtype: ASMExclusionFilterListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_asm_exclusion_filters_endpoint.call_with_http_info(**kwargs)

    def update_asm_exclusion_filter(
        self,
        exclusion_filter_id: str,
        body: ASMExclusionFilterUpdateRequest,
    ) -> ASMExclusionFilterResponse:
        """Update a ASM Exclusion filter.

        Update a specific Exclusion filter.
        Returns the Exclusion filter object when the request is successful.

        :param exclusion_filter_id: The ID of the exclusion filter.
        :type exclusion_filter_id: str
        :param body: New definition of the Exclusion filter.
        :type body: ASMExclusionFilterUpdateRequest
        :rtype: ASMExclusionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exclusion_filter_id"] = exclusion_filter_id

        kwargs["body"] = body

        return self._update_asm_exclusion_filter_endpoint.call_with_http_info(**kwargs)
