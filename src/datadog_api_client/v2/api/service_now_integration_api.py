# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UUID,
)
from datadog_api_client.v2.model.service_now_assignment_groups_response import ServiceNowAssignmentGroupsResponse
from datadog_api_client.v2.model.service_now_business_services_response import ServiceNowBusinessServicesResponse
from datadog_api_client.v2.model.service_now_templates_response import ServiceNowTemplatesResponse
from datadog_api_client.v2.model.service_now_template_response import ServiceNowTemplateResponse
from datadog_api_client.v2.model.service_now_template_create_request import ServiceNowTemplateCreateRequest
from datadog_api_client.v2.model.service_now_template_update_request import ServiceNowTemplateUpdateRequest
from datadog_api_client.v2.model.service_now_instances_response import ServiceNowInstancesResponse
from datadog_api_client.v2.model.service_now_users_response import ServiceNowUsersResponse


class ServiceNowIntegrationApi:
    """
    Manage your ServiceNow Integration. ServiceNow is a cloud-based platform that helps organizations manage digital workflows for enterprise operations.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_service_now_template_endpoint = _Endpoint(
            settings={
                "response_type": (ServiceNowTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/servicenow/handles",
                "operation_id": "create_service_now_template",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ServiceNowTemplateCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_service_now_template_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/servicenow/handles/{template_id}",
                "operation_id": "delete_service_now_template",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "template_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_service_now_template_endpoint = _Endpoint(
            settings={
                "response_type": (ServiceNowTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/servicenow/handles/{template_id}",
                "operation_id": "get_service_now_template",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "template_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_service_now_assignment_groups_endpoint = _Endpoint(
            settings={
                "response_type": (ServiceNowAssignmentGroupsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/servicenow/assignment_groups/{instance_id}",
                "operation_id": "list_service_now_assignment_groups",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "instance_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "instance_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_service_now_business_services_endpoint = _Endpoint(
            settings={
                "response_type": (ServiceNowBusinessServicesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/servicenow/business_services/{instance_id}",
                "operation_id": "list_service_now_business_services",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "instance_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "instance_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_service_now_instances_endpoint = _Endpoint(
            settings={
                "response_type": (ServiceNowInstancesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/servicenow/instances",
                "operation_id": "list_service_now_instances",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_service_now_templates_endpoint = _Endpoint(
            settings={
                "response_type": (ServiceNowTemplatesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/servicenow/handles",
                "operation_id": "list_service_now_templates",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_service_now_users_endpoint = _Endpoint(
            settings={
                "response_type": (ServiceNowUsersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/servicenow/users/{instance_id}",
                "operation_id": "list_service_now_users",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "instance_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "instance_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_service_now_template_endpoint = _Endpoint(
            settings={
                "response_type": (ServiceNowTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/servicenow/handles/{template_id}",
                "operation_id": "update_service_now_template",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "template_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ServiceNowTemplateUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_service_now_template(
        self,
        body: ServiceNowTemplateCreateRequest,
    ) -> ServiceNowTemplateResponse:
        """Create ServiceNow template.

        Create a new ServiceNow template.

        :type body: ServiceNowTemplateCreateRequest
        :rtype: ServiceNowTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_service_now_template_endpoint.call_with_http_info(**kwargs)

    def delete_service_now_template(
        self,
        template_id: UUID,
    ) -> None:
        """Delete ServiceNow template.

        Delete a ServiceNow template by ID.

        :param template_id: The ID of the ServiceNow template to delete
        :type template_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id

        return self._delete_service_now_template_endpoint.call_with_http_info(**kwargs)

    def get_service_now_template(
        self,
        template_id: UUID,
    ) -> ServiceNowTemplateResponse:
        """Get ServiceNow template.

        Get a ServiceNow template by ID.

        :param template_id: The ID of the ServiceNow template to retrieve
        :type template_id: UUID
        :rtype: ServiceNowTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id

        return self._get_service_now_template_endpoint.call_with_http_info(**kwargs)

    def list_service_now_assignment_groups(
        self,
        instance_id: UUID,
    ) -> ServiceNowAssignmentGroupsResponse:
        """List ServiceNow assignment groups.

        Get all assignment groups for a ServiceNow instance.

        :param instance_id: The ID of the ServiceNow instance
        :type instance_id: UUID
        :rtype: ServiceNowAssignmentGroupsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["instance_id"] = instance_id

        return self._list_service_now_assignment_groups_endpoint.call_with_http_info(**kwargs)

    def list_service_now_business_services(
        self,
        instance_id: UUID,
    ) -> ServiceNowBusinessServicesResponse:
        """List ServiceNow business services.

        Get all business services for a ServiceNow instance.

        :param instance_id: The ID of the ServiceNow instance
        :type instance_id: UUID
        :rtype: ServiceNowBusinessServicesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["instance_id"] = instance_id

        return self._list_service_now_business_services_endpoint.call_with_http_info(**kwargs)

    def list_service_now_instances(
        self,
    ) -> ServiceNowInstancesResponse:
        """List ServiceNow instances.

        Get all ServiceNow instances for the organization.

        :rtype: ServiceNowInstancesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_service_now_instances_endpoint.call_with_http_info(**kwargs)

    def list_service_now_templates(
        self,
    ) -> ServiceNowTemplatesResponse:
        """List ServiceNow templates.

        Get all ServiceNow templates for the organization.

        :rtype: ServiceNowTemplatesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_service_now_templates_endpoint.call_with_http_info(**kwargs)

    def list_service_now_users(
        self,
        instance_id: UUID,
    ) -> ServiceNowUsersResponse:
        """List ServiceNow users.

        Get all users for a ServiceNow instance.

        :param instance_id: The ID of the ServiceNow instance
        :type instance_id: UUID
        :rtype: ServiceNowUsersResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["instance_id"] = instance_id

        return self._list_service_now_users_endpoint.call_with_http_info(**kwargs)

    def update_service_now_template(
        self,
        template_id: UUID,
        body: ServiceNowTemplateUpdateRequest,
    ) -> ServiceNowTemplateResponse:
        """Update ServiceNow template.

        Update a ServiceNow template by ID.

        :param template_id: The ID of the ServiceNow template to update
        :type template_id: UUID
        :type body: ServiceNowTemplateUpdateRequest
        :rtype: ServiceNowTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id

        kwargs["body"] = body

        return self._update_service_now_template_endpoint.call_with_http_info(**kwargs)
