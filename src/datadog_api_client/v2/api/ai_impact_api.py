# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.ai_impact_user_activity_request import AIImpactUserActivityRequest


class AIImpactApi:
    """
    Send AI coding tool usage data to measure the impact of AI tools on software delivery.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_ai_impact_user_activity_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth"],
                "endpoint_path": "/api/v2/ai_impact/user_activity",
                "operation_id": "create_ai_impact_user_activity",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AIImpactUserActivityRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_ai_impact_user_activity(
        self,
        body: AIImpactUserActivityRequest,
    ) -> None:
        """Send AI tool user activity.

        Send daily AI coding tool activity for one or more users. Each entry records whether a
        user was active on a given day, along with the AI tools and models they used. An entry
        is stored once per tool, and sending the same user, day, and tool again overwrites the
        previous value.

        :type body: AIImpactUserActivityRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_ai_impact_user_activity_endpoint.call_with_http_info(**kwargs)
