# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model.user_response import UserResponse
from datadog_api_client.v2.model.service_account_create_request import ServiceAccountCreateRequest
from datadog_api_client.v2.model.user_invitations_response import UserInvitationsResponse
from datadog_api_client.v2.model.user_invitations_request import UserInvitationsRequest
from datadog_api_client.v2.model.user_invitation_response import UserInvitationResponse
from datadog_api_client.v2.model.users_response import UsersResponse
from datadog_api_client.v2.model.query_sort_order import QuerySortOrder
from datadog_api_client.v2.model.user_create_request import UserCreateRequest
from datadog_api_client.v2.model.user_update_request import UserUpdateRequest
from datadog_api_client.v2.model.permissions_response import PermissionsResponse


class UsersApi:
    """
    Create, edit, and disable users.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_service_account_endpoint = _Endpoint(
            settings={
                "response_type": (UserResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/service_accounts",
                "operation_id": "create_service_account",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ServiceAccountCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_user_endpoint = _Endpoint(
            settings={
                "response_type": (UserResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/users",
                "operation_id": "create_user",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (UserCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._disable_user_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/users/{user_id}",
                "operation_id": "disable_user",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "user_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_invitation_endpoint = _Endpoint(
            settings={
                "response_type": (UserInvitationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/user_invitations/{user_invitation_uuid}",
                "operation_id": "get_invitation",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "user_invitation_uuid": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_invitation_uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_user_endpoint = _Endpoint(
            settings={
                "response_type": (UserResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/users/{user_id}",
                "operation_id": "get_user",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "user_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_user_organizations_endpoint = _Endpoint(
            settings={
                "response_type": (UserResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/users/{user_id}/orgs",
                "operation_id": "list_user_organizations",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "user_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_user_permissions_endpoint = _Endpoint(
            settings={
                "response_type": (PermissionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/users/{user_id}/permissions",
                "operation_id": "list_user_permissions",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "user_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_users_endpoint = _Endpoint(
            settings={
                "response_type": (UsersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/users",
                "operation_id": "list_users",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
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
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "sort_dir": {
                    "openapi_types": (QuerySortOrder,),
                    "attribute": "sort_dir",
                    "location": "query",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
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
                "content_type": [],
            },
            api_client=api_client,
        )

        self._send_invitations_endpoint = _Endpoint(
            settings={
                "response_type": (UserInvitationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/user_invitations",
                "operation_id": "send_invitations",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (UserInvitationsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_user_endpoint = _Endpoint(
            settings={
                "response_type": (UserResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/users/{user_id}",
                "operation_id": "update_user",
                "http_method": "PATCH",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "user_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UserUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_service_account(self, body, **kwargs):
        """Create a service account.

        Create a service account for your organization.

        :type body: ServiceAccountCreateRequest
        :rtype: UserResponse
        """
        kwargs["body"] = body

        return self._create_service_account_endpoint.call_with_http_info(**kwargs)

    def create_user(self, body, **kwargs):
        """Create a user.

        Create a user for your organization.

        :type body: UserCreateRequest
        :rtype: UserResponse
        """
        kwargs["body"] = body

        return self._create_user_endpoint.call_with_http_info(**kwargs)

    def disable_user(self, user_id, **kwargs):
        """Disable a user.

        Disable a user. Can only be used with an application key belonging
        to an administrator user.

        :param user_id: The ID of the user.
        :type user_id: str
        :rtype: None
        """
        kwargs["user_id"] = user_id

        return self._disable_user_endpoint.call_with_http_info(**kwargs)

    def get_invitation(self, user_invitation_uuid, **kwargs):
        """Get a user invitation.

        Returns a single user invitation by its UUID.

        :param user_invitation_uuid: The UUID of the user invitation.
        :type user_invitation_uuid: str
        :rtype: UserInvitationResponse
        """
        kwargs["user_invitation_uuid"] = user_invitation_uuid

        return self._get_invitation_endpoint.call_with_http_info(**kwargs)

    def get_user(self, user_id, **kwargs):
        """Get user details.

        Get a user in the organization specified by the user’s ``user_id``.

        :param user_id: The ID of the user.
        :type user_id: str
        :rtype: UserResponse
        """
        kwargs["user_id"] = user_id

        return self._get_user_endpoint.call_with_http_info(**kwargs)

    def list_user_organizations(self, user_id, **kwargs):
        """Get a user organization.

        Get a user organization. Returns the user information and all organizations
        joined by this user.

        :param user_id: The ID of the user.
        :type user_id: str
        :rtype: UserResponse
        """
        kwargs["user_id"] = user_id

        return self._list_user_organizations_endpoint.call_with_http_info(**kwargs)

    def list_user_permissions(self, user_id, **kwargs):
        """Get a user permissions.

        Get a user permission set. Returns a list of the user’s permissions
        granted by the associated user's roles.

        :param user_id: The ID of the user.
        :type user_id: str
        :rtype: PermissionsResponse
        """
        kwargs["user_id"] = user_id

        return self._list_user_permissions_endpoint.call_with_http_info(**kwargs)

    def list_users(self, **kwargs):
        """List all users.

        Get the list of all users in the organization. This list includes
        all users even if they are deactivated or unverified.

        :param page_size: Size for a given page.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: User attribute to order results by. Sort order is ascending by default.
            Sort order is descending if the field
            is prefixed by a negative sign, for example ``sort=-name``. Options: ``name`` ,
            ``modified_at`` , ``user_count``.
        :type sort: str, optional
        :param sort_dir: Direction of sort. Options: ``asc`` , ``desc``.
        :type sort_dir: QuerySortOrder, optional
        :param filter: Filter all users by the given string. Defaults to no filtering.
        :type filter: str, optional
        :param filter_status: Filter on status attribute.
            Comma separated list, with possible values ``Active`` , ``Pending`` , and ``Disabled``.
            Defaults to no filtering.
        :type filter_status: str, optional
        :rtype: UsersResponse
        """
        return self._list_users_endpoint.call_with_http_info(**kwargs)

    def send_invitations(self, body, **kwargs):
        """Send invitation emails.

        Sends emails to one or more users inviting them to join the organization.

        :type body: UserInvitationsRequest
        :rtype: UserInvitationsResponse
        """
        kwargs["body"] = body

        return self._send_invitations_endpoint.call_with_http_info(**kwargs)

    def update_user(self, user_id, body, **kwargs):
        """Update a user.

        Edit a user. Can only be used with an application key belonging
        to an administrator user.

        :param user_id: The ID of the user.
        :type user_id: str
        :type body: UserUpdateRequest
        :rtype: UserResponse
        """
        kwargs["user_id"] = user_id

        kwargs["body"] = body

        return self._update_user_endpoint.call_with_http_info(**kwargs)
