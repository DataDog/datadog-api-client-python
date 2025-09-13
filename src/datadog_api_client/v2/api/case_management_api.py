# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.cases_response import CasesResponse
from datadog_api_client.v2.model.case_sortable_field import CaseSortableField
from datadog_api_client.v2.model.case import Case
from datadog_api_client.v2.model.case_response import CaseResponse
from datadog_api_client.v2.model.case_create_request import CaseCreateRequest
from datadog_api_client.v2.model.projects_response import ProjectsResponse
from datadog_api_client.v2.model.project_response import ProjectResponse
from datadog_api_client.v2.model.project_create_request import ProjectCreateRequest
from datadog_api_client.v2.model.case_empty_request import CaseEmptyRequest
from datadog_api_client.v2.model.case_assign_request import CaseAssignRequest
from datadog_api_client.v2.model.case_update_attributes_request import CaseUpdateAttributesRequest
from datadog_api_client.v2.model.timeline_response import TimelineResponse
from datadog_api_client.v2.model.case_comment_request import CaseCommentRequest
from datadog_api_client.v2.model.case_update_custom_attribute_request import CaseUpdateCustomAttributeRequest
from datadog_api_client.v2.model.case_update_description_request import CaseUpdateDescriptionRequest
from datadog_api_client.v2.model.case_update_priority_request import CaseUpdatePriorityRequest
from datadog_api_client.v2.model.case_update_status_request import CaseUpdateStatusRequest
from datadog_api_client.v2.model.case_update_title_request import CaseUpdateTitleRequest


