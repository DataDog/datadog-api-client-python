# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.policy_result_response import PolicyResultResponse


class PolicyManagementApi:
    """
    Manage and evaluate organizational policies.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._evaluate_policy_result_endpoint = _Endpoint(
            settings={
                "response_type": (PolicyResultResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/policy/{policy_type}/result",
                "operation_id": "evaluate_policy_result",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "policy_type": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "policy_type",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def evaluate_policy_result(
        self,
        policy_type: str,
    ) -> PolicyResultResponse:
        """Evaluate policy result.

        Retrieve the evaluation result for a specific policy type.

        :param policy_type: The type of policy to evaluate (e.g., SAML, HIPAA).
        :type policy_type: str
        :rtype: PolicyResultResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_type"] = policy_type

        return self._evaluate_policy_result_endpoint.call_with_http_info(**kwargs)
