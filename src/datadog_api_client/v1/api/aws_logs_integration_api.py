# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.aws_account_and_lambda_request import AWSAccountAndLambdaRequest
from datadog_api_client.v1.model.aws_logs_list_response import AWSLogsListResponse
from datadog_api_client.v1.model.aws_logs_async_response import AWSLogsAsyncResponse
from datadog_api_client.v1.model.aws_logs_list_services_response import AWSLogsListServicesResponse
from datadog_api_client.v1.model.aws_logs_services_request import AWSLogsServicesRequest


class AWSLogsIntegrationApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._check_aws_logs_lambda_async_endpoint = _Endpoint(
            settings={
                "response_type": (AWSLogsAsyncResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/integration/aws/logs/check_async",
                "operation_id": "check_aws_logs_lambda_async",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AWSAccountAndLambdaRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._check_aws_logs_services_async_endpoint = _Endpoint(
            settings={
                "response_type": (AWSLogsAsyncResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws/logs/services_async",
                "operation_id": "check_aws_logs_services_async",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AWSLogsServicesRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_aws_lambda_arn_endpoint = _Endpoint(
            settings={
                "response_type": (dict,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws/logs",
                "operation_id": "create_aws_lambda_arn",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AWSAccountAndLambdaRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_aws_lambda_arn_endpoint = _Endpoint(
            settings={
                "response_type": (dict,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws/logs",
                "operation_id": "delete_aws_lambda_arn",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AWSAccountAndLambdaRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._enable_aws_log_services_endpoint = _Endpoint(
            settings={
                "response_type": (dict,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws/logs/services",
                "operation_id": "enable_aws_log_services",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AWSLogsServicesRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_aws_logs_integrations_endpoint = _Endpoint(
            settings={
                "response_type": ([AWSLogsListResponse],),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws/logs",
                "operation_id": "list_aws_logs_integrations",
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

        self._list_aws_logs_services_endpoint = _Endpoint(
            settings={
                "response_type": ([AWSLogsListServicesResponse],),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/aws/logs/services",
                "operation_id": "list_aws_logs_services",
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

    def check_aws_logs_lambda_async(self, body, **kwargs):
        """Check that an AWS Lambda Function exists.

        Test if permissions are present to add a log-forwarding triggers for the given services and AWS account. The input
        is the same as for Enable an AWS service log collection. Subsequent requests will always repeat the above, so this
        endpoint can be polled intermittently instead of blocking.

        - Returns a status of 'created' when it's checking if the Lambda exists in the account.
        - Returns a status of 'waiting' while checking.
        - Returns a status of 'checked and ok' if the Lambda exists.
        - Returns a status of 'error' if the Lambda does not exist.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.check_aws_logs_lambda_async(body, async_req=True)
        >>> result = thread.get()

        :param body: Check AWS Log Lambda Async request body.
        :type body: AWSAccountAndLambdaRequest
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
        :rtype: AWSLogsAsyncResponse
        """
        kwargs = self._check_aws_logs_lambda_async_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._check_aws_logs_lambda_async_endpoint.call_with_http_info(**kwargs)

    def check_aws_logs_services_async(self, body, **kwargs):
        """Check permissions for log services.

        Test if permissions are present to add log-forwarding triggers for the
        given services and AWS account. Input is the same as for `EnableAWSLogServices`.
        Done async, so can be repeatedly polled in a non-blocking fashion until
        the async request completes.

        - Returns a status of `created` when it's checking if the permissions exists
          in the AWS account.
        - Returns a status of `waiting` while checking.
        - Returns a status of `checked and ok` if the Lambda exists.
        - Returns a status of `error` if the Lambda does not exist.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.check_aws_logs_services_async(body, async_req=True)
        >>> result = thread.get()

        :param body: Check AWS Logs Async Services request body.
        :type body: AWSLogsServicesRequest
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
        :rtype: AWSLogsAsyncResponse
        """
        kwargs = self._check_aws_logs_services_async_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._check_aws_logs_services_async_endpoint.call_with_http_info(**kwargs)

    def create_aws_lambda_arn(self, body, **kwargs):
        """Add AWS Log Lambda ARN.

        Attach the Lambda ARN of the Lambda created for the Datadog-AWS log collection to your AWS account ID to enable log collection.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_aws_lambda_arn(body, async_req=True)
        >>> result = thread.get()

        :param body: AWS Log Lambda Async request body.
        :type body: AWSAccountAndLambdaRequest
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
        :rtype: dict
        """
        kwargs = self._create_aws_lambda_arn_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_aws_lambda_arn_endpoint.call_with_http_info(**kwargs)

    def delete_aws_lambda_arn(self, body, **kwargs):
        """Delete an AWS Logs integration.

        Delete a Datadog-AWS logs configuration by removing the specific Lambda ARN associated with a given AWS account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_aws_lambda_arn(body, async_req=True)
        >>> result = thread.get()

        :param body: Delete AWS Lambda ARN request body.
        :type body: AWSAccountAndLambdaRequest
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
        :rtype: dict
        """
        kwargs = self._delete_aws_lambda_arn_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._delete_aws_lambda_arn_endpoint.call_with_http_info(**kwargs)

    def enable_aws_log_services(self, body, **kwargs):
        """Enable an AWS Logs integration.

        Enable automatic log collection for a list of services. This should be run after running `CreateAWSLambdaARN` to save the configuration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.enable_aws_log_services(body, async_req=True)
        >>> result = thread.get()

        :param body: Enable AWS Log Services request body.
        :type body: AWSLogsServicesRequest
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
        :rtype: dict
        """
        kwargs = self._enable_aws_log_services_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._enable_aws_log_services_endpoint.call_with_http_info(**kwargs)

    def list_aws_logs_integrations(self, **kwargs):
        """List all AWS Logs integrations.

        List all Datadog-AWS Logs integrations configured in your Datadog account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_aws_logs_integrations(async_req=True)
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
        :rtype: [AWSLogsListResponse]
        """
        kwargs = self._list_aws_logs_integrations_endpoint.default_arguments(kwargs)
        return self._list_aws_logs_integrations_endpoint.call_with_http_info(**kwargs)

    def list_aws_logs_services(self, **kwargs):
        """Get list of AWS log ready services.

        Get the list of current AWS services that Datadog offers automatic log collection. Use returned service IDs with the services parameter for the Enable an AWS service log collection API endpoint.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_aws_logs_services(async_req=True)
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
        :rtype: [AWSLogsListServicesResponse]
        """
        kwargs = self._list_aws_logs_services_endpoint.default_arguments(kwargs)
        return self._list_aws_logs_services_endpoint.call_with_http_info(**kwargs)
