# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.slack_integration_channels import SlackIntegrationChannels
from datadog_api_client.v1.model.slack_integration_channel import SlackIntegrationChannel


class SlackIntegrationApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_slack_integration_channel_endpoint = _Endpoint(
            settings={
                "response_type": (SlackIntegrationChannel,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/slack/configuration/accounts/{account_name}/channels",
                "operation_id": "create_slack_integration_channel",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "account_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SlackIntegrationChannel,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_slack_integration_channel_endpoint = _Endpoint(
            settings={
                "response_type": (SlackIntegrationChannel,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}",
                "operation_id": "get_slack_integration_channel",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "account_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_name",
                    "location": "path",
                },
                "channel_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "channel_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_slack_integration_channels_endpoint = _Endpoint(
            settings={
                "response_type": (SlackIntegrationChannels,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/slack/configuration/accounts/{account_name}/channels",
                "operation_id": "get_slack_integration_channels",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "account_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._remove_slack_integration_channel_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}",
                "operation_id": "remove_slack_integration_channel",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "account_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_name",
                    "location": "path",
                },
                "channel_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "channel_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_slack_integration_channel_endpoint = _Endpoint(
            settings={
                "response_type": (SlackIntegrationChannel,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name}",
                "operation_id": "update_slack_integration_channel",
                "http_method": "PATCH",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "account_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_name",
                    "location": "path",
                },
                "channel_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "channel_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SlackIntegrationChannel,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_slack_integration_channel(self, account_name, body, **kwargs):
        """Create a Slack integration channel.

        Add a channel to your Datadog-Slack integration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_slack_integration_channel(account_name, body, async_req=True)
        >>> result = thread.get()

        :param account_name: Your Slack account name.
        :type account_name: str
        :param body: Payload describing Slack channel to be created
        :type body: SlackIntegrationChannel
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
        :rtype: SlackIntegrationChannel
        """
        kwargs = self._create_slack_integration_channel_endpoint.default_arguments(kwargs)
        kwargs["account_name"] = account_name

        kwargs["body"] = body

        return self._create_slack_integration_channel_endpoint.call_with_http_info(**kwargs)

    def get_slack_integration_channel(self, account_name, channel_name, **kwargs):
        """Get a Slack integration channel.

        Get a channel configured for your Datadog-Slack integration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_slack_integration_channel(account_name, channel_name, async_req=True)
        >>> result = thread.get()

        :param account_name: Your Slack account name.
        :type account_name: str
        :param channel_name: The name of the Slack channel being operated on.
        :type channel_name: str
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
        :rtype: SlackIntegrationChannel
        """
        kwargs = self._get_slack_integration_channel_endpoint.default_arguments(kwargs)
        kwargs["account_name"] = account_name

        kwargs["channel_name"] = channel_name

        return self._get_slack_integration_channel_endpoint.call_with_http_info(**kwargs)

    def get_slack_integration_channels(self, account_name, **kwargs):
        """Get all channels in a Slack integration.

        Get a list of all channels configured for your Datadog-Slack integration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_slack_integration_channels(account_name, async_req=True)
        >>> result = thread.get()

        :param account_name: Your Slack account name.
        :type account_name: str
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
        :rtype: SlackIntegrationChannels
        """
        kwargs = self._get_slack_integration_channels_endpoint.default_arguments(kwargs)
        kwargs["account_name"] = account_name

        return self._get_slack_integration_channels_endpoint.call_with_http_info(**kwargs)

    def remove_slack_integration_channel(self, account_name, channel_name, **kwargs):
        """Remove a Slack integration channel.

        Remove a channel from your Datadog-Slack integration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.remove_slack_integration_channel(account_name, channel_name, async_req=True)
        >>> result = thread.get()

        :param account_name: Your Slack account name.
        :type account_name: str
        :param channel_name: The name of the Slack channel being operated on.
        :type channel_name: str
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
        kwargs = self._remove_slack_integration_channel_endpoint.default_arguments(kwargs)
        kwargs["account_name"] = account_name

        kwargs["channel_name"] = channel_name

        return self._remove_slack_integration_channel_endpoint.call_with_http_info(**kwargs)

    def update_slack_integration_channel(self, account_name, channel_name, body, **kwargs):
        """Update a Slack integration channel.

        Update a channel used in your Datadog-Slack integration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_slack_integration_channel(account_name, channel_name, body, async_req=True)
        >>> result = thread.get()

        :param account_name: Your Slack account name.
        :type account_name: str
        :param channel_name: The name of the Slack channel being operated on.
        :type channel_name: str
        :param body: Payload describing fields and values to be updated.
        :type body: SlackIntegrationChannel
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
        :rtype: SlackIntegrationChannel
        """
        kwargs = self._update_slack_integration_channel_endpoint.default_arguments(kwargs)
        kwargs["account_name"] = account_name

        kwargs["channel_name"] = channel_name

        kwargs["body"] = body

        return self._update_slack_integration_channel_endpoint.call_with_http_info(**kwargs)
