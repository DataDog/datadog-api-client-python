# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.intake_payload_accepted import IntakePayloadAccepted
from datadog_api_client.v1.model.service_checks import ServiceChecks


class ServiceChecksApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._submit_service_check_endpoint = _Endpoint(
            settings={
                "response_type": (IntakePayloadAccepted,),
                "auth": ["apiKeyAuth"],
                "endpoint_path": "/api/v1/check_run",
                "operation_id": "submit_service_check",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ServiceChecks,),
                    "location": "body",
                    "collection_format": "multi",
                },
            },
            headers_map={"accept": ["text/json", "application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def submit_service_check(self, body, **kwargs):
        """Submit a Service Check.

        Submit a list of Service Checks.

        **Notes**:
        - A valid API key is required.
        - Service checks can be submitted up to 10 minutes in the past.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.submit_service_check(body, async_req=True)
        >>> result = thread.get()

        :param body: Service Check request body.
        :type body: ServiceChecks
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
        :rtype: IntakePayloadAccepted
        """
        kwargs = self._submit_service_check_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._submit_service_check_endpoint.call_with_http_info(**kwargs)
