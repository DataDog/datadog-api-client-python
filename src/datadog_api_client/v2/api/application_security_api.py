# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.application_security_waf_custom_rule_list_response import (
    ApplicationSecurityWafCustomRuleListResponse,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_response import (
    ApplicationSecurityWafCustomRuleResponse,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_create_request import (
    ApplicationSecurityWafCustomRuleCreateRequest,
)
from datadog_api_client.v2.model.application_security_waf_custom_rule_update_request import (
    ApplicationSecurityWafCustomRuleUpdateRequest,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filters_response import (
    ApplicationSecurityWafExclusionFiltersResponse,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_response import (
    ApplicationSecurityWafExclusionFilterResponse,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_create_request import (
    ApplicationSecurityWafExclusionFilterCreateRequest,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_update_request import (
    ApplicationSecurityWafExclusionFilterUpdateRequest,
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

        self._create_application_security_waf_custom_rule_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationSecurityWafCustomRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/custom_rules",
                "operation_id": "create_application_security_waf_custom_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ApplicationSecurityWafCustomRuleCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_application_security_waf_exclusion_filter_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationSecurityWafExclusionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/exclusion_filters",
                "operation_id": "create_application_security_waf_exclusion_filter",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ApplicationSecurityWafExclusionFilterCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_application_security_waf_custom_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id}",
                "operation_id": "delete_application_security_waf_custom_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "custom_rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "custom_rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_application_security_waf_exclusion_filter_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}",
                "operation_id": "delete_application_security_waf_exclusion_filter",
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

        self._get_application_security_waf_custom_rule_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationSecurityWafCustomRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id}",
                "operation_id": "get_application_security_waf_custom_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "custom_rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "custom_rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_application_security_waf_exclusion_filter_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationSecurityWafExclusionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}",
                "operation_id": "get_application_security_waf_exclusion_filter",
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

        self._list_application_security_waf_custom_rules_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationSecurityWafCustomRuleListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/custom_rules",
                "operation_id": "list_application_security_waf_custom_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_application_security_waf_exclusion_filters_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationSecurityWafExclusionFiltersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/exclusion_filters",
                "operation_id": "list_application_security_waf_exclusion_filters",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_application_security_waf_custom_rule_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationSecurityWafCustomRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/custom_rules/{custom_rule_id}",
                "operation_id": "update_application_security_waf_custom_rule",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "custom_rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "custom_rule_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ApplicationSecurityWafCustomRuleUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_application_security_waf_exclusion_filter_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationSecurityWafExclusionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/asm/waf/exclusion_filters/{exclusion_filter_id}",
                "operation_id": "update_application_security_waf_exclusion_filter",
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
                    "openapi_types": (ApplicationSecurityWafExclusionFilterUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_application_security_waf_custom_rule(
        self,
        body: ApplicationSecurityWafCustomRuleCreateRequest,
    ) -> ApplicationSecurityWafCustomRuleResponse:
        """Create a WAF custom rule.

        Create a new WAF custom rule with the given parameters.

        :param body: The definition of the new WAF Custom Rule.
        :type body: ApplicationSecurityWafCustomRuleCreateRequest
        :rtype: ApplicationSecurityWafCustomRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_application_security_waf_custom_rule_endpoint.call_with_http_info(**kwargs)

    def create_application_security_waf_exclusion_filter(
        self,
        body: ApplicationSecurityWafExclusionFilterCreateRequest,
    ) -> ApplicationSecurityWafExclusionFilterResponse:
        """Create a WAF exclusion filter.

        Create a new WAF exclusion filter with the given parameters.

        A request matched by an exclusion filter will be ignored by the Application Security WAF product.
        Go to https://app.datadoghq.com/security/appsec/passlist to review existing exclusion filters (also called passlist entries).

        :param body: The definition of the new WAF exclusion filter.
        :type body: ApplicationSecurityWafExclusionFilterCreateRequest
        :rtype: ApplicationSecurityWafExclusionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_application_security_waf_exclusion_filter_endpoint.call_with_http_info(**kwargs)

    def delete_application_security_waf_custom_rule(
        self,
        custom_rule_id: str,
    ) -> None:
        """Delete a WAF Custom Rule.

        Delete a specific WAF custom rule.

        :param custom_rule_id: The ID of the custom rule.
        :type custom_rule_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["custom_rule_id"] = custom_rule_id

        return self._delete_application_security_waf_custom_rule_endpoint.call_with_http_info(**kwargs)

    def delete_application_security_waf_exclusion_filter(
        self,
        exclusion_filter_id: str,
    ) -> None:
        """Delete a WAF exclusion filter.

        Delete a specific WAF exclusion filter using its identifier.

        :param exclusion_filter_id: The identifier of the WAF exclusion filter.
        :type exclusion_filter_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exclusion_filter_id"] = exclusion_filter_id

        return self._delete_application_security_waf_exclusion_filter_endpoint.call_with_http_info(**kwargs)

    def get_application_security_waf_custom_rule(
        self,
        custom_rule_id: str,
    ) -> ApplicationSecurityWafCustomRuleResponse:
        """Get a WAF custom rule.

        Retrieve a WAF custom rule by ID.

        :param custom_rule_id: The ID of the custom rule.
        :type custom_rule_id: str
        :rtype: ApplicationSecurityWafCustomRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["custom_rule_id"] = custom_rule_id

        return self._get_application_security_waf_custom_rule_endpoint.call_with_http_info(**kwargs)

    def get_application_security_waf_exclusion_filter(
        self,
        exclusion_filter_id: str,
    ) -> ApplicationSecurityWafExclusionFilterResponse:
        """Get a WAF exclusion filter.

        Retrieve a specific WAF exclusion filter using its identifier.

        :param exclusion_filter_id: The identifier of the WAF exclusion filter.
        :type exclusion_filter_id: str
        :rtype: ApplicationSecurityWafExclusionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exclusion_filter_id"] = exclusion_filter_id

        return self._get_application_security_waf_exclusion_filter_endpoint.call_with_http_info(**kwargs)

    def list_application_security_waf_custom_rules(
        self,
    ) -> ApplicationSecurityWafCustomRuleListResponse:
        """List all WAF custom rules.

        Retrieve a list of WAF custom rule.

        :rtype: ApplicationSecurityWafCustomRuleListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_application_security_waf_custom_rules_endpoint.call_with_http_info(**kwargs)

    def list_application_security_waf_exclusion_filters(
        self,
    ) -> ApplicationSecurityWafExclusionFiltersResponse:
        """List all WAF exclusion filters.

        Retrieve a list of WAF exclusion filters.

        :rtype: ApplicationSecurityWafExclusionFiltersResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_application_security_waf_exclusion_filters_endpoint.call_with_http_info(**kwargs)

    def update_application_security_waf_custom_rule(
        self,
        custom_rule_id: str,
        body: ApplicationSecurityWafCustomRuleUpdateRequest,
    ) -> ApplicationSecurityWafCustomRuleResponse:
        """Update a WAF Custom Rule.

        Update a specific WAF custom Rule.
        Returns the Custom Rule object when the request is successful.

        :param custom_rule_id: The ID of the custom rule.
        :type custom_rule_id: str
        :param body: New definition of the WAF Custom Rule.
        :type body: ApplicationSecurityWafCustomRuleUpdateRequest
        :rtype: ApplicationSecurityWafCustomRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["custom_rule_id"] = custom_rule_id

        kwargs["body"] = body

        return self._update_application_security_waf_custom_rule_endpoint.call_with_http_info(**kwargs)

    def update_application_security_waf_exclusion_filter(
        self,
        exclusion_filter_id: str,
        body: ApplicationSecurityWafExclusionFilterUpdateRequest,
    ) -> ApplicationSecurityWafExclusionFilterResponse:
        """Update a WAF exclusion filter.

        Update a specific WAF exclusion filter using its identifier.
        Returns the exclusion filter object when the request is successful.

        :param exclusion_filter_id: The identifier of the WAF exclusion filter.
        :type exclusion_filter_id: str
        :param body: The exclusion filter to update.
        :type body: ApplicationSecurityWafExclusionFilterUpdateRequest
        :rtype: ApplicationSecurityWafExclusionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exclusion_filter_id"] = exclusion_filter_id

        kwargs["body"] = body

        return self._update_application_security_waf_exclusion_filter_endpoint.call_with_http_info(**kwargs)
