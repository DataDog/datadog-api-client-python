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
    file_type,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.global_orgs_response import GlobalOrgsResponse
from datadog_api_client.v2.model.global_org_data import GlobalOrgData
from datadog_api_client.v2.model.managed_orgs_response import ManagedOrgsResponse
from datadog_api_client.v2.model.org_saml_preferences_update_request import OrgSAMLPreferencesUpdateRequest
from datadog_api_client.v2.model.org_config_list_response import OrgConfigListResponse
from datadog_api_client.v2.model.org_config_get_response import OrgConfigGetResponse
from datadog_api_client.v2.model.org_config_write_request import OrgConfigWriteRequest
from datadog_api_client.v2.model.saml_configurations_response import SAMLConfigurationsResponse
from datadog_api_client.v2.model.saml_configuration_response import SAMLConfigurationResponse
from datadog_api_client.v2.model.saml_configuration_update_request import SAMLConfigurationUpdateRequest


class OrganizationsApi:
    """
    Create, edit, and manage your organizations. Read more about `multi-org accounts <https://docs.datadoghq.com/account_management/multi_organization>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_org_config_endpoint = _Endpoint(
            settings={
                "response_type": (OrgConfigGetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_configs/{org_config_name}",
                "operation_id": "get_org_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "org_config_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "org_config_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_saml_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (SAMLConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/saml_configurations/{saml_config_uuid}",
                "operation_id": "get_saml_configuration",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "saml_config_uuid": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "saml_config_uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_global_orgs_endpoint = _Endpoint(
            settings={
                "response_type": (GlobalOrgsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/global_orgs",
                "operation_id": "list_global_orgs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "user_handle": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_handle",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_org_configs_endpoint = _Endpoint(
            settings={
                "response_type": (OrgConfigListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_configs",
                "operation_id": "list_org_configs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_orgs_endpoint = _Endpoint(
            settings={
                "response_type": (ManagedOrgsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/org",
                "operation_id": "list_orgs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[name]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_saml_configurations_endpoint = _Endpoint(
            settings={
                "response_type": (SAMLConfigurationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/saml_configurations",
                "operation_id": "list_saml_configurations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_org_config_endpoint = _Endpoint(
            settings={
                "response_type": (OrgConfigGetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_configs/{org_config_name}",
                "operation_id": "update_org_config",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "org_config_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "org_config_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (OrgConfigWriteRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_org_saml_configurations_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org/saml_configurations",
                "operation_id": "update_org_saml_configurations",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OrgSAMLPreferencesUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_saml_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (SAMLConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/saml_configurations/{saml_config_uuid}",
                "operation_id": "update_saml_configuration",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "saml_config_uuid": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "saml_config_uuid",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SAMLConfigurationUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._upload_idp_metadata_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/saml_configurations/idp_metadata",
                "operation_id": "upload_idp_metadata",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "idp_file": {
                    "openapi_types": (file_type,),
                    "attribute": "idp_file",
                    "location": "form",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["multipart/form-data"]},
            api_client=api_client,
        )

    def get_org_config(
        self,
        org_config_name: str,
    ) -> OrgConfigGetResponse:
        """Get a specific Org Config value.

        Return the name, description, and value of a specific Org Config.

        :param org_config_name: The name of an Org Config.
        :type org_config_name: str
        :rtype: OrgConfigGetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_config_name"] = org_config_name

        return self._get_org_config_endpoint.call_with_http_info(**kwargs)

    def get_saml_configuration(
        self,
        saml_config_uuid: str,
    ) -> SAMLConfigurationResponse:
        """Get a SAML configuration.

        Get a single SAML configuration for the current organization by its UUID.

        :param saml_config_uuid: The UUID of the SAML configuration.
        :type saml_config_uuid: str
        :rtype: SAMLConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["saml_config_uuid"] = saml_config_uuid

        return self._get_saml_configuration_endpoint.call_with_http_info(**kwargs)

    def list_global_orgs(
        self,
        user_handle: str,
        *,
        page_limit: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
    ) -> GlobalOrgsResponse:
        """List global orgs.

        Returns organizations across regions for the authenticated user. The ``user_handle`` query parameter must match the authenticated user's handle.

        :param user_handle: The handle of the authenticated user.
        :type user_handle: str
        :param page_limit: Maximum number of results returned.
        :type page_limit: int, optional
        :param page_cursor: String to query the next page of results.
            This key is provided with each valid response from the API in ``meta.page.next_cursor``.
        :type page_cursor: str, optional
        :rtype: GlobalOrgsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["user_handle"] = user_handle

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        return self._list_global_orgs_endpoint.call_with_http_info(**kwargs)

    def list_global_orgs_with_pagination(
        self,
        user_handle: str,
        *,
        page_limit: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[GlobalOrgData]:
        """List global orgs.

        Provide a paginated version of :meth:`list_global_orgs`, returning all items.

        :param user_handle: The handle of the authenticated user.
        :type user_handle: str
        :param page_limit: Maximum number of results returned.
        :type page_limit: int, optional
        :param page_cursor: String to query the next page of results.
            This key is provided with each valid response from the API in ``meta.page.next_cursor``.
        :type page_cursor: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[GlobalOrgData]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["user_handle"] = user_handle

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        local_page_size = get_attribute_from_path(kwargs, "page_limit", 100)
        endpoint = self._list_global_orgs_endpoint
        set_attribute_from_path(kwargs, "page_limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "page_cursor",
            "cursor_path": "meta.page.next_cursor",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_org_configs(
        self,
    ) -> OrgConfigListResponse:
        """List Org Configs.

        Returns all Org Configs (name, description, and value).

        :rtype: OrgConfigListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_org_configs_endpoint.call_with_http_info(**kwargs)

    def list_orgs(
        self,
        *,
        filter_name: Union[str, UnsetType] = unset,
    ) -> ManagedOrgsResponse:
        """List your managed organizations.

        Returns the current organization and its managed organizations in JSON:API format.

        :param filter_name: Filter managed organizations by name.
        :type filter_name: str, optional
        :rtype: ManagedOrgsResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_name is not unset:
            kwargs["filter_name"] = filter_name

        return self._list_orgs_endpoint.call_with_http_info(**kwargs)

    def list_saml_configurations(
        self,
    ) -> SAMLConfigurationsResponse:
        """List SAML configurations.

        Get the list of SAML configurations for the current organization. An organization has at most one SAML configuration.

        :rtype: SAMLConfigurationsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_saml_configurations_endpoint.call_with_http_info(**kwargs)

    def update_org_config(
        self,
        org_config_name: str,
        body: OrgConfigWriteRequest,
    ) -> OrgConfigGetResponse:
        """Update a specific Org Config.

        Update the value of a specific Org Config.

        :param org_config_name: The name of an Org Config.
        :type org_config_name: str
        :type body: OrgConfigWriteRequest
        :rtype: OrgConfigGetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_config_name"] = org_config_name

        kwargs["body"] = body

        return self._update_org_config_endpoint.call_with_http_info(**kwargs)

    def update_org_saml_configurations(
        self,
        body: OrgSAMLPreferencesUpdateRequest,
    ) -> None:
        """Update organization SAML preferences.

        Update the SAML preferences for the current organization.

        Use this endpoint to set the just-in-time (JIT) provisioning domains and the default role
        assigned to just-in-time provisioned users.

        :type body: OrgSAMLPreferencesUpdateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._update_org_saml_configurations_endpoint.call_with_http_info(**kwargs)

    def update_saml_configuration(
        self,
        saml_config_uuid: str,
        body: SAMLConfigurationUpdateRequest,
    ) -> SAMLConfigurationResponse:
        """Update a SAML configuration.

        Update a single SAML configuration for the current organization.

        Use this endpoint to enable or disable identity-provider-initiated login, set the
        just-in-time provisioning domains, and set the default role assigned to
        just-in-time provisioned users. A default role is required to enable just-in-time provisioning.

        :param saml_config_uuid: The UUID of the SAML configuration.
        :type saml_config_uuid: str
        :type body: SAMLConfigurationUpdateRequest
        :rtype: SAMLConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["saml_config_uuid"] = saml_config_uuid

        kwargs["body"] = body

        return self._update_saml_configuration_endpoint.call_with_http_info(**kwargs)

    def upload_idp_metadata(
        self,
        *,
        idp_file: Union[file_type, UnsetType] = unset,
    ) -> None:
        """Upload IdP metadata.

        Endpoint for uploading IdP metadata for SAML setup.

        Use this endpoint to upload or replace IdP metadata for SAML login configuration.

        :param idp_file: The IdP metadata XML file
        :type idp_file: file_type, optional
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        if idp_file is not unset:
            kwargs["idp_file"] = idp_file

        return self._upload_idp_metadata_endpoint.call_with_http_info(**kwargs)
