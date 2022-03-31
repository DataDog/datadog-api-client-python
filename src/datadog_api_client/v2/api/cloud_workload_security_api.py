# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.model_utils import (
    file_type,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rules_list_response import (
    CloudWorkloadSecurityAgentRulesListResponse,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_response import (
    CloudWorkloadSecurityAgentRuleResponse,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_request import (
    CloudWorkloadSecurityAgentRuleCreateRequest,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_request import (
    CloudWorkloadSecurityAgentRuleUpdateRequest,
)


class CloudWorkloadSecurityApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_cloud_workload_security_agent_rule_endpoint = _Endpoint(
            settings={
                "response_type": (CloudWorkloadSecurityAgentRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/cloud_workload_security/agent_rules",
                "operation_id": "create_cloud_workload_security_agent_rule",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CloudWorkloadSecurityAgentRuleCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_cloud_workload_security_agent_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id}",
                "operation_id": "delete_cloud_workload_security_agent_rule",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "agent_rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "agent_rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._download_cloud_workload_policy_file_endpoint = _Endpoint(
            settings={
                "response_type": (file_type,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/cloud_workload/policy/download",
                "operation_id": "download_cloud_workload_policy_file",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/yaml", "application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_cloud_workload_security_agent_rule_endpoint = _Endpoint(
            settings={
                "response_type": (CloudWorkloadSecurityAgentRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id}",
                "operation_id": "get_cloud_workload_security_agent_rule",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "agent_rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "agent_rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_cloud_workload_security_agent_rules_endpoint = _Endpoint(
            settings={
                "response_type": (CloudWorkloadSecurityAgentRulesListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/cloud_workload_security/agent_rules",
                "operation_id": "list_cloud_workload_security_agent_rules",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_cloud_workload_security_agent_rule_endpoint = _Endpoint(
            settings={
                "response_type": (CloudWorkloadSecurityAgentRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id}",
                "operation_id": "update_cloud_workload_security_agent_rule",
                "http_method": "PATCH",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "agent_rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "agent_rule_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CloudWorkloadSecurityAgentRuleUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_cloud_workload_security_agent_rule(self, body, **kwargs):
        """Create a Cloud Workload Security Agent rule.

        Create a new Agent rule with the given parameters.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_cloud_workload_security_agent_rule(body, async_req=True)
        >>> result = thread.get()

        :param body: The definition of the new Agent rule.
        :type body: CloudWorkloadSecurityAgentRuleCreateRequest
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
        :rtype: CloudWorkloadSecurityAgentRuleResponse
        """
        kwargs = self._create_cloud_workload_security_agent_rule_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_cloud_workload_security_agent_rule_endpoint.call_with_http_info(**kwargs)

    def delete_cloud_workload_security_agent_rule(self, agent_rule_id, **kwargs):
        """Delete a Cloud Workload Security Agent rule.

        Delete a specific Agent rule.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_cloud_workload_security_agent_rule(agent_rule_id, async_req=True)
        >>> result = thread.get()

        :param agent_rule_id: The ID of the Agent rule.
        :type agent_rule_id: str
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
        kwargs = self._delete_cloud_workload_security_agent_rule_endpoint.default_arguments(kwargs)
        kwargs["agent_rule_id"] = agent_rule_id

        return self._delete_cloud_workload_security_agent_rule_endpoint.call_with_http_info(**kwargs)

    def download_cloud_workload_policy_file(self, **kwargs):
        """Get the latest Cloud Workload Security policy.

        The download endpoint generates a Cloud Workload Security policy file from your currently active
        Cloud Workload Security rules, and downloads them as a .policy file. This file can then be deployed to
        your agents to update the policy running in your environment.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.download_cloud_workload_policy_file(async_req=True)
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
        :rtype: file_type
        """
        kwargs = self._download_cloud_workload_policy_file_endpoint.default_arguments(kwargs)
        return self._download_cloud_workload_policy_file_endpoint.call_with_http_info(**kwargs)

    def get_cloud_workload_security_agent_rule(self, agent_rule_id, **kwargs):
        """Get a Cloud Workload Security Agent rule.

        Get the details of a specific Agent rule.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_cloud_workload_security_agent_rule(agent_rule_id, async_req=True)
        >>> result = thread.get()

        :param agent_rule_id: The ID of the Agent rule.
        :type agent_rule_id: str
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
        :rtype: CloudWorkloadSecurityAgentRuleResponse
        """
        kwargs = self._get_cloud_workload_security_agent_rule_endpoint.default_arguments(kwargs)
        kwargs["agent_rule_id"] = agent_rule_id

        return self._get_cloud_workload_security_agent_rule_endpoint.call_with_http_info(**kwargs)

    def list_cloud_workload_security_agent_rules(self, **kwargs):
        """Get all Cloud Workload Security Agent rules.

        Get the list of Agent rules.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_cloud_workload_security_agent_rules(async_req=True)
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
        :rtype: CloudWorkloadSecurityAgentRulesListResponse
        """
        kwargs = self._list_cloud_workload_security_agent_rules_endpoint.default_arguments(kwargs)
        return self._list_cloud_workload_security_agent_rules_endpoint.call_with_http_info(**kwargs)

    def update_cloud_workload_security_agent_rule(self, agent_rule_id, body, **kwargs):
        """Update a Cloud Workload Security Agent rule.

        Update a specific Agent rule.
        Returns the Agent rule object when the request is successful.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_cloud_workload_security_agent_rule(agent_rule_id, body, async_req=True)
        >>> result = thread.get()

        :param agent_rule_id: The ID of the Agent rule.
        :type agent_rule_id: str
        :param body: New definition of the Agent rule.
        :type body: CloudWorkloadSecurityAgentRuleUpdateRequest
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
        :rtype: CloudWorkloadSecurityAgentRuleResponse
        """
        kwargs = self._update_cloud_workload_security_agent_rule_endpoint.default_arguments(kwargs)
        kwargs["agent_rule_id"] = agent_rule_id

        kwargs["body"] = body

        return self._update_cloud_workload_security_agent_rule_endpoint.call_with_http_info(**kwargs)
