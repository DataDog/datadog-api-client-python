# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.list_pipelines_response import ListPipelinesResponse
from datadog_api_client.v2.model.observability_pipeline import ObservabilityPipeline
from datadog_api_client.v2.model.observability_pipeline_spec import ObservabilityPipelineSpec
from datadog_api_client.v2.model.validation_response import ValidationResponse


class ObservabilityPipelinesApi:
    """
    Observability Pipelines allows you to collect and process logs within your own infrastructure, and then route them to downstream integrations.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_pipeline_endpoint = _Endpoint(
            settings={
                "response_type": (ObservabilityPipeline,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/obs_pipelines/pipelines",
                "operation_id": "create_pipeline",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ObservabilityPipelineSpec,),
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
                "response_type": (ObservabilityPipeline,),
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
                "response_type": (ListPipelinesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/obs_pipelines/pipelines",
                "operation_id": "list_pipelines",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_pipeline_endpoint = _Endpoint(
            settings={
                "response_type": (ObservabilityPipeline,),
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
                    "openapi_types": (ObservabilityPipeline,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._validate_pipeline_endpoint = _Endpoint(
            settings={
                "response_type": (ValidationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/obs_pipelines/pipelines/validate",
                "operation_id": "validate_pipeline",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ObservabilityPipelineSpec,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_pipeline(
        self,
        body: ObservabilityPipelineSpec,
    ) -> ObservabilityPipeline:
        """Create a new pipeline.

        Create a new pipeline.

        :type body: ObservabilityPipelineSpec
        :rtype: ObservabilityPipeline
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_pipeline_endpoint.call_with_http_info(**kwargs)

    def delete_pipeline(
        self,
        pipeline_id: str,
    ) -> None:
        """Delete a pipeline.

        Delete a pipeline.

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
    ) -> ObservabilityPipeline:
        """Get a specific pipeline.

        Get a specific pipeline by its ID.

        :param pipeline_id: The ID of the pipeline to retrieve.
        :type pipeline_id: str
        :rtype: ObservabilityPipeline
        """
        kwargs: Dict[str, Any] = {}
        kwargs["pipeline_id"] = pipeline_id

        return self._get_pipeline_endpoint.call_with_http_info(**kwargs)

    def list_pipelines(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> ListPipelinesResponse:
        """List pipelines.

        Retrieve a list of pipelines.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :rtype: ListPipelinesResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        return self._list_pipelines_endpoint.call_with_http_info(**kwargs)

    def update_pipeline(
        self,
        pipeline_id: str,
        body: ObservabilityPipeline,
    ) -> ObservabilityPipeline:
        """Update a pipeline.

        Update a pipeline.

        :param pipeline_id: The ID of the pipeline to update.
        :type pipeline_id: str
        :type body: ObservabilityPipeline
        :rtype: ObservabilityPipeline
        """
        kwargs: Dict[str, Any] = {}
        kwargs["pipeline_id"] = pipeline_id

        kwargs["body"] = body

        return self._update_pipeline_endpoint.call_with_http_info(**kwargs)

    def validate_pipeline(
        self,
        body: ObservabilityPipelineSpec,
    ) -> ValidationResponse:
        """Validate an observability pipeline.

        Validates a pipeline configuration without creating or updating any resources.
        Returns a list of validation errors, if any.

        :type body: ObservabilityPipelineSpec
        :rtype: ValidationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._validate_pipeline_endpoint.call_with_http_info(**kwargs)
