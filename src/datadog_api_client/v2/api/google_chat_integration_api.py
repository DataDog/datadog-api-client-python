# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.google_chat_organizations_response import GoogleChatOrganizationsResponse
from datadog_api_client.v2.model.google_chat_app_named_space_response import GoogleChatAppNamedSpaceResponse
from datadog_api_client.v2.model.google_chat_organization_response import GoogleChatOrganizationResponse
from datadog_api_client.v2.model.google_chat_delegated_user_response import GoogleChatDelegatedUserResponse
from datadog_api_client.v2.model.google_chat_organization_handles_response import GoogleChatOrganizationHandlesResponse
from datadog_api_client.v2.model.google_chat_organization_handle_response import GoogleChatOrganizationHandleResponse
from datadog_api_client.v2.model.google_chat_create_organization_handle_request import (
    GoogleChatCreateOrganizationHandleRequest,
)
from datadog_api_client.v2.model.google_chat_update_organization_handle_request import (
    GoogleChatUpdateOrganizationHandleRequest,
)
from datadog_api_client.v2.model.google_chat_target_audiences_response import GoogleChatTargetAudiencesResponse
from datadog_api_client.v2.model.google_chat_target_audience_response import GoogleChatTargetAudienceResponse
from datadog_api_client.v2.model.google_chat_target_audience_create_request import GoogleChatTargetAudienceCreateRequest
from datadog_api_client.v2.model.google_chat_target_audience_update_request import GoogleChatTargetAudienceUpdateRequest


