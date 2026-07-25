# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.ai_guard_evaluate_response import AIGuardEvaluateResponse
from datadog_api_client.v2.model.ai_guard_evaluate_request import AIGuardEvaluateRequest


class AIGuardApi:
    """
    Analyze AI conversations for security threats including prompt injection,
    jailbreak attempts, and other AI-specific attacks.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._evaluate_ai_guard_request_endpoint = _Endpoint(
            settings={
                "response_type": (AIGuardEvaluateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/ai-guard/evaluate",
                "operation_id": "evaluate_ai_guard_request",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AIGuardEvaluateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def evaluate_ai_guard_request(
        self,
        body: AIGuardEvaluateRequest,
    ) -> AIGuardEvaluateResponse:
        """Evaluate an AI Guard request.

        Analyzes a conversation for security threats such as prompt injection, jailbreak
        attempts, and other AI-specific attacks. Returns an action recommendation (ALLOW,
        DENY, or ABORT) along with the detected threat tags.

        :type body: AIGuardEvaluateRequest
        :rtype: AIGuardEvaluateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._evaluate_ai_guard_request_endpoint.call_with_http_info(**kwargs)
