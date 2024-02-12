# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.projects_response import ProjectsResponse
from datadog_api_client.v2.model.project_response import ProjectResponse
from datadog_api_client.v2.model.project_create_request import ProjectCreateRequest


class CasesProjectsApi:
    """
    View and manage project within Case Management
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_project_endpoint = _Endpoint(
            settings={
                "response_type": (ProjectResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects",
                "operation_id": "create_project",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProjectCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_project_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}",
                "operation_id": "delete_project",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_project_endpoint = _Endpoint(
            settings={
                "response_type": (ProjectResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects/{project_id}",
                "operation_id": "get_project",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "project_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_projects_endpoint = _Endpoint(
            settings={
                "response_type": (ProjectsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/projects",
                "operation_id": "get_projects",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def create_project(
        self,
        body: ProjectCreateRequest,
    ) -> ProjectResponse:
        """Create a project.

        Create a project.

        :param body: Project payload
        :type body: ProjectCreateRequest
        :rtype: ProjectResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_project_endpoint.call_with_http_info(**kwargs)

    def delete_project(
        self,
        project_id: str,
    ) -> None:
        """Remove a project.

        Remove a project using the project's ``id``.

        :param project_id: Project UUID
        :type project_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        return self._delete_project_endpoint.call_with_http_info(**kwargs)

    def get_project(
        self,
        project_id: str,
    ) -> ProjectResponse:
        """Get the details of a project.

        Get the details of a project by ``project_id``.

        :param project_id: Project UUID
        :type project_id: str
        :rtype: ProjectResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["project_id"] = project_id

        return self._get_project_endpoint.call_with_http_info(**kwargs)

    def get_projects(
        self,
    ) -> ProjectsResponse:
        """Get all projects.

        Get all projects.

        :rtype: ProjectsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_projects_endpoint.call_with_http_info(**kwargs)