class GoogleChatIntegrationApi:
    """
    Configure your `Datadog Google Chat integration <https://docs.datadoghq.com/integrations/google-hangouts-chat/>`_
    directly through the Datadog API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_google_chat_target_audience_endpoint = _Endpoint(
            settings={
                "response_type": (GoogleChatTargetAudienceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations/{organization_binding_id}/target-audiences",
                "operation_id": "create_google_chat_target_audience",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "organization_binding_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "organization_binding_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (GoogleChatTargetAudienceCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_organization_handle_endpoint = _Endpoint(
            settings={
                "response_type": (GoogleChatOrganizationHandleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations/{organization_binding_id}/organization-handles",
                "operation_id": "create_organization_handle",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "organization_binding_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "organization_binding_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (GoogleChatCreateOrganizationHandleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_google_chat_delegated_user_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations/{organization_binding_id}/delegated-user",
                "operation_id": "delete_google_chat_delegated_user",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "organization_binding_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "organization_binding_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_google_chat_organization_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations/{organization_binding_id}",
                "operation_id": "delete_google_chat_organization",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "organization_binding_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "organization_binding_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_google_chat_target_audience_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations/{organization_binding_id}/target-audiences/{target_audience_id}",
                "operation_id": "delete_google_chat_target_audience",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "organization_binding_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "organization_binding_id",
                    "location": "path",
                },
                "target_audience_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "target_audience_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_organization_handle_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations/{organization_binding_id}/organization-handles/{handle_id}",
                "operation_id": "delete_organization_handle",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "organization_binding_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "organization_binding_id",
                    "location": "path",
                },
                "handle_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "handle_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_google_chat_delegated_user_endpoint = _Endpoint(
            settings={
                "response_type": (GoogleChatDelegatedUserResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations/{organization_binding_id}/delegated-user",
                "operation_id": "get_google_chat_delegated_user",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "organization_binding_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "organization_binding_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_google_chat_organization_endpoint = _Endpoint(
            settings={
                "response_type": (GoogleChatOrganizationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations/{organization_binding_id}",
                "operation_id": "get_google_chat_organization",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "organization_binding_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "organization_binding_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_google_chat_target_audience_endpoint = _Endpoint(
            settings={
                "response_type": (GoogleChatTargetAudienceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations/{organization_binding_id}/target-audiences/{target_audience_id}",
                "operation_id": "get_google_chat_target_audience",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "organization_binding_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "organization_binding_id",
                    "location": "path",
                },
                "target_audience_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "target_audience_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_organization_handle_endpoint = _Endpoint(
            settings={
                "response_type": (GoogleChatOrganizationHandleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations/{organization_binding_id}/organization-handles/{handle_id}",
                "operation_id": "get_organization_handle",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "organization_binding_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "organization_binding_id",
                    "location": "path",
                },
                "handle_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "handle_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_space_by_display_name_endpoint = _Endpoint(
            settings={
                "response_type": (GoogleChatAppNamedSpaceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations/app/named-spaces/{domain_name}/{space_display_name}",
                "operation_id": "get_space_by_display_name",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "domain_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "domain_name",
                    "location": "path",
                },
                "space_display_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "space_display_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_google_chat_organizations_endpoint = _Endpoint(
            settings={
                "response_type": (GoogleChatOrganizationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations",
                "operation_id": "list_google_chat_organizations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_google_chat_target_audiences_endpoint = _Endpoint(
            settings={
                "response_type": (GoogleChatTargetAudiencesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations/{organization_binding_id}/target-audiences",
                "operation_id": "list_google_chat_target_audiences",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "organization_binding_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "organization_binding_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_organization_handles_endpoint = _Endpoint(
            settings={
                "response_type": (GoogleChatOrganizationHandlesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations/{organization_binding_id}/organization-handles",
                "operation_id": "list_organization_handles",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "organization_binding_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "organization_binding_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_google_chat_target_audience_endpoint = _Endpoint(
            settings={
                "response_type": (GoogleChatTargetAudienceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations/{organization_binding_id}/target-audiences/{target_audience_id}",
                "operation_id": "update_google_chat_target_audience",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "organization_binding_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "organization_binding_id",
                    "location": "path",
                },
                "target_audience_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "target_audience_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (GoogleChatTargetAudienceUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_organization_handle_endpoint = _Endpoint(
            settings={
                "response_type": (GoogleChatOrganizationHandleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/google-chat/organizations/{organization_binding_id}/organization-handles/{handle_id}",
                "operation_id": "update_organization_handle",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "organization_binding_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "organization_binding_id",
                    "location": "path",
                },
                "handle_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "handle_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (GoogleChatUpdateOrganizationHandleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_google_chat_target_audience(
        self,
        organization_binding_id: str,
        body: GoogleChatTargetAudienceCreateRequest,
    ) -> GoogleChatTargetAudienceResponse:
        """Create a target audience.

        Create a target audience for a Google Chat organization binding in the Datadog Google Chat integration.

        :param organization_binding_id: Your organization binding ID.
        :type organization_binding_id: str
        :param body: Target audience payload.
        :type body: GoogleChatTargetAudienceCreateRequest
        :rtype: GoogleChatTargetAudienceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["organization_binding_id"] = organization_binding_id

        kwargs["body"] = body

        return self._create_google_chat_target_audience_endpoint.call_with_http_info(**kwargs)

    def create_organization_handle(
        self,
        organization_binding_id: str,
        body: GoogleChatCreateOrganizationHandleRequest,
    ) -> GoogleChatOrganizationHandleResponse:
        """Create organization handle.

        Create an organization handle in the Datadog Google Chat integration.

        :param organization_binding_id: Your organization binding ID.
        :type organization_binding_id: str
        :param body: Organization handle payload.
        :type body: GoogleChatCreateOrganizationHandleRequest
        :rtype: GoogleChatOrganizationHandleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["organization_binding_id"] = organization_binding_id

        kwargs["body"] = body

        return self._create_organization_handle_endpoint.call_with_http_info(**kwargs)

    def delete_google_chat_delegated_user(
        self,
        organization_binding_id: str,
    ) -> None:
        """Delete the delegated user.

        Delete the delegated user for a Google Chat organization binding from the Datadog Google Chat integration.

        :param organization_binding_id: Your organization binding ID.
        :type organization_binding_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["organization_binding_id"] = organization_binding_id

        return self._delete_google_chat_delegated_user_endpoint.call_with_http_info(**kwargs)

    def delete_google_chat_organization(
        self,
        organization_binding_id: str,
    ) -> None:
        """Delete a Google Chat organization binding.

        Delete a Google Chat organization binding from the Datadog Google Chat integration.

        :param organization_binding_id: Your organization binding ID.
        :type organization_binding_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["organization_binding_id"] = organization_binding_id

        return self._delete_google_chat_organization_endpoint.call_with_http_info(**kwargs)

    def delete_google_chat_target_audience(
        self,
        organization_binding_id: str,
        target_audience_id: str,
    ) -> None:
        """Delete a target audience.

        Delete a target audience from a Google Chat organization binding in the Datadog Google Chat integration.

        :param organization_binding_id: Your organization binding ID.
        :type organization_binding_id: str
        :param target_audience_id: Your target audience ID.
        :type target_audience_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["organization_binding_id"] = organization_binding_id

        kwargs["target_audience_id"] = target_audience_id

        return self._delete_google_chat_target_audience_endpoint.call_with_http_info(**kwargs)

    def delete_organization_handle(
        self,
        organization_binding_id: str,
        handle_id: str,
    ) -> None:
        """Delete organization handle.

        Delete an organization handle from the Datadog Google Chat integration.

        :param organization_binding_id: Your organization binding ID.
        :type organization_binding_id: str
        :param handle_id: Your organization handle ID.
        :type handle_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["organization_binding_id"] = organization_binding_id

        kwargs["handle_id"] = handle_id

        return self._delete_organization_handle_endpoint.call_with_http_info(**kwargs)

    def get_google_chat_delegated_user(
        self,
        organization_binding_id: str,
    ) -> GoogleChatDelegatedUserResponse:
        """Get the delegated user.

        Get the delegated user for a Google Chat organization binding in the Datadog Google Chat integration.

        :param organization_binding_id: Your organization binding ID.
        :type organization_binding_id: str
        :rtype: GoogleChatDelegatedUserResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["organization_binding_id"] = organization_binding_id

        return self._get_google_chat_delegated_user_endpoint.call_with_http_info(**kwargs)

    def get_google_chat_organization(
        self,
        organization_binding_id: str,
    ) -> GoogleChatOrganizationResponse:
        """Get a Google Chat organization binding.

        Get a Google Chat organization binding from the Datadog Google Chat integration.

        :param organization_binding_id: Your organization binding ID.
        :type organization_binding_id: str
        :rtype: GoogleChatOrganizationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["organization_binding_id"] = organization_binding_id

        return self._get_google_chat_organization_endpoint.call_with_http_info(**kwargs)

    def get_google_chat_target_audience(
        self,
        organization_binding_id: str,
        target_audience_id: str,
    ) -> GoogleChatTargetAudienceResponse:
        """Get a target audience.

        Get a target audience for a Google Chat organization binding in the Datadog Google Chat integration.

        :param organization_binding_id: Your organization binding ID.
        :type organization_binding_id: str
        :param target_audience_id: Your target audience ID.
        :type target_audience_id: str
        :rtype: GoogleChatTargetAudienceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["organization_binding_id"] = organization_binding_id

        kwargs["target_audience_id"] = target_audience_id

        return self._get_google_chat_target_audience_endpoint.call_with_http_info(**kwargs)

    def get_organization_handle(
        self,
        organization_binding_id: str,
        handle_id: str,
    ) -> GoogleChatOrganizationHandleResponse:
        """Get organization handle.

        Get an organization handle from the Datadog Google Chat integration.

        :param organization_binding_id: Your organization binding ID.
        :type organization_binding_id: str
        :param handle_id: Your organization handle ID.
        :type handle_id: str
        :rtype: GoogleChatOrganizationHandleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["organization_binding_id"] = organization_binding_id

        kwargs["handle_id"] = handle_id

        return self._get_organization_handle_endpoint.call_with_http_info(**kwargs)

    def get_space_by_display_name(
        self,
        domain_name: str,
        space_display_name: str,
    ) -> GoogleChatAppNamedSpaceResponse:
        """Get space information by display name.

        Get the resource name and organization binding ID of a space in the Datadog Google Chat integration.

        :param domain_name: The Google Chat domain name.
        :type domain_name: str
        :param space_display_name: The Google Chat space display name.
        :type space_display_name: str
        :rtype: GoogleChatAppNamedSpaceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["domain_name"] = domain_name

        kwargs["space_display_name"] = space_display_name

        return self._get_space_by_display_name_endpoint.call_with_http_info(**kwargs)

    def list_google_chat_organizations(
        self,
    ) -> GoogleChatOrganizationsResponse:
        """Get all Google Chat organization bindings.

        Get a list of all Google Chat organization bindings in the Datadog Google Chat integration.

        :rtype: GoogleChatOrganizationsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_google_chat_organizations_endpoint.call_with_http_info(**kwargs)

    def list_google_chat_target_audiences(
        self,
        organization_binding_id: str,
    ) -> GoogleChatTargetAudiencesResponse:
        """Get all target audiences.

        Get a list of all target audiences for a Google Chat organization binding in the Datadog Google Chat integration.

        :param organization_binding_id: Your organization binding ID.
        :type organization_binding_id: str
        :rtype: GoogleChatTargetAudiencesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["organization_binding_id"] = organization_binding_id

        return self._list_google_chat_target_audiences_endpoint.call_with_http_info(**kwargs)

    def list_organization_handles(
        self,
        organization_binding_id: str,
    ) -> GoogleChatOrganizationHandlesResponse:
        """Get all organization handles.

        Get a list of all organization handles from the Datadog Google Chat integration.

        :param organization_binding_id: Your organization binding ID.
        :type organization_binding_id: str
        :rtype: GoogleChatOrganizationHandlesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["organization_binding_id"] = organization_binding_id

        return self._list_organization_handles_endpoint.call_with_http_info(**kwargs)

    def update_google_chat_target_audience(
        self,
        organization_binding_id: str,
        target_audience_id: str,
        body: GoogleChatTargetAudienceUpdateRequest,
    ) -> GoogleChatTargetAudienceResponse:
        """Update a target audience.

        Update a target audience for a Google Chat organization binding in the Datadog Google Chat integration.

        :param organization_binding_id: Your organization binding ID.
        :type organization_binding_id: str
        :param target_audience_id: Your target audience ID.
        :type target_audience_id: str
        :param body: Target audience payload.
        :type body: GoogleChatTargetAudienceUpdateRequest
        :rtype: GoogleChatTargetAudienceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["organization_binding_id"] = organization_binding_id

        kwargs["target_audience_id"] = target_audience_id

        kwargs["body"] = body

        return self._update_google_chat_target_audience_endpoint.call_with_http_info(**kwargs)

    def update_organization_handle(
        self,
        organization_binding_id: str,
        handle_id: str,
        body: GoogleChatUpdateOrganizationHandleRequest,
    ) -> GoogleChatOrganizationHandleResponse:
        """Update organization handle.

        Update an organization handle from the Datadog Google Chat integration.

        :param organization_binding_id: Your organization binding ID.
        :type organization_binding_id: str
        :param handle_id: Your organization handle ID.
        :type handle_id: str
        :param body: Organization handle payload.
        :type body: GoogleChatUpdateOrganizationHandleRequest
        :rtype: GoogleChatOrganizationHandleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["organization_binding_id"] = organization_binding_id

        kwargs["handle_id"] = handle_id

        kwargs["body"] = body

        return self._update_organization_handle_endpoint.call_with_http_info(**kwargs)
