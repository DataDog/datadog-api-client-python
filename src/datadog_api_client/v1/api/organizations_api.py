# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401
import sys  # noqa: F401

from datadog_api_client.v1.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from datadog_api_client.v1.model.api_error_response import APIErrorResponse
from datadog_api_client.v1.model.idp_response import IdpResponse
from datadog_api_client.v1.model.organization import Organization
from datadog_api_client.v1.model.organization_create_body import OrganizationCreateBody
from datadog_api_client.v1.model.organization_create_response import OrganizationCreateResponse
from datadog_api_client.v1.model.organization_list_response import OrganizationListResponse
from datadog_api_client.v1.model.organization_response import OrganizationResponse


class OrganizationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_child_org_endpoint = _Endpoint(
            settings={
                "response_type": (OrganizationCreateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/org",
                "operation_id": "create_child_org",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (OrganizationCreateBody,),
                },
                "attribute_map": {},
                "location_map": {
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_org_endpoint = _Endpoint(
            settings={
                "response_type": (OrganizationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/org/{public_id}",
                "operation_id": "get_org",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "public_id",
                ],
                "required": [
                    "public_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "public_id": (str,),
                },
                "attribute_map": {
                    "public_id": "public_id",
                },
                "location_map": {
                    "public_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_orgs_endpoint = _Endpoint(
            settings={
                "response_type": (OrganizationListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/org",
                "operation_id": "list_orgs",
                "http_method": "GET",
                "servers": None,
            },
            params_map={"all": [], "required": [], "nullable": [], "enum": [], "validation": []},
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_org_endpoint = _Endpoint(
            settings={
                "response_type": (OrganizationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/org/{public_id}",
                "operation_id": "update_org",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "public_id",
                    "body",
                ],
                "required": [
                    "public_id",
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "public_id": (str,),
                    "body": (Organization,),
                },
                "attribute_map": {
                    "public_id": "public_id",
                },
                "location_map": {
                    "public_id": "path",
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._upload_id_p_for_org_endpoint = _Endpoint(
            settings={
                "response_type": (IdpResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/org/{public_id}/idp_metadata",
                "operation_id": "upload_id_p_for_org",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "public_id",
                    "idp_file",
                ],
                "required": [
                    "public_id",
                    "idp_file",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "public_id": (str,),
                    "idp_file": (file_type,),
                },
                "attribute_map": {
                    "public_id": "public_id",
                    "idp_file": "idp_file",
                },
                "location_map": {
                    "public_id": "path",
                    "idp_file": "form",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["multipart/form-data"]},
            api_client=api_client,
        )

    def create_child_org(self, body, **kwargs):
        """Create a child organization  # noqa: E501

        Create a child organization.  This endpoint requires the [multi-organization account](https://docs.datadoghq.com/account_management/multi_organization/) feature and must be enabled by [contacting support](https://docs.datadoghq.com/help/).  Once a new child organization is created, you can interact with it by using the `org.public_id`, `pi_key.key`, and `application_key.hash` provided in the response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_child_org(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (OrganizationCreateBody): Organization object that needs to be created

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            OrganizationCreateResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._create_child_org_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._create_child_org_endpoint.call_with_http_info(**kwargs)

    def get_org(self, public_id, **kwargs):
        """Get organization information  # noqa: E501

        Get organization information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_org(public_id, async_req=True)
        >>> result = thread.get()

        Args:
            public_id (str): The `public_id` of the organization you are operating within.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            OrganizationResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._get_org_endpoint.default_arguments(kwargs)
        kwargs["public_id"] = public_id
        return self._get_org_endpoint.call_with_http_info(**kwargs)

    def list_orgs(self, **kwargs):
        """List your managed organizations  # noqa: E501

        List your managed organizations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_orgs(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            OrganizationListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_orgs_endpoint.default_arguments(kwargs)
        return self._list_orgs_endpoint.call_with_http_info(**kwargs)

    def update_org(self, public_id, body, **kwargs):
        """Update your organization  # noqa: E501

        Update your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_org(public_id, body, async_req=True)
        >>> result = thread.get()

        Args:
            public_id (str): The `public_id` of the organization you are operating within.
            body (Organization):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            OrganizationResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._update_org_endpoint.default_arguments(kwargs)
        kwargs["public_id"] = public_id
        kwargs["body"] = body
        return self._update_org_endpoint.call_with_http_info(**kwargs)

    def upload_id_p_for_org(self, public_id, idp_file, **kwargs):
        """Upload IdP metadata  # noqa: E501

        There are a couple of options for updating the Identity Provider (IdP) metadata from your SAML IdP.  * **Multipart Form-Data**: Post the IdP metadata file using a form post.  * **XML Body:** Post the IdP metadata file as the body of the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_id_p_for_org(public_id, idp_file, async_req=True)
        >>> result = thread.get()

        Args:
            public_id (str): The `public_id` of the organization you are operating with
            idp_file (file_type): The path to the XML metadata file you wish to upload.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            IdpResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._upload_id_p_for_org_endpoint.default_arguments(kwargs)
        kwargs["public_id"] = public_id
        kwargs["idp_file"] = idp_file
        return self._upload_id_p_for_org_endpoint.call_with_http_info(**kwargs)
