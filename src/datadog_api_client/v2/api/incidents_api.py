# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.incidents_response import IncidentsResponse
from datadog_api_client.v2.model.incident_related_object import IncidentRelatedObject
from datadog_api_client.v2.model.incident_response_data import IncidentResponseData
from datadog_api_client.v2.model.incident_response import IncidentResponse
from datadog_api_client.v2.model.incident_create_request import IncidentCreateRequest
from datadog_api_client.v2.model.incident_update_request import IncidentUpdateRequest
from datadog_api_client.v2.model.incident_attachments_response import IncidentAttachmentsResponse
from datadog_api_client.v2.model.incident_attachment_related_object import IncidentAttachmentRelatedObject
from datadog_api_client.v2.model.incident_attachment_attachment_type import IncidentAttachmentAttachmentType
from datadog_api_client.v2.model.incident_attachment_update_response import IncidentAttachmentUpdateResponse
from datadog_api_client.v2.model.incident_attachment_update_request import IncidentAttachmentUpdateRequest


class IncidentsApi:
    """
    Manage incident response.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_incident_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents",
                "operation_id": "create_incident",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (IncidentCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_incident_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}",
                "operation_id": "delete_incident",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_incident_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}",
                "operation_id": "get_incident",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": ([IncidentRelatedObject],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_incident_attachments_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentAttachmentsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/attachments",
                "operation_id": "list_incident_attachments",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": ([IncidentAttachmentRelatedObject],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
                "filter_attachment_type": {
                    "openapi_types": ([IncidentAttachmentAttachmentType],),
                    "attribute": "filter[attachment_type]",
                    "location": "query",
                    "collection_format": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_incidents_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents",
                "operation_id": "list_incidents",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "include": {
                    "openapi_types": ([IncidentRelatedObject],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_incident_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}",
                "operation_id": "update_incident",
                "http_method": "PATCH",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": ([IncidentRelatedObject],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_attachments_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentAttachmentUpdateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/attachments",
                "operation_id": "update_incident_attachments",
                "http_method": "PATCH",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": ([IncidentAttachmentRelatedObject],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentAttachmentUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_incident(
        self,
        body: IncidentCreateRequest,
    ) -> IncidentResponse:
        """Create an incident.

        Create an incident.

        :param body: Incident payload.
        :type body: IncidentCreateRequest
        :rtype: IncidentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_incident_endpoint.call_with_http_info(**kwargs)

    def delete_incident(
        self,
        incident_id: str,
    ) -> None:
        """Delete an existing incident.

        Deletes an existing incident from the users organization.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        return self._delete_incident_endpoint.call_with_http_info(**kwargs)

    def get_incident(
        self,
        incident_id: str,
        *,
        include: Union[List[IncidentRelatedObject], UnsetType] = unset,
    ) -> IncidentResponse:
        """Get the details of an incident.

        Get the details of an incident by ``incident_id``.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param include: Specifies which types of related objects should be included in the response.
        :type include: [IncidentRelatedObject], optional
        :rtype: IncidentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        if include is not unset:
            kwargs["include"] = include

        return self._get_incident_endpoint.call_with_http_info(**kwargs)

    def list_incident_attachments(
        self,
        incident_id: str,
        *,
        include: Union[List[IncidentAttachmentRelatedObject], UnsetType] = unset,
        filter_attachment_type: Union[List[IncidentAttachmentAttachmentType], UnsetType] = unset,
    ) -> IncidentAttachmentsResponse:
        """Get a list of attachments.

        Get all attachments for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param include: Specifies which types of related objects are included in the response.
        :type include: [IncidentAttachmentRelatedObject], optional
        :param filter_attachment_type: Specifies which types of attachments are included in the response.
        :type filter_attachment_type: [IncidentAttachmentAttachmentType], optional
        :rtype: IncidentAttachmentsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        if include is not unset:
            kwargs["include"] = include

        if filter_attachment_type is not unset:
            kwargs["filter_attachment_type"] = filter_attachment_type

        return self._list_incident_attachments_endpoint.call_with_http_info(**kwargs)

    def list_incidents(
        self,
        *,
        include: Union[List[IncidentRelatedObject], UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
    ) -> IncidentsResponse:
        """Get a list of incidents.

        Get all incidents for the user's organization.

        :param include: Specifies which types of related objects should be included in the response.
        :type include: [IncidentRelatedObject], optional
        :param page_size: Size for a given page. The maximum allowed value is 5000.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :rtype: IncidentsResponse
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        return self._list_incidents_endpoint.call_with_http_info(**kwargs)

    def list_incidents_with_pagination(
        self,
        *,
        include: Union[List[IncidentRelatedObject], UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
    ) -> collections.abc.Iterable[IncidentResponseData]:
        """Get a list of incidents.

        Provide a paginated version of :meth:`list_incidents`, returning all items.

        :param include: Specifies which types of related objects should be included in the response.
        :type include: [IncidentRelatedObject], optional
        :param page_size: Size for a given page. The maximum allowed value is 5000.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[IncidentResponseData]
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._list_incidents_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        while True:
            response = endpoint.call_with_http_info(**kwargs)
            for item in get_attribute_from_path(response, "data"):
                yield item
            if len(get_attribute_from_path(response, "data")) < local_page_size:
                break
            set_attribute_from_path(
                kwargs,
                "page_offset",
                get_attribute_from_path(kwargs, "page_offset", 0) + local_page_size,
                endpoint.params_map,
            )

    def update_incident(
        self,
        incident_id: str,
        body: IncidentUpdateRequest,
        *,
        include: Union[List[IncidentRelatedObject], UnsetType] = unset,
    ) -> IncidentResponse:
        """Update an existing incident.

        Updates an incident. Provide only the attributes that should be updated as this request is a partial update.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param body: Incident Payload.
        :type body: IncidentUpdateRequest
        :param include: Specifies which types of related objects should be included in the response.
        :type include: [IncidentRelatedObject], optional
        :rtype: IncidentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_incident_endpoint.call_with_http_info(**kwargs)

    def update_incident_attachments(
        self,
        incident_id: str,
        body: IncidentAttachmentUpdateRequest,
        *,
        include: Union[List[IncidentAttachmentRelatedObject], UnsetType] = unset,
    ) -> IncidentAttachmentUpdateResponse:
        """Create, update, and delete incident attachments.

        The bulk update endpoint for creating, updating, and deleting attachments for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param body: Incident Attachment Payload.
        :type body: IncidentAttachmentUpdateRequest
        :param include: Specifies which types of related objects are included in the response.
        :type include: [IncidentAttachmentRelatedObject], optional
        :rtype: IncidentAttachmentUpdateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_incident_attachments_endpoint.call_with_http_info(**kwargs)
