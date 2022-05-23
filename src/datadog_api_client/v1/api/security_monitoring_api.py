# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.successful_signal_update_response import SuccessfulSignalUpdateResponse
from datadog_api_client.v1.model.add_signal_to_incident_request import AddSignalToIncidentRequest
from datadog_api_client.v1.model.signal_assignee_update_request import SignalAssigneeUpdateRequest
from datadog_api_client.v1.model.signal_state_update_request import SignalStateUpdateRequest


class SecurityMonitoringApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._add_security_monitoring_signal_to_incident_endpoint = _Endpoint(
            settings={
                "response_type": (SuccessfulSignalUpdateResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/security_analytics/signals/{signal_id}/add_to_incident",
                "operation_id": "add_security_monitoring_signal_to_incident",
                "http_method": "PATCH",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "signal_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "signal_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AddSignalToIncidentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._edit_security_monitoring_signal_assignee_endpoint = _Endpoint(
            settings={
                "response_type": (SuccessfulSignalUpdateResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/security_analytics/signals/{signal_id}/assignee",
                "operation_id": "edit_security_monitoring_signal_assignee",
                "http_method": "PATCH",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "signal_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "signal_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SignalAssigneeUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._edit_security_monitoring_signal_state_endpoint = _Endpoint(
            settings={
                "response_type": (SuccessfulSignalUpdateResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/security_analytics/signals/{signal_id}/state",
                "operation_id": "edit_security_monitoring_signal_state",
                "http_method": "PATCH",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "signal_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "signal_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SignalStateUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def add_security_monitoring_signal_to_incident(self, signal_id, body, **kwargs):
        """Add a security signal to an incident.

        Add a security signal to an incident. This makes it possible to search for signals by incident within the signal explorer and to view the signals on the incident timeline.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.add_security_monitoring_signal_to_incident(signal_id, body, async_req=True)
        >>> result = thread.get()

        :param signal_id: The ID of the signal.
        :type signal_id: str
        :param body: Attributes describing the signal update.
        :type body: AddSignalToIncidentRequest
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
        :rtype: SuccessfulSignalUpdateResponse
        """
        kwargs = self._add_security_monitoring_signal_to_incident_endpoint.default_arguments(kwargs)
        kwargs["signal_id"] = signal_id

        kwargs["body"] = body

        return self._add_security_monitoring_signal_to_incident_endpoint.call_with_http_info(**kwargs)

    def edit_security_monitoring_signal_assignee(self, signal_id, body, **kwargs):
        """Modify the triage assignee of a security signal.

        Modify the triage assignee of a security signal.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.edit_security_monitoring_signal_assignee(signal_id, body, async_req=True)
        >>> result = thread.get()

        :param signal_id: The ID of the signal.
        :type signal_id: str
        :param body: Attributes describing the signal update.
        :type body: SignalAssigneeUpdateRequest
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
        :rtype: SuccessfulSignalUpdateResponse
        """
        kwargs = self._edit_security_monitoring_signal_assignee_endpoint.default_arguments(kwargs)
        kwargs["signal_id"] = signal_id

        kwargs["body"] = body

        return self._edit_security_monitoring_signal_assignee_endpoint.call_with_http_info(**kwargs)

    def edit_security_monitoring_signal_state(self, signal_id, body, **kwargs):
        """Change the triage state of a security signal.

        Change the triage state of a security signal.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.edit_security_monitoring_signal_state(signal_id, body, async_req=True)
        >>> result = thread.get()

        :param signal_id: The ID of the signal.
        :type signal_id: str
        :param body: Attributes describing the signal update.
        :type body: SignalStateUpdateRequest
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
        :rtype: SuccessfulSignalUpdateResponse
        """
        kwargs = self._edit_security_monitoring_signal_state_endpoint.default_arguments(kwargs)
        kwargs["signal_id"] = signal_id

        kwargs["body"] = body

        return self._edit_security_monitoring_signal_state_endpoint.call_with_http_info(**kwargs)
