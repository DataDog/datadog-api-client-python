# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.aws_cloud_auth_persona_mappings_response import AWSCloudAuthPersonaMappingsResponse


class CloudAuthenticationApi:
    """
    Configure AWS cloud authentication mappings for persona and intake authentication through the Datadog API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_aws_cloud_auth_persona_mappings_endpoint = _Endpoint(
            settings={
                "response_type": (AWSCloudAuthPersonaMappingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cloud_auth/aws/persona_mapping",
                "operation_id": "list_aws_cloud_auth_persona_mappings",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def list_aws_cloud_auth_persona_mappings(
        self,
    ) -> AWSCloudAuthPersonaMappingsResponse:
        """List AWS cloud authentication persona mappings.

        List all AWS cloud authentication persona mappings. This endpoint retrieves all configured persona mappings that associate AWS IAM principals with Datadog users.

        :rtype: AWSCloudAuthPersonaMappingsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_aws_cloud_auth_persona_mappings_endpoint.call_with_http_info(**kwargs)
