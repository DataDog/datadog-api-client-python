# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    file_type,
    UnsetType,
    unset,
    UUID,
)
from datadog_api_client.v2.model.model_lab_facet_keys_response import ModelLabFacetKeysResponse
from datadog_api_client.v2.model.model_lab_facet_values_response import ModelLabFacetValuesResponse
from datadog_api_client.v2.model.model_lab_facet_type import ModelLabFacetType
from datadog_api_client.v2.model.model_lab_project_facet_type import ModelLabProjectFacetType
from datadog_api_client.v2.model.model_lab_projects_response import ModelLabProjectsResponse
from datadog_api_client.v2.model.model_lab_project_response import ModelLabProjectResponse
from datadog_api_client.v2.model.model_lab_project_artifacts_response import ModelLabProjectArtifactsResponse
from datadog_api_client.v2.model.model_lab_runs_response import ModelLabRunsResponse
from datadog_api_client.v2.model.model_lab_run_status import ModelLabRunStatus
from datadog_api_client.v2.model.model_lab_run_response import ModelLabRunResponse
from datadog_api_client.v2.model.model_lab_run_artifacts_response import ModelLabRunArtifactsResponse


class ModelLabAPIApi:
    """
    Manage Model Lab projects, runs, artifacts, and facets for ML experiment tracking.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._delete_model_lab_run_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/runs/{run_id}",
                "operation_id": "delete_model_lab_run",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "run_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "run_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_model_lab_artifact_content_endpoint = _Endpoint(
            settings={
                "response_type": (file_type,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/artifacts/content",
                "operation_id": "get_model_lab_artifact_content",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "query",
                },
                "artifact_path": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "artifact_path",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/octet-stream", "application/json"],
            },
            api_client=api_client,
        )

        self._get_model_lab_project_endpoint = _Endpoint(
            settings={
                "response_type": (ModelLabProjectResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/projects/{project_id}",
                "operation_id": "get_model_lab_project",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "project_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_model_lab_run_endpoint = _Endpoint(
            settings={
                "response_type": (ModelLabRunResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/runs/{run_id}",
                "operation_id": "get_model_lab_run",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "run_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "run_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_model_lab_project_artifacts_endpoint = _Endpoint(
            settings={
                "response_type": (ModelLabProjectArtifactsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/projects/{project_id}/artifacts",
                "operation_id": "list_model_lab_project_artifacts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "project_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_model_lab_project_facet_keys_endpoint = _Endpoint(
            settings={
                "response_type": (ModelLabFacetKeysResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/project-facet-keys",
                "operation_id": "list_model_lab_project_facet_keys",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_model_lab_project_facet_values_endpoint = _Endpoint(
            settings={
                "response_type": (ModelLabFacetValuesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/project-facet-values",
                "operation_id": "list_model_lab_project_facet_values",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "facet_type": {
                    "required": True,
                    "openapi_types": (ModelLabProjectFacetType,),
                    "attribute": "facet_type",
                    "location": "query",
                },
                "facet_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "facet_name",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_model_lab_projects_endpoint = _Endpoint(
            settings={
                "response_type": (ModelLabProjectsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/projects",
                "operation_id": "list_model_lab_projects",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
                "filter_owner_id": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[owner_id]",
                    "location": "query",
                },
                "filter_tags": {
                    "openapi_types": (str,),
                    "attribute": "filter[tags]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 100,
                    },
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

        self._list_model_lab_run_artifacts_endpoint = _Endpoint(
            settings={
                "response_type": (ModelLabRunArtifactsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/runs/{run_id}/artifacts",
                "operation_id": "list_model_lab_run_artifacts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "run_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "run_id",
                    "location": "path",
                },
                "path": {
                    "openapi_types": (str,),
                    "attribute": "path",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_model_lab_run_facet_keys_endpoint = _Endpoint(
            settings={
                "response_type": (ModelLabFacetKeysResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/facet-keys",
                "operation_id": "list_model_lab_run_facet_keys",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_project_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "filter[project_id]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_model_lab_run_facet_values_endpoint = _Endpoint(
            settings={
                "response_type": (ModelLabFacetValuesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/facet-values",
                "operation_id": "list_model_lab_run_facet_values",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_project_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "filter[project_id]",
                    "location": "query",
                },
                "facet_type": {
                    "required": True,
                    "openapi_types": (ModelLabFacetType,),
                    "attribute": "facet_type",
                    "location": "query",
                },
                "facet_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "facet_name",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_model_lab_runs_endpoint = _Endpoint(
            settings={
                "response_type": (ModelLabRunsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/runs",
                "operation_id": "list_model_lab_runs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[id]",
                    "location": "query",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
                "filter_owner_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[owner_id]",
                    "location": "query",
                },
                "filter_status": {
                    "openapi_types": (ModelLabRunStatus,),
                    "attribute": "filter[status]",
                    "location": "query",
                },
                "filter_project_id": {
                    "openapi_types": (int,),
                    "attribute": "filter[project_id]",
                    "location": "query",
                },
                "filter_tags": {
                    "openapi_types": (str,),
                    "attribute": "filter[tags]",
                    "location": "query",
                },
                "filter_params": {
                    "openapi_types": (str,),
                    "attribute": "filter[params]",
                    "location": "query",
                },
                "filter_parent_run_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[parent_run_id]",
                    "location": "query",
                },
                "pinned_first": {
                    "openapi_types": (bool,),
                    "attribute": "pinned_first",
                    "location": "query",
                },
                "include_pinned": {
                    "openapi_types": (bool,),
                    "attribute": "include_pinned",
                    "location": "query",
                },
                "include_descendant_matches": {
                    "openapi_types": (bool,),
                    "attribute": "include_descendant_matches",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 100,
                    },
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

        self._pin_model_lab_run_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/runs/{run_id}/pin",
                "operation_id": "pin_model_lab_run",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "run_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "run_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._star_model_lab_project_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/projects/{project_id}/star",
                "operation_id": "star_model_lab_project",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "project_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._unpin_model_lab_run_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/runs/{run_id}/pin",
                "operation_id": "unpin_model_lab_run",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "run_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "run_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._unstar_model_lab_project_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/model-lab-api/projects/{project_id}/star",
                "operation_id": "unstar_model_lab_project",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "project_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

    def delete_model_lab_run(
        self,
        run_id: int,
    ) -> None:
        """Delete a Model Lab run.

        Delete a Model Lab run by its ID.

        :param run_id: The ID of the Model Lab run.
        :type run_id: int
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["run_id"] = run_id

        return self._delete_model_lab_run_endpoint.call_with_http_info(**kwargs)

    def get_model_lab_artifact_content(
        self,
        project_id: str,
        artifact_path: str,
    ) -> file_type:
        """Get Model Lab artifact content.

        Download the raw content of a Model Lab artifact file.

        :param project_id: ID of the project.
        :type project_id: str
        :param artifact_path: Path to the artifact relative to the project directory.
        :type artifact_path: str
        :rtype: file_type
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        kwargs["artifact_path"] = artifact_path

        return self._get_model_lab_artifact_content_endpoint.call_with_http_info(**kwargs)

    def get_model_lab_project(
        self,
        project_id: int,
    ) -> ModelLabProjectResponse:
        """Get a Model Lab project.

        Get a single Model Lab project by its ID.

        :param project_id: The ID of the Model Lab project.
        :type project_id: int
        :rtype: ModelLabProjectResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        return self._get_model_lab_project_endpoint.call_with_http_info(**kwargs)

    def get_model_lab_run(
        self,
        run_id: int,
    ) -> ModelLabRunResponse:
        """Get a Model Lab run.

        Get a single Model Lab run by its ID.

        :param run_id: The ID of the Model Lab run.
        :type run_id: int
        :rtype: ModelLabRunResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["run_id"] = run_id

        return self._get_model_lab_run_endpoint.call_with_http_info(**kwargs)

    def list_model_lab_project_artifacts(
        self,
        project_id: int,
    ) -> ModelLabProjectArtifactsResponse:
        """List Model Lab project artifacts.

        List all artifact files for a specific Model Lab project.

        :param project_id: The ID of the Model Lab project.
        :type project_id: int
        :rtype: ModelLabProjectArtifactsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        return self._list_model_lab_project_artifacts_endpoint.call_with_http_info(**kwargs)

    def list_model_lab_project_facet_keys(
        self,
    ) -> ModelLabFacetKeysResponse:
        """List Model Lab project facet keys.

        List all available facet keys for filtering Model Lab projects.

        :rtype: ModelLabFacetKeysResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_model_lab_project_facet_keys_endpoint.call_with_http_info(**kwargs)

    def list_model_lab_project_facet_values(
        self,
        facet_type: ModelLabProjectFacetType,
        facet_name: str,
    ) -> ModelLabFacetValuesResponse:
        """List Model Lab project facet values.

        List available facet values for a specific project facet key.

        :param facet_type: Facet type. Valid values: tag.
        :type facet_type: ModelLabProjectFacetType
        :param facet_name: Facet name.
        :type facet_name: str
        :rtype: ModelLabFacetValuesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["facet_type"] = facet_type

        kwargs["facet_name"] = facet_name

        return self._list_model_lab_project_facet_values_endpoint.call_with_http_info(**kwargs)

    def list_model_lab_projects(
        self,
        *,
        filter: Union[str, UnsetType] = unset,
        filter_owner_id: Union[UUID, UnsetType] = unset,
        filter_tags: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> ModelLabProjectsResponse:
        """List Model Lab projects.

        List all Model Lab projects for the current organization.

        :param filter: Text search filter for project name or description.
        :type filter: str, optional
        :param filter_owner_id: Filter by owner UUID.
        :type filter_owner_id: UUID, optional
        :param filter_tags: Filter by tags. Format: key:value,key2:value2.
        :type filter_tags: str, optional
        :param sort: Sort field. Valid values: name, created_at, updated_at. Prefix with '-' for descending order (e.g., -updated_at).
        :type sort: str, optional
        :param page_size: Number of items per page. Maximum is 100.
        :type page_size: int, optional
        :param page_number: Page number (1-indexed).
        :type page_number: int, optional
        :rtype: ModelLabProjectsResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter is not unset:
            kwargs["filter"] = filter

        if filter_owner_id is not unset:
            kwargs["filter_owner_id"] = filter_owner_id

        if filter_tags is not unset:
            kwargs["filter_tags"] = filter_tags

        if sort is not unset:
            kwargs["sort"] = sort

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        return self._list_model_lab_projects_endpoint.call_with_http_info(**kwargs)

    def list_model_lab_run_artifacts(
        self,
        run_id: int,
        *,
        path: Union[str, UnsetType] = unset,
    ) -> ModelLabRunArtifactsResponse:
        """List Model Lab run artifacts.

        List artifact files for a specific Model Lab run.

        :param run_id: The ID of the Model Lab run.
        :type run_id: int
        :param path: Optional subdirectory path within the run's artifacts.
        :type path: str, optional
        :rtype: ModelLabRunArtifactsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["run_id"] = run_id

        if path is not unset:
            kwargs["path"] = path

        return self._list_model_lab_run_artifacts_endpoint.call_with_http_info(**kwargs)

    def list_model_lab_run_facet_keys(
        self,
        filter_project_id: int,
    ) -> ModelLabFacetKeysResponse:
        """List Model Lab run facet keys.

        List all available facet keys for filtering Model Lab runs.

        :param filter_project_id: Filter by project ID.
        :type filter_project_id: int
        :rtype: ModelLabFacetKeysResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["filter_project_id"] = filter_project_id

        return self._list_model_lab_run_facet_keys_endpoint.call_with_http_info(**kwargs)

    def list_model_lab_run_facet_values(
        self,
        filter_project_id: int,
        facet_type: ModelLabFacetType,
        facet_name: str,
    ) -> ModelLabFacetValuesResponse:
        """List Model Lab run facet values.

        List available facet values for a specific run facet key.

        :param filter_project_id: Filter by project ID.
        :type filter_project_id: int
        :param facet_type: Facet type. Valid values: parameter, attribute, tag, metric.
        :type facet_type: ModelLabFacetType
        :param facet_name: Facet name.
        :type facet_name: str
        :rtype: ModelLabFacetValuesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["filter_project_id"] = filter_project_id

        kwargs["facet_type"] = facet_type

        kwargs["facet_name"] = facet_name

        return self._list_model_lab_run_facet_values_endpoint.call_with_http_info(**kwargs)

    def list_model_lab_runs(
        self,
        *,
        filter_id: Union[str, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        filter_owner_id: Union[str, UnsetType] = unset,
        filter_status: Union[ModelLabRunStatus, UnsetType] = unset,
        filter_project_id: Union[int, UnsetType] = unset,
        filter_tags: Union[str, UnsetType] = unset,
        filter_params: Union[str, UnsetType] = unset,
        filter_parent_run_id: Union[str, UnsetType] = unset,
        pinned_first: Union[bool, UnsetType] = unset,
        include_pinned: Union[bool, UnsetType] = unset,
        include_descendant_matches: Union[bool, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> ModelLabRunsResponse:
        """List Model Lab runs.

        List all Model Lab runs for the current organization.

        :param filter_id: Filter by run ID(s). Comma-separated list for multiple IDs.
        :type filter_id: str, optional
        :param filter: Text search filter for run name or description.
        :type filter: str, optional
        :param filter_owner_id: Filter by owner UUID.
        :type filter_owner_id: str, optional
        :param filter_status: Filter by run status. Valid values: pending, running, completed, failed, killed, unresponsive, paused.
        :type filter_status: ModelLabRunStatus, optional
        :param filter_project_id: Filter by project ID.
        :type filter_project_id: int, optional
        :param filter_tags: Filter by tags. Format: key:value,key2:value2.
        :type filter_tags: str, optional
        :param filter_params: Filter by params. Format: key:value,key2:>0.5,key3:true.
        :type filter_params: str, optional
        :param filter_parent_run_id: Filter by parent run ID. Use 'null' to return only root runs (runs with no parent).
        :type filter_parent_run_id: str, optional
        :param pinned_first: Sort pinned runs before non-pinned runs. Pinned runs are ordered by pin time descending.
        :type pinned_first: bool, optional
        :param include_pinned: Include all runs pinned by the current user, regardless of other filters.
        :type include_pinned: bool, optional
        :param include_descendant_matches: When true, also return runs whose descendants match the active filters. The descendant_match field in each result indicates whether the run was included via a descendant match.
        :type include_descendant_matches: bool, optional
        :param sort: Sort field. Valid values: name, created_at, updated_at, duration. Prefix with '-' for descending order (e.g., -updated_at).
        :type sort: str, optional
        :param page_size: Number of items per page. Maximum is 100.
        :type page_size: int, optional
        :param page_number: Page number (1-indexed).
        :type page_number: int, optional
        :rtype: ModelLabRunsResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_id is not unset:
            kwargs["filter_id"] = filter_id

        if filter is not unset:
            kwargs["filter"] = filter

        if filter_owner_id is not unset:
            kwargs["filter_owner_id"] = filter_owner_id

        if filter_status is not unset:
            kwargs["filter_status"] = filter_status

        if filter_project_id is not unset:
            kwargs["filter_project_id"] = filter_project_id

        if filter_tags is not unset:
            kwargs["filter_tags"] = filter_tags

        if filter_params is not unset:
            kwargs["filter_params"] = filter_params

        if filter_parent_run_id is not unset:
            kwargs["filter_parent_run_id"] = filter_parent_run_id

        if pinned_first is not unset:
            kwargs["pinned_first"] = pinned_first

        if include_pinned is not unset:
            kwargs["include_pinned"] = include_pinned

        if include_descendant_matches is not unset:
            kwargs["include_descendant_matches"] = include_descendant_matches

        if sort is not unset:
            kwargs["sort"] = sort

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        return self._list_model_lab_runs_endpoint.call_with_http_info(**kwargs)

    def pin_model_lab_run(
        self,
        run_id: int,
    ) -> None:
        """Pin a Model Lab run.

        Pin a Model Lab run for the current user.

        :param run_id: The ID of the Model Lab run.
        :type run_id: int
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["run_id"] = run_id

        return self._pin_model_lab_run_endpoint.call_with_http_info(**kwargs)

    def star_model_lab_project(
        self,
        project_id: int,
    ) -> None:
        """Star a Model Lab project.

        Star a Model Lab project for the current user.

        :param project_id: The ID of the Model Lab project.
        :type project_id: int
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        return self._star_model_lab_project_endpoint.call_with_http_info(**kwargs)

    def unpin_model_lab_run(
        self,
        run_id: int,
    ) -> None:
        """Unpin a Model Lab run.

        Remove the pin from a Model Lab run for the current user.

        :param run_id: The ID of the Model Lab run.
        :type run_id: int
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["run_id"] = run_id

        return self._unpin_model_lab_run_endpoint.call_with_http_info(**kwargs)

    def unstar_model_lab_project(
        self,
        project_id: int,
    ) -> None:
        """Remove star from a Model Lab project.

        Remove the star from a Model Lab project for the current user.

        :param project_id: The ID of the Model Lab project.
        :type project_id: int
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        return self._unstar_model_lab_project_endpoint.call_with_http_info(**kwargs)
