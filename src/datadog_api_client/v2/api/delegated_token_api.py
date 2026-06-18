# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.delegated_token_response import DelegatedTokenResponse


class DelegatedTokenApi:
    """
    Exchange a cloud-provider identity proof or Datadog credential for a short-lived delegated-user JWT
    via Workload Identity Federation.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_delegated_token_endpoint = _Endpoint(
            settings={
                "response_type": (DelegatedTokenResponse,),
                "auth": [],
                "endpoint_path": "/api/v2/delegated-token",
                "operation_id": "get_delegated_token",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def get_delegated_token(
        self,
    ) -> DelegatedTokenResponse:
        """Get a delegated token.

        Exchange a Workload Identity Federation (WIF) proof or Datadog credentials for a short-lived access token
        scoped to a Datadog user.

        To authenticate with a WIF identity, pass the cloud-provider token in the ``Authorization`` header using
        the ``Bearer`` or ``Delegated`` scheme. Datadog resolves the Datadog user from the persona mapping configured
        for that cloud identity.

        To obtain a token for the calling user directly, authenticate with standard Datadog API and application keys.

        Use the returned ``access_token`` as a bearer token in subsequent API calls.

        :rtype: DelegatedTokenResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_delegated_token_endpoint.call_with_http_info(**kwargs)
