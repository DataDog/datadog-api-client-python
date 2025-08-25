# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.recommendation_document import RecommendationDocument


class SpaApi:
    """
    SPA (Spark Pod Autosizing) API. Provides resource recommendations and cost insights to help optimize Spark job configurations.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_spa_recommendations_endpoint = _Endpoint(
            settings={
                "response_type": (RecommendationDocument,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/spa/recommendations/{service}/{shard}",
                "operation_id": "get_spa_recommendations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "shard": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "shard",
                    "location": "path",
                },
                "service": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "service",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def get_spa_recommendations(
        self,
        shard: str,
        service: str,
    ) -> RecommendationDocument:
        """Get SPA Recommendations.

        Retrieve resource recommendations for a Spark job. The caller (Spark Gateway or DJM UI) provides a service name and shard identifier, and SPA returns structured recommendations for driver and executor resources.

        :param shard: The shard tag for a spark job, which differentiates jobs within the same service that have different resource needs
        :type shard: str
        :param service: The service name for a spark job
        :type service: str
        :rtype: RecommendationDocument
        """
        kwargs: Dict[str, Any] = {}
        kwargs["shard"] = shard

        kwargs["service"] = service

        return self._get_spa_recommendations_endpoint.call_with_http_info(**kwargs)
