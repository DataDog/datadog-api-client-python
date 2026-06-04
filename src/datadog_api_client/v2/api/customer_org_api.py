# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.customer_org_disable_response import CustomerOrgDisableResponse
from datadog_api_client.v2.model.customer_org_disable_request import CustomerOrgDisableRequest


class CustomerOrgApi:
    """
    Programmatic management of a customer's Datadog organization. Use this API to perform
    self-service organization lifecycle actions such as disabling the authenticated org.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._disable_customer_org_endpoint = _Endpoint(
            settings={
                "response_type": (CustomerOrgDisableResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/org/disable",
                "operation_id": "disable_customer_org",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CustomerOrgDisableRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def disable_customer_org(
        self,
        body: CustomerOrgDisableRequest,
    ) -> CustomerOrgDisableResponse:
        """Disable the authenticated customer organization.

        Disable the Datadog organization associated with the authenticated user or API key.
        The request body uses JSON:API format. If ``org_uuid`` is supplied, it must match
        the authenticated org or the request is rejected. Successful calls disable the org
        and return the resulting state from the downstream service. Requires the
        ``org_management`` permission.

        :type body: CustomerOrgDisableRequest
        :rtype: CustomerOrgDisableResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._disable_customer_org_endpoint.call_with_http_info(**kwargs)
