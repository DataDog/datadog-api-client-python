# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.hamr_org_connection_response import HamrOrgConnectionResponse
from datadog_api_client.v2.model.hamr_org_connection_request import HamrOrgConnectionRequest


class HighAvailabilityMultiRegionApi:
    """
    Configure High Availability Multi-Region (HAMR) connections between Datadog organizations.
    HAMR provides disaster recovery capabilities by maintaining synchronized data between primary
    and secondary organizations across different datacenters.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_hamr_org_connection_endpoint = _Endpoint(
            settings={
                "response_type": (HamrOrgConnectionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/hamr",
                "operation_id": "create_hamr_org_connection",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (HamrOrgConnectionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_hamr_org_connection_endpoint = _Endpoint(
            settings={
                "response_type": (HamrOrgConnectionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/hamr",
                "operation_id": "get_hamr_org_connection",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def create_hamr_org_connection(
        self,
        body: HamrOrgConnectionRequest,
    ) -> HamrOrgConnectionResponse:
        """Create or update HAMR organization connection.

        Create or update the High Availability Multi-Region (HAMR) organization connection.
        This endpoint allows you to configure the HAMR connection between the authenticated organization
        and a target organization, including setting the connection status (ONBOARDING, PASSIVE, FAILOVER, ACTIVE, RECOVERY)

        :type body: HamrOrgConnectionRequest
        :rtype: HamrOrgConnectionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_hamr_org_connection_endpoint.call_with_http_info(**kwargs)

    def get_hamr_org_connection(
        self,
    ) -> HamrOrgConnectionResponse:
        """Get HAMR organization connection.

        Retrieve the High Availability Multi-Region (HAMR) organization connection details for the authenticated organization.
        This endpoint returns information about the HAMR connection configuration, including the target organization,
        datacenter, status, and whether this is the primary or secondary organization in the HAMR relationship.

        :rtype: HamrOrgConnectionResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_hamr_org_connection_endpoint.call_with_http_info(**kwargs)
