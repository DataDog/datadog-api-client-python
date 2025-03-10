# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.pipeline import Pipeline


class ObservabilityPipelinesApi:
    """
    Observability Pipelines are awesome!
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_pipeline_endpoint = _Endpoint(
            settings={
                "response_type": (Pipeline,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/obs_pipelines/pipelines",
                "operation_id": "create_pipeline",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (Pipeline,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_pipeline_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}",
                "operation_id": "delete_pipeline",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "pipeline_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "pipeline_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_pipeline_endpoint = _Endpoint(
            settings={
                "response_type": (Pipeline,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}",
                "operation_id": "get_pipeline",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "pipeline_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "pipeline_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_pipelines_endpoint = _Endpoint(
            settings={
                "response_type": ([Pipeline],),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/obs_pipelines/pipelines",
                "operation_id": "list_pipelines",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_pipeline_endpoint = _Endpoint(
            settings={
                "response_type": (Pipeline,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/obs_pipelines/pipelines/{pipeline_id}",
                "operation_id": "update_pipeline",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "pipeline_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "pipeline_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (Pipeline,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_pipeline(
        self,
        body: Pipeline,
    ) -> Pipeline:
        """Create a new pipeline.

        Creates a new observability pipeline.

        :type body: Pipeline
        :rtype: Pipeline
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_pipeline_endpoint.call_with_http_info(**kwargs)

    def delete_pipeline(
        self,
        pipeline_id: str,
    ) -> None:
        """Delete a specific pipeline.

        Deletes a specific observability pipeline.

        :param pipeline_id: The ID of the pipeline to delete.
        :type pipeline_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["pipeline_id"] = pipeline_id

        return self._delete_pipeline_endpoint.call_with_http_info(**kwargs)

    def get_pipeline(
        self,
        pipeline_id: str,
    ) -> Pipeline:
        """Get a specific pipeline.

        Retrieves a specific observability pipeline.

        :param pipeline_id: The ID of the pipeline to retrieve.
        :type pipeline_id: str
        :rtype: Pipeline
        """
        kwargs: Dict[str, Any] = {}
        kwargs["pipeline_id"] = pipeline_id

        return self._get_pipeline_endpoint.call_with_http_info(**kwargs)

    def list_pipelines(
        self,
    ) -> List[Pipeline]:
        """Get all pipelines.

        Retrieves a list of all configured observability pipelines.

        :rtype: [Pipeline]
        """
        kwargs: Dict[str, Any] = {}
        return self._list_pipelines_endpoint.call_with_http_info(**kwargs)

    def update_pipeline(
        self,
        pipeline_id: str,
        body: Pipeline,
    ) -> Pipeline:
        """Update a specific pipeline.

        Updates a specific observability pipeline.

        :param pipeline_id: The ID of the pipeline to update.
        :type pipeline_id: str
        :type body: Pipeline
        :rtype: Pipeline
        """
        kwargs: Dict[str, Any] = {}
        kwargs["pipeline_id"] = pipeline_id

        kwargs["body"] = body

        return self._update_pipeline_endpoint.call_with_http_info(**kwargs)
