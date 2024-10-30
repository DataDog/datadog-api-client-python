# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.domain_allowlist_response import DomainAllowlistResponse
from datadog_api_client.v2.model.domain_allowlist_request import DomainAllowlistRequest


class DomainAllowlistApi:
    """
    Configure your Datadog Email Domain Allowlist directly through the Datadog API.
    The Email Domain Allowlist controls the domains that certain datadog emails can be sent to.
    For more information, see the `Domain Allowlist docs page <https://docs.datadoghq.com/account_management/org_settings/domain_allowlist>`_
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_domain_allowlist_endpoint = _Endpoint(
            settings={
                "response_type": (DomainAllowlistResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/domain_allowlist",
                "operation_id": "get_domain_allowlist",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._patch_domain_allowlist_endpoint = _Endpoint(
            settings={
                "response_type": (DomainAllowlistResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/domain_allowlist",
                "operation_id": "patch_domain_allowlist",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DomainAllowlistRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def get_domain_allowlist(
        self,
    ) -> DomainAllowlistResponse:
        """Get Domain Allowlist.

        Get the domain allowlist for an organization.

        :rtype: DomainAllowlistResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_domain_allowlist_endpoint.call_with_http_info(**kwargs)

    def patch_domain_allowlist(
        self,
        body: DomainAllowlistRequest,
    ) -> DomainAllowlistResponse:
        """Sets Domain Allowlist.

        Update the domain allowlist for an organization.

        :type body: DomainAllowlistRequest
        :rtype: DomainAllowlistResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._patch_domain_allowlist_endpoint.call_with_http_info(**kwargs)
