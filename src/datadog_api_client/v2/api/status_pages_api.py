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
    UUID,
)
from datadog_api_client.v2.model.status_page_array import StatusPageArray
from datadog_api_client.v2.model.status_page import StatusPage
from datadog_api_client.v2.model.create_status_page_request import CreateStatusPageRequest
from datadog_api_client.v2.model.degradation_array import DegradationArray
from datadog_api_client.v2.model.patch_status_page_request import PatchStatusPageRequest
from datadog_api_client.v2.model.status_pages_component_array import StatusPagesComponentArray
from datadog_api_client.v2.model.status_pages_component import StatusPagesComponent
from datadog_api_client.v2.model.create_component_request import CreateComponentRequest
from datadog_api_client.v2.model.patch_component_request import PatchComponentRequest
from datadog_api_client.v2.model.degradation import Degradation
from datadog_api_client.v2.model.create_degradation_request import CreateDegradationRequest
from datadog_api_client.v2.model.patch_degradation_request import PatchDegradationRequest


class StatusPagesApi:
    """
    Auto-generated tag Status Pages
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_component_endpoint = _Endpoint(
            settings={
                "response_type": (StatusPagesComponent,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages/{page_id}/components",
                "operation_id": "create_component",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "page_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CreateComponentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_degradation_endpoint = _Endpoint(
            settings={
                "response_type": (Degradation,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages/{page_id}/degradations",
                "operation_id": "create_degradation",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "page_id",
                    "location": "path",
                },
                "notify_subscribers": {
                    "openapi_types": (bool,),
                    "attribute": "notify_subscribers",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CreateDegradationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_status_page_endpoint = _Endpoint(
            settings={
                "response_type": (StatusPage,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages",
                "operation_id": "create_status_page",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CreateStatusPageRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_component_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages/{page_id}/components/{component_id}",
                "operation_id": "delete_component",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "page_id",
                    "location": "path",
                },
                "component_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "component_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_degradation_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages/{page_id}/degradations/{degradation_id}",
                "operation_id": "delete_degradation",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "page_id",
                    "location": "path",
                },
                "degradation_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "degradation_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_status_page_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages/{page_id}",
                "operation_id": "delete_status_page",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "page_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_component_endpoint = _Endpoint(
            settings={
                "response_type": (StatusPagesComponent,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages/{page_id}/components/{component_id}",
                "operation_id": "get_component",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "page_id",
                    "location": "path",
                },
                "component_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "component_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_degradation_endpoint = _Endpoint(
            settings={
                "response_type": (Degradation,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages/{page_id}/degradations/{degradation_id}",
                "operation_id": "get_degradation",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "page_id",
                    "location": "path",
                },
                "degradation_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "degradation_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_status_page_endpoint = _Endpoint(
            settings={
                "response_type": (StatusPage,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages/{page_id}",
                "operation_id": "get_status_page",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "page_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_components_endpoint = _Endpoint(
            settings={
                "response_type": (StatusPagesComponentArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages/{page_id}/components",
                "operation_id": "list_components",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "page_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_degradations_endpoint = _Endpoint(
            settings={
                "response_type": (DegradationArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages/degradations",
                "operation_id": "list_degradations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_page_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[page_id]",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "filter_status": {
                    "openapi_types": (str,),
                    "attribute": "filter[status]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_status_pages_endpoint = _Endpoint(
            settings={
                "response_type": (StatusPageArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages",
                "operation_id": "list_status_pages",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_component_endpoint = _Endpoint(
            settings={
                "response_type": (StatusPagesComponent,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages/{page_id}/components/{component_id}",
                "operation_id": "update_component",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "page_id",
                    "location": "path",
                },
                "component_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "component_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (PatchComponentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_degradation_endpoint = _Endpoint(
            settings={
                "response_type": (Degradation,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages/{page_id}/degradations/{degradation_id}",
                "operation_id": "update_degradation",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "page_id",
                    "location": "path",
                },
                "notify_subscribers": {
                    "openapi_types": (bool,),
                    "attribute": "notify_subscribers",
                    "location": "query",
                },
                "degradation_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "degradation_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (PatchDegradationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_status_page_endpoint = _Endpoint(
            settings={
                "response_type": (StatusPage,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages/{page_id}",
                "operation_id": "update_status_page",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "delete_subscribers": {
                    "openapi_types": (bool,),
                    "attribute": "delete_subscribers",
                    "location": "query",
                },
                "page_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "page_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (PatchStatusPageRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_component(
        self,
        page_id: UUID,
        body: CreateComponentRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> StatusPagesComponent:
        """Create component.

        Creates a new component.

        :param page_id: The ID of the status page.
        :type page_id: UUID
        :type body: CreateComponentRequest
        :param include: Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page, group.
        :type include: str, optional
        :rtype: StatusPagesComponent
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._create_component_endpoint.call_with_http_info(**kwargs)

    def create_degradation(
        self,
        page_id: UUID,
        body: CreateDegradationRequest,
        *,
        notify_subscribers: Union[bool, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
    ) -> Degradation:
        """Create degradation.

        Creates a new degradation.

        :param page_id: The ID of the status page.
        :type page_id: UUID
        :type body: CreateDegradationRequest
        :param notify_subscribers: Whether to notify page subscribers of the degradation.
        :type notify_subscribers: bool, optional
        :param include: Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page.
        :type include: str, optional
        :rtype: Degradation
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        if notify_subscribers is not unset:
            kwargs["notify_subscribers"] = notify_subscribers

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._create_degradation_endpoint.call_with_http_info(**kwargs)

    def create_status_page(
        self,
        body: CreateStatusPageRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> StatusPage:
        """Create status page.

        Creates a new status page.

        :type body: CreateStatusPageRequest
        :param include: Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user.
        :type include: str, optional
        :rtype: StatusPage
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._create_status_page_endpoint.call_with_http_info(**kwargs)

    def delete_component(
        self,
        page_id: UUID,
        component_id: UUID,
    ) -> None:
        """Delete component.

        Deletes a component by its ID.

        :param page_id: The ID of the status page.
        :type page_id: UUID
        :param component_id: The ID of the component.
        :type component_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        kwargs["component_id"] = component_id

        return self._delete_component_endpoint.call_with_http_info(**kwargs)

    def delete_degradation(
        self,
        page_id: UUID,
        degradation_id: UUID,
    ) -> None:
        """Delete degradation.

        Deletes a degradation by its ID.

        :param page_id: The ID of the status page.
        :type page_id: UUID
        :param degradation_id: The ID of the degradation.
        :type degradation_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        kwargs["degradation_id"] = degradation_id

        return self._delete_degradation_endpoint.call_with_http_info(**kwargs)

    def delete_status_page(
        self,
        page_id: UUID,
    ) -> None:
        """Delete status page.

        Deletes a status page by its ID.

        :param page_id: The ID of the status page.
        :type page_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        return self._delete_status_page_endpoint.call_with_http_info(**kwargs)

    def get_component(
        self,
        page_id: UUID,
        component_id: UUID,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> StatusPagesComponent:
        """Get component.

        Retrieves a specific component by its ID.

        :param page_id: The ID of the status page.
        :type page_id: UUID
        :param component_id: The ID of the component.
        :type component_id: UUID
        :param include: Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page, group.
        :type include: str, optional
        :rtype: StatusPagesComponent
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        kwargs["component_id"] = component_id

        if include is not unset:
            kwargs["include"] = include

        return self._get_component_endpoint.call_with_http_info(**kwargs)

    def get_degradation(
        self,
        page_id: UUID,
        degradation_id: UUID,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> Degradation:
        """Get degradation.

        Retrieves a specific degradation by its ID.

        :param page_id: The ID of the status page.
        :type page_id: UUID
        :param degradation_id: The ID of the degradation.
        :type degradation_id: UUID
        :param include: Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page.
        :type include: str, optional
        :rtype: Degradation
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        kwargs["degradation_id"] = degradation_id

        if include is not unset:
            kwargs["include"] = include

        return self._get_degradation_endpoint.call_with_http_info(**kwargs)

    def get_status_page(
        self,
        page_id: UUID,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> StatusPage:
        """Get status page.

        Retrieves a specific status page by its ID.

        :param page_id: The ID of the status page.
        :type page_id: UUID
        :param include: Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user.
        :type include: str, optional
        :rtype: StatusPage
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        if include is not unset:
            kwargs["include"] = include

        return self._get_status_page_endpoint.call_with_http_info(**kwargs)

    def list_components(
        self,
        page_id: UUID,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> StatusPagesComponentArray:
        """List components.

        Lists all components for a status page.

        :param page_id: The ID of the status page.
        :type page_id: UUID
        :param include: Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page, group.
        :type include: str, optional
        :rtype: StatusPagesComponentArray
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        if include is not unset:
            kwargs["include"] = include

        return self._list_components_endpoint.call_with_http_info(**kwargs)

    def list_degradations(
        self,
        *,
        filter_page_id: Union[str, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
        filter_status: Union[str, UnsetType] = unset,
    ) -> DegradationArray:
        """List degradations.

        Lists all degradations for the organization. Optionally filter by status and page.

        :param filter_page_id: Optional page id filter.
        :type filter_page_id: str, optional
        :param page_offset: Offset to use as the start of the page.
        :type page_offset: int, optional
        :param page_limit: The number of degradations to return per page.
        :type page_limit: int, optional
        :param include: Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page.
        :type include: str, optional
        :param filter_status: Optional degradation status filter. Supported values: investigating, identified, monitoring, resolved.
        :type filter_status: str, optional
        :rtype: DegradationArray
        """
        kwargs: Dict[str, Any] = {}
        if filter_page_id is not unset:
            kwargs["filter_page_id"] = filter_page_id

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if include is not unset:
            kwargs["include"] = include

        if filter_status is not unset:
            kwargs["filter_status"] = filter_status

        return self._list_degradations_endpoint.call_with_http_info(**kwargs)

    def list_status_pages(
        self,
        *,
        page_offset: Union[int, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
    ) -> StatusPageArray:
        """List status pages.

        Lists all status pages for the organization.

        :param page_offset: Offset to use as the start of the page.
        :type page_offset: int, optional
        :param page_limit: The number of status pages to return per page.
        :type page_limit: int, optional
        :param include: Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user.
        :type include: str, optional
        :rtype: StatusPageArray
        """
        kwargs: Dict[str, Any] = {}
        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if include is not unset:
            kwargs["include"] = include

        return self._list_status_pages_endpoint.call_with_http_info(**kwargs)

    def update_component(
        self,
        page_id: UUID,
        component_id: UUID,
        body: PatchComponentRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> StatusPagesComponent:
        """Update component.

        Updates an existing component's attributes.

        :param page_id: The ID of the status page.
        :type page_id: UUID
        :param component_id: The ID of the component.
        :type component_id: UUID
        :type body: PatchComponentRequest
        :param include: Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page, group.
        :type include: str, optional
        :rtype: StatusPagesComponent
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        kwargs["component_id"] = component_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_component_endpoint.call_with_http_info(**kwargs)

    def update_degradation(
        self,
        page_id: UUID,
        degradation_id: UUID,
        body: PatchDegradationRequest,
        *,
        notify_subscribers: Union[bool, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
    ) -> Degradation:
        """Update degradation.

        Updates an existing degradation's attributes.

        :param page_id: The ID of the status page.
        :type page_id: UUID
        :param degradation_id: The ID of the degradation.
        :type degradation_id: UUID
        :type body: PatchDegradationRequest
        :param notify_subscribers: Whether to notify page subscribers of the degradation.
        :type notify_subscribers: bool, optional
        :param include: Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page.
        :type include: str, optional
        :rtype: Degradation
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        if notify_subscribers is not unset:
            kwargs["notify_subscribers"] = notify_subscribers

        kwargs["degradation_id"] = degradation_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_degradation_endpoint.call_with_http_info(**kwargs)

    def update_status_page(
        self,
        page_id: UUID,
        body: PatchStatusPageRequest,
        *,
        delete_subscribers: Union[bool, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
    ) -> StatusPage:
        """Update status page.

        Updates an existing status page's attributes.

        :param page_id: The ID of the status page.
        :type page_id: UUID
        :type body: PatchStatusPageRequest
        :param delete_subscribers: Whether to delete existing subscribers when updating a status page's type.
        :type delete_subscribers: bool, optional
        :param include: Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user.
        :type include: str, optional
        :rtype: StatusPage
        """
        kwargs: Dict[str, Any] = {}
        if delete_subscribers is not unset:
            kwargs["delete_subscribers"] = delete_subscribers

        kwargs["page_id"] = page_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_status_page_endpoint.call_with_http_info(**kwargs)
