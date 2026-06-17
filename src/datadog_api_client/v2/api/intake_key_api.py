# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.intake_api_key_response import IntakeAPIKeyResponse


class IntakeKeyApi:
    """
    Exchange a cloud-provider identity proof for a Datadog API key via Workload Identity Federation intake mappings.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_intake_key_endpoint = _Endpoint(
            settings={
                "response_type": (IntakeAPIKeyResponse,),
                "auth": [],
                "endpoint_path": "/api/v2/intake-key",
                "operation_id": "get_intake_key",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def get_intake_key(
        self,
    ) -> IntakeAPIKeyResponse:
        """Get an intake API key.

        Exchanges a Workload Identity Federation (WIF) identity proof for a Datadog API key associated with the matching WIF intake mapping.

        Pass a cloud-provider token in the ``Authorization`` header using the ``Bearer`` or ``Delegated`` scheme.
        The token is validated against the WIF intake mappings configured for the caller's organization. On success,
        a managed-rotation API key is returned that the workload can use to send telemetry to Datadog.

        Unlike the delegated-token endpoint ( ``POST /api/v2/delegated-token`` ), this endpoint authenticates
        the cloud workload at the organization level rather than mapping it to a specific Datadog user.

        Standard Datadog API and application key authentication is not accepted. Authenticate using a
        cloud-provider token in the ``Authorization: Bearer`` header.

        :rtype: IntakeAPIKeyResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_intake_key_endpoint.call_with_http_info(**kwargs)