class CaseManagementApi:
    """
    View and manage cases and projects within Case Management. See the `Case Management page <https://docs.datadoghq.com/service_management/case_management/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._archive_case_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/archive",
                "operation_id": "archive_case",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseEmptyRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._assign_case_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/assign",
                "operation_id": "assign_case",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseAssignRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._comment_case_endpoint = _Endpoint(
            settings={
                "response_type": (TimelineResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cases/{case_id}/comment",
                "operation_id": "comment_case",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseCommentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_case_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases",
                "operation_id": "create_case",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CaseCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

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

        self._delete_case_comment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cases/{case_id}/comment/{cell_id}",
                "operation_id": "delete_case_comment",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "cell_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "cell_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_case_custom_attribute_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}",
                "operation_id": "delete_case_custom_attribute",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "custom_attribute_key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "custom_attribute_key",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
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

        self._get_case_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}",
                "operation_id": "get_case",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
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

        self._search_cases_endpoint = _Endpoint(
            settings={
                "response_type": (CasesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases",
                "operation_id": "search_cases",
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
                "sort_field": {
                    "openapi_types": (CaseSortableField,),
                    "attribute": "sort[field]",
                    "location": "query",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
                "sort_asc": {
                    "openapi_types": (bool,),
                    "attribute": "sort[asc]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._unarchive_case_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/unarchive",
                "operation_id": "unarchive_case",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseEmptyRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._unassign_case_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/unassign",
                "operation_id": "unassign_case",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseEmptyRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_attributes_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/attributes",
                "operation_id": "update_attributes",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseUpdateAttributesRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_case_custom_attribute_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/custom_attributes/{custom_attribute_key}",
                "operation_id": "update_case_custom_attribute",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "custom_attribute_key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "custom_attribute_key",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseUpdateCustomAttributeRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_case_description_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/description",
                "operation_id": "update_case_description",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseUpdateDescriptionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_case_title_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/title",
                "operation_id": "update_case_title",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseUpdateTitleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_priority_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/priority",
                "operation_id": "update_priority",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseUpdatePriorityRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_status_endpoint = _Endpoint(
            settings={
                "response_type": (CaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cases/{case_id}/status",
                "operation_id": "update_status",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CaseUpdateStatusRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def archive_case(
        self,
        case_id: str,
        body: CaseEmptyRequest,
    ) -> CaseResponse:
        """Archive case.

        Archive case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Archive case payload
        :type body: CaseEmptyRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._archive_case_endpoint.call_with_http_info(**kwargs)

    def assign_case(
        self,
        case_id: str,
        body: CaseAssignRequest,
    ) -> CaseResponse:
        """Assign case.

        Assign case to a user

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Assign case payload
        :type body: CaseAssignRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._assign_case_endpoint.call_with_http_info(**kwargs)

    def comment_case(
        self,
        case_id: str,
        body: CaseCommentRequest,
    ) -> TimelineResponse:
        """Comment case.

        Comment case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case comment payload
        :type body: CaseCommentRequest
        :rtype: TimelineResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._comment_case_endpoint.call_with_http_info(**kwargs)

    def create_case(
        self,
        body: CaseCreateRequest,
    ) -> CaseResponse:
        """Create a case.

        Create a Case

        :param body: Case payload
        :type body: CaseCreateRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_case_endpoint.call_with_http_info(**kwargs)

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

    def delete_case_comment(
        self,
        case_id: str,
        cell_id: str,
    ) -> None:
        """Delete case comment.

        Delete case comment

        :param case_id: Case's UUID or key
        :type case_id: str
        :param cell_id: Timeline cell's UUID
        :type cell_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["cell_id"] = cell_id

        return self._delete_case_comment_endpoint.call_with_http_info(**kwargs)

    def delete_case_custom_attribute(
        self,
        case_id: str,
        custom_attribute_key: str,
    ) -> CaseResponse:
        """Delete custom attribute from case.

        Delete custom attribute from case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param custom_attribute_key: Case Custom attribute's key
        :type custom_attribute_key: str
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["custom_attribute_key"] = custom_attribute_key

        return self._delete_case_custom_attribute_endpoint.call_with_http_info(**kwargs)

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

    def get_case(
        self,
        case_id: str,
    ) -> CaseResponse:
        """Get the details of a case.

        Get the details of case by ``case_id``

        :param case_id: Case's UUID or key
        :type case_id: str
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        return self._get_case_endpoint.call_with_http_info(**kwargs)

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

    def search_cases(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort_field: Union[CaseSortableField, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        sort_asc: Union[bool, UnsetType] = unset,
    ) -> CasesResponse:
        """Search cases.

        Search cases.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort_field: Specify which field to sort
        :type sort_field: CaseSortableField, optional
        :param filter: Search query
        :type filter: str, optional
        :param sort_asc: Specify if order is ascending or not
        :type sort_asc: bool, optional
        :rtype: CasesResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort_field is not unset:
            kwargs["sort_field"] = sort_field

        if filter is not unset:
            kwargs["filter"] = filter

        if sort_asc is not unset:
            kwargs["sort_asc"] = sort_asc

        return self._search_cases_endpoint.call_with_http_info(**kwargs)

    def search_cases_with_pagination(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort_field: Union[CaseSortableField, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        sort_asc: Union[bool, UnsetType] = unset,
    ) -> collections.abc.Iterable[Case]:
        """Search cases.

        Provide a paginated version of :meth:`search_cases`, returning all items.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort_field: Specify which field to sort
        :type sort_field: CaseSortableField, optional
        :param filter: Search query
        :type filter: str, optional
        :param sort_asc: Specify if order is ascending or not
        :type sort_asc: bool, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[Case]
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort_field is not unset:
            kwargs["sort_field"] = sort_field

        if filter is not unset:
            kwargs["filter"] = filter

        if sort_asc is not unset:
            kwargs["sort_asc"] = sort_asc

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._search_cases_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_param": "page_number",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def unarchive_case(
        self,
        case_id: str,
        body: CaseEmptyRequest,
    ) -> CaseResponse:
        """Unarchive case.

        Unarchive case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Unarchive case payload
        :type body: CaseEmptyRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._unarchive_case_endpoint.call_with_http_info(**kwargs)

    def unassign_case(
        self,
        case_id: str,
        body: CaseEmptyRequest,
    ) -> CaseResponse:
        """Unassign case.

        Unassign case

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Unassign case payload
        :type body: CaseEmptyRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._unassign_case_endpoint.call_with_http_info(**kwargs)

    def update_attributes(
        self,
        case_id: str,
        body: CaseUpdateAttributesRequest,
    ) -> CaseResponse:
        """Update case attributes.

        Update case attributes

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case attributes update payload
        :type body: CaseUpdateAttributesRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._update_attributes_endpoint.call_with_http_info(**kwargs)

    def update_case_custom_attribute(
        self,
        case_id: str,
        custom_attribute_key: str,
        body: CaseUpdateCustomAttributeRequest,
    ) -> CaseResponse:
        """Update case custom attribute.

        Update case custom attribute

        :param case_id: Case's UUID or key
        :type case_id: str
        :param custom_attribute_key: Case Custom attribute's key
        :type custom_attribute_key: str
        :param body: Update case custom attribute payload
        :type body: CaseUpdateCustomAttributeRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["custom_attribute_key"] = custom_attribute_key

        kwargs["body"] = body

        return self._update_case_custom_attribute_endpoint.call_with_http_info(**kwargs)

    def update_case_description(
        self,
        case_id: str,
        body: CaseUpdateDescriptionRequest,
    ) -> CaseResponse:
        """Update case description.

        Update case description

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case description update payload
        :type body: CaseUpdateDescriptionRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._update_case_description_endpoint.call_with_http_info(**kwargs)

    def update_case_title(
        self,
        case_id: str,
        body: CaseUpdateTitleRequest,
    ) -> CaseResponse:
        """Update case title.

        Update case title

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case title update payload
        :type body: CaseUpdateTitleRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._update_case_title_endpoint.call_with_http_info(**kwargs)

    def update_priority(
        self,
        case_id: str,
        body: CaseUpdatePriorityRequest,
    ) -> CaseResponse:
        """Update case priority.

        Update case priority

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case priority update payload
        :type body: CaseUpdatePriorityRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._update_priority_endpoint.call_with_http_info(**kwargs)

    def update_status(
        self,
        case_id: str,
        body: CaseUpdateStatusRequest,
    ) -> CaseResponse:
        """Update case status.

        Update case status

        :param case_id: Case's UUID or key
        :type case_id: str
        :param body: Case status update payload
        :type body: CaseUpdateStatusRequest
        :rtype: CaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._update_status_endpoint.call_with_http_info(**kwargs)
