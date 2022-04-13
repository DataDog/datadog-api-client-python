# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.model_utils import (
    file_type,
)


class OrganizationsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._upload_idp_metadata_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/saml_configurations/idp_metadata",
                "operation_id": "upload_idp_metadata",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
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

    def upload_idp_metadata(self, **kwargs):
        """Upload IdP metadata.

        Endpoint for uploading IdP metadata for SAML setup.

        Use this endpoint to upload or replace IdP metadata for SAML login configuration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.upload_idp_metadata(async_req=True)
        >>> result = thread.get()

        :param idp_file: The IdP metadata XML file
        :type idp_file: file_type, optional
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
        :rtype: None
        """
        kwargs = self._upload_idp_metadata_endpoint.default_arguments(kwargs)
        return self._upload_idp_metadata_endpoint.call_with_http_info(**kwargs)
