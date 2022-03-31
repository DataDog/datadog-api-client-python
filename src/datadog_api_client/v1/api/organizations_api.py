# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.model_utils import (
    file_type,
)
from datadog_api_client.v1.model.organization_list_response import OrganizationListResponse
from datadog_api_client.v1.model.organization_create_response import OrganizationCreateResponse
from datadog_api_client.v1.model.organization_create_body import OrganizationCreateBody
from datadog_api_client.v1.model.organization_response import OrganizationResponse
from datadog_api_client.v1.model.organization import Organization
from datadog_api_client.v1.model.idp_response import IdpResponse


class OrganizationsApi:
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
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OrganizationCreateBody,),
                    "location": "body",
                },
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
                "version": "v1",
                "servers": None,
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
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
                "version": "v1",
                "servers": None,
            },
            params_map={},
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
                "version": "v1",
                "servers": None,
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (Organization,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._upload_idp_for_org_endpoint = _Endpoint(
            settings={
                "response_type": (IdpResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/org/{public_id}/idp_metadata",
                "operation_id": "upload_idp_for_org",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "idp_file": {
                    "required": True,
                    "openapi_types": (file_type,),
                    "attribute": "idp_file",
                    "location": "form",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["multipart/form-data"]},
            api_client=api_client,
        )

    def create_child_org(self, body, **kwargs):
        """Create a child organization.

        Create a child organization.

        This endpoint requires the
        [multi-organization account](https://docs.datadoghq.com/account_management/multi_organization/)
        feature and must be enabled by
        [contacting support](https://docs.datadoghq.com/help/).

        Once a new child organization is created, you can interact with it
        by using the `org.public_id`, `api_key.key`, and
        `application_key.hash` provided in the response.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_child_org(body, async_req=True)
        >>> result = thread.get()

        :param body: Organization object that needs to be created
        :type body: OrganizationCreateBody
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: OrganizationCreateResponse
        """
        kwargs = self._create_child_org_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_child_org_endpoint.call_with_http_info(**kwargs)

    def get_org(self, public_id, **kwargs):
        """Get organization information.

        Get organization information.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_org(public_id, async_req=True)
        >>> result = thread.get()

        :param public_id: The `public_id` of the organization you are operating within.
        :type public_id: str
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: OrganizationResponse
        """
        kwargs = self._get_org_endpoint.default_arguments(kwargs)
        kwargs["public_id"] = public_id

        return self._get_org_endpoint.call_with_http_info(**kwargs)

    def list_orgs(self, **kwargs):
        """List your managed organizations.

        List your managed organizations.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_orgs(async_req=True)
        >>> result = thread.get()

        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: OrganizationListResponse
        """
        kwargs = self._list_orgs_endpoint.default_arguments(kwargs)
        return self._list_orgs_endpoint.call_with_http_info(**kwargs)

    def update_org(self, public_id, body, **kwargs):
        """Update your organization.

        Update your organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_org(public_id, body, async_req=True)
        >>> result = thread.get()

        :param public_id: The `public_id` of the organization you are operating within.
        :type public_id: str
        :type body: Organization
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: OrganizationResponse
        """
        kwargs = self._update_org_endpoint.default_arguments(kwargs)
        kwargs["public_id"] = public_id

        kwargs["body"] = body

        return self._update_org_endpoint.call_with_http_info(**kwargs)

    def upload_idp_for_org(self, public_id, idp_file, **kwargs):
        """Upload IdP metadata.

        There are a couple of options for updating the Identity Provider (IdP)
        metadata from your SAML IdP.

        * **Multipart Form-Data**: Post the IdP metadata file using a form post.

        * **XML Body:** Post the IdP metadata file as the body of the request.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.upload_idp_for_org(public_id, idp_file, async_req=True)
        >>> result = thread.get()

        :param public_id: The `public_id` of the organization you are operating with
        :type public_id: str
        :param idp_file: The path to the XML metadata file you wish to upload.
        :type idp_file: file_type
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: IdpResponse
        """
        kwargs = self._upload_idp_for_org_endpoint.default_arguments(kwargs)
        kwargs["public_id"] = public_id

        kwargs["idp_file"] = idp_file

        return self._upload_idp_for_org_endpoint.call_with_http_info(**kwargs)
