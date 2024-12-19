# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.aws_scan_options_response import AwsScanOptionsResponse


class AgentlessScanningApi:
    """
    Datadog Agentless Scanning provides visibility into risks and vulnerabilities
    within your hosts, running containers, and serverless functions—all without
    requiring teams to install Agents on every host or where Agents cannot be installed.
    Go to https://www.datadoghq.com/blog/agentless-scanning/ to learn more
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_aws_scan_options_endpoint = _Endpoint(
            settings={
                "response_type": (AwsScanOptionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/agentless_scanning/accounts/aws",
                "operation_id": "list_aws_scan_options",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def list_aws_scan_options(
        self,
    ) -> AwsScanOptionsResponse:
        """Get AWS Scan Options.

        Fetches the scan options configured for AWS accounts.

        :rtype: AwsScanOptionsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_aws_scan_options_endpoint.call_with_http_info(**kwargs)
