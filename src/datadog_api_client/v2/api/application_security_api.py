# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.application_security_exclusion_filters_response import (
    ApplicationSecurityExclusionFiltersResponse,
)
from datadog_api_client.v2.model.application_security_exclusion_filter_response import (
    ApplicationSecurityExclusionFilterResponse,
)
from datadog_api_client.v2.model.application_security_exclusion_filter_request import (
    ApplicationSecurityExclusionFilterRequest,
)


class ApplicationSecurityApi:
    """
    `Datadog Application Security <https://docs.datadoghq.com/security/application_security/>`_ provides protection against
    application-level attacks that aim to exploit code-level vulnerabilities,
    such as Server-Side-Request-Forgery (SSRF), SQL injection, Log4Shell, and
    Reflected Cross-Site-Scripting (XSS). You can monitor and protect apps
    hosted directly on a server, Docker, Kubernetes, Amazon ECS, and (for
    supported languages) AWS Fargate.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_application_security_exclusion_filter_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationSecurityExclusionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/exclusion_filters",
                "operation_id": "create_application_security_exclusion_filter",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ApplicationSecurityExclusionFilterRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_application_security_exclusion_filter_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}",
                "operation_id": "delete_application_security_exclusion_filter",
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

        self._get_application_security_exclusion_filter_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationSecurityExclusionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}",
                "operation_id": "get_application_security_exclusion_filter",
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

        self._list_application_security_exclusion_filters_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationSecurityExclusionFiltersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/exclusion_filters",
                "operation_id": "list_application_security_exclusion_filters",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_application_security_exclusion_filter_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationSecurityExclusionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}",
                "operation_id": "update_application_security_exclusion_filter",
                "http_method": "PUT",
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
                    "openapi_types": (ApplicationSecurityExclusionFilterRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_application_security_exclusion_filter(
        self,
        body: ApplicationSecurityExclusionFilterRequest,
    ) -> ApplicationSecurityExclusionFilterResponse:
        """Create an Application Security exclusion filter.

        Create a new Application Security exclusion filter with the given parameters.

        A request matched by an exclusion filter will be ignored by the Application Security product.
        Go to https://app.datadoghq.com/security/appsec/passlist to review existing exclusion filters (also called passlist entries).

        :param body: The definition of the new exclusion filter.
        :type body: ApplicationSecurityExclusionFilterRequest
        :rtype: ApplicationSecurityExclusionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_application_security_exclusion_filter_endpoint.call_with_http_info(**kwargs)

    def delete_application_security_exclusion_filter(
        self,
        exclusion_filter_id: str,
    ) -> None:
        """Delete an Application Security exclusion filter.

        Delete a specific Application Security exclusion filter using its identifier.

        :param exclusion_filter_id: The identifier of the exclusion filter.
        :type exclusion_filter_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exclusion_filter_id"] = exclusion_filter_id

        return self._delete_application_security_exclusion_filter_endpoint.call_with_http_info(**kwargs)

    def get_application_security_exclusion_filter(
        self,
        exclusion_filter_id: str,
    ) -> ApplicationSecurityExclusionFilterResponse:
        """Get an Application Security exclusion filter.

        Retrieve a specific Application Security exclusion filter using its identifier.

        :param exclusion_filter_id: The identifier of the exclusion filter.
        :type exclusion_filter_id: str
        :rtype: ApplicationSecurityExclusionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exclusion_filter_id"] = exclusion_filter_id

        return self._get_application_security_exclusion_filter_endpoint.call_with_http_info(**kwargs)

    def list_application_security_exclusion_filters(
        self,
    ) -> ApplicationSecurityExclusionFiltersResponse:
        """List all Application Security exclusion filters.

        Retrieve a list of Application Security exclusion filters.

        :rtype: ApplicationSecurityExclusionFiltersResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_application_security_exclusion_filters_endpoint.call_with_http_info(**kwargs)

    def update_application_security_exclusion_filter(
        self,
        exclusion_filter_id: str,
        body: ApplicationSecurityExclusionFilterRequest,
    ) -> ApplicationSecurityExclusionFilterResponse:
        """Update an Application Security exclusion filter.

        Update a specific Application Security exclusion filter using its identifier.
        Returns the exclusion filter object when the request is successful.

        :param exclusion_filter_id: The identifier of the exclusion filter.
        :type exclusion_filter_id: str
        :param body: The exclusion filter to update.
        :type body: ApplicationSecurityExclusionFilterRequest
        :rtype: ApplicationSecurityExclusionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exclusion_filter_id"] = exclusion_filter_id

        kwargs["body"] = body

        return self._update_application_security_exclusion_filter_endpoint.call_with_http_info(**kwargs)
