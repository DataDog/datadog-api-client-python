# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    file_type,
    UnsetType,
    unset,
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
from datadog_api_client.v2.model.cloud_workload_security_agent_policies_list_response import (
    CloudWorkloadSecurityAgentPoliciesListResponse,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_response import (
    CloudWorkloadSecurityAgentPolicyResponse,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_create_request import (
    CloudWorkloadSecurityAgentPolicyCreateRequest,
)
from datadog_api_client.v2.model.cloud_workload_security_agent_policy_update_request import (
    CloudWorkloadSecurityAgentPolicyUpdateRequest,
)


class CSMThreatsApi:
    """
    Workload Protection monitors file, network, and process activity across your environment to detect real-time threats to your infrastructure. See `Workload Protection <https://docs.datadoghq.com/security/workload_protection/>`_ for more information on setting up Workload Protection.

    **Note** : These endpoints are split based on whether you are using the US1-FED site or not. Please reference the specific resource for the site you are using.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_cloud_workload_security_agent_rule_endpoint = _Endpoint(
            settings={
                "response_type": (CloudWorkloadSecurityAgentRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/cloud_workload_security/agent_rules",
                "operation_id": "create_cloud_workload_security_agent_rule",
                "http_method": "POST",
                "version": "v2",
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

        self._create_csm_threats_agent_policy_endpoint = _Endpoint(
            settings={
                "response_type": (CloudWorkloadSecurityAgentPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/cws/policy",
                "operation_id": "create_csm_threats_agent_policy",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CloudWorkloadSecurityAgentPolicyCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_csm_threats_agent_rule_endpoint = _Endpoint(
            settings={
                "response_type": (CloudWorkloadSecurityAgentRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/cws/agent_rules",
                "operation_id": "create_csm_threats_agent_rule",
                "http_method": "POST",
                "version": "v2",
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
            },
            api_client=api_client,
        )

        self._delete_csm_threats_agent_policy_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/cws/policy/{policy_id}",
                "operation_id": "delete_csm_threats_agent_policy",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "policy_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "policy_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_csm_threats_agent_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id}",
                "operation_id": "delete_csm_threats_agent_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "agent_rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "agent_rule_id",
                    "location": "path",
                },
                "policy_id": {
                    "openapi_types": (str,),
                    "attribute": "policy_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._download_cloud_workload_policy_file_endpoint = _Endpoint(
            settings={
                "response_type": (file_type,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/cloud_workload/policy/download",
                "operation_id": "download_cloud_workload_policy_file",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/yaml", "application/json"],
            },
            api_client=api_client,
        )

        self._download_csm_threats_policy_endpoint = _Endpoint(
            settings={
                "response_type": (file_type,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/cws/policy/download",
                "operation_id": "download_csm_threats_policy",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/zip", "application/json"],
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
            },
            api_client=api_client,
        )

        self._get_csm_threats_agent_policy_endpoint = _Endpoint(
            settings={
                "response_type": (CloudWorkloadSecurityAgentPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/cws/policy/{policy_id}",
                "operation_id": "get_csm_threats_agent_policy",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "policy_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "policy_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_csm_threats_agent_rule_endpoint = _Endpoint(
            settings={
                "response_type": (CloudWorkloadSecurityAgentRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id}",
                "operation_id": "get_csm_threats_agent_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "agent_rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "agent_rule_id",
                    "location": "path",
                },
                "policy_id": {
                    "openapi_types": (str,),
                    "attribute": "policy_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
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
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_csm_threats_agent_policies_endpoint = _Endpoint(
            settings={
                "response_type": (CloudWorkloadSecurityAgentPoliciesListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/cws/policy",
                "operation_id": "list_csm_threats_agent_policies",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_csm_threats_agent_rules_endpoint = _Endpoint(
            settings={
                "response_type": (CloudWorkloadSecurityAgentRulesListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/cws/agent_rules",
                "operation_id": "list_csm_threats_agent_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "policy_id": {
                    "openapi_types": (str,),
                    "attribute": "policy_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
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

        self._update_csm_threats_agent_policy_endpoint = _Endpoint(
            settings={
                "response_type": (CloudWorkloadSecurityAgentPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/cws/policy/{policy_id}",
                "operation_id": "update_csm_threats_agent_policy",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "policy_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "policy_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CloudWorkloadSecurityAgentPolicyUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_csm_threats_agent_rule_endpoint = _Endpoint(
            settings={
                "response_type": (CloudWorkloadSecurityAgentRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/cws/agent_rules/{agent_rule_id}",
                "operation_id": "update_csm_threats_agent_rule",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "agent_rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "agent_rule_id",
                    "location": "path",
                },
                "policy_id": {
                    "openapi_types": (str,),
                    "attribute": "policy_id",
                    "location": "query",
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

    def create_cloud_workload_security_agent_rule(
        self,
        body: CloudWorkloadSecurityAgentRuleCreateRequest,
    ) -> CloudWorkloadSecurityAgentRuleResponse:
        """Create a Workload Protection agent rule (US1-FED).

        Create a new agent rule with the given parameters.

        **Note** : This endpoint should only be used for the Government (US1-FED) site.

        :param body: The definition of the new agent rule
        :type body: CloudWorkloadSecurityAgentRuleCreateRequest
        :rtype: CloudWorkloadSecurityAgentRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_cloud_workload_security_agent_rule_endpoint.call_with_http_info(**kwargs)

    def create_csm_threats_agent_policy(
        self,
        body: CloudWorkloadSecurityAgentPolicyCreateRequest,
    ) -> CloudWorkloadSecurityAgentPolicyResponse:
        """Create a Workload Protection policy.

        Create a new Workload Protection policy with the given parameters.

        **Note** : This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.

        :param body: The definition of the new Agent policy
        :type body: CloudWorkloadSecurityAgentPolicyCreateRequest
        :rtype: CloudWorkloadSecurityAgentPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_csm_threats_agent_policy_endpoint.call_with_http_info(**kwargs)

    def create_csm_threats_agent_rule(
        self,
        body: CloudWorkloadSecurityAgentRuleCreateRequest,
    ) -> CloudWorkloadSecurityAgentRuleResponse:
        """Create a Workload Protection agent rule.

        Create a new Workload Protection agent rule with the given parameters.

        **Note** : This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.

        :param body: The definition of the new agent rule
        :type body: CloudWorkloadSecurityAgentRuleCreateRequest
        :rtype: CloudWorkloadSecurityAgentRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_csm_threats_agent_rule_endpoint.call_with_http_info(**kwargs)

    def delete_cloud_workload_security_agent_rule(
        self,
        agent_rule_id: str,
    ) -> None:
        """Delete a Workload Protection agent rule (US1-FED).

        Delete a specific agent rule.

        **Note** : This endpoint should only be used for the Government (US1-FED) site.

        :param agent_rule_id: The ID of the Agent rule
        :type agent_rule_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["agent_rule_id"] = agent_rule_id

        return self._delete_cloud_workload_security_agent_rule_endpoint.call_with_http_info(**kwargs)

    def delete_csm_threats_agent_policy(
        self,
        policy_id: str,
    ) -> None:
        """Delete a Workload Protection policy.

        Delete a specific Workload Protection policy.

        **Note** : This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.

        :param policy_id: The ID of the Agent policy
        :type policy_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        return self._delete_csm_threats_agent_policy_endpoint.call_with_http_info(**kwargs)

    def delete_csm_threats_agent_rule(
        self,
        agent_rule_id: str,
        *,
        policy_id: Union[str, UnsetType] = unset,
    ) -> None:
        """Delete a Workload Protection agent rule.

        Delete a specific Workload Protection agent rule.

        **Note** : This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.

        :param agent_rule_id: The ID of the Agent rule
        :type agent_rule_id: str
        :param policy_id: The ID of the Agent policy
        :type policy_id: str, optional
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["agent_rule_id"] = agent_rule_id

        if policy_id is not unset:
            kwargs["policy_id"] = policy_id

        return self._delete_csm_threats_agent_rule_endpoint.call_with_http_info(**kwargs)

    def download_cloud_workload_policy_file(
        self,
    ) -> file_type:
        """Download the Workload Protection policy (US1-FED).

        The download endpoint generates a Workload Protection policy file from your currently active
        Workload Protection agent rules, and downloads them as a ``.policy`` file. This file can then be deployed to
        your agents to update the policy running in your environment.

        **Note** : This endpoint should only be used for the Government (US1-FED) site.

        :rtype: file_type
        """
        kwargs: Dict[str, Any] = {}
        return self._download_cloud_workload_policy_file_endpoint.call_with_http_info(**kwargs)

    def download_csm_threats_policy(
        self,
    ) -> file_type:
        """Download the Workload Protection policy.

        The download endpoint generates a Workload Protection policy file from your currently active
        Workload Protection agent rules, and downloads them as a ``.policy`` file. This file can then be deployed to
        your agents to update the policy running in your environment.

        **Note** : This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.

        :rtype: file_type
        """
        kwargs: Dict[str, Any] = {}
        return self._download_csm_threats_policy_endpoint.call_with_http_info(**kwargs)

    def get_cloud_workload_security_agent_rule(
        self,
        agent_rule_id: str,
    ) -> CloudWorkloadSecurityAgentRuleResponse:
        """Get a Workload Protection agent rule (US1-FED).

        Get the details of a specific agent rule.

        **Note** : This endpoint should only be used for the Government (US1-FED) site.

        :param agent_rule_id: The ID of the Agent rule
        :type agent_rule_id: str
        :rtype: CloudWorkloadSecurityAgentRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["agent_rule_id"] = agent_rule_id

        return self._get_cloud_workload_security_agent_rule_endpoint.call_with_http_info(**kwargs)

    def get_csm_threats_agent_policy(
        self,
        policy_id: str,
    ) -> CloudWorkloadSecurityAgentPolicyResponse:
        """Get a Workload Protection policy.

        Get the details of a specific Workload Protection policy.

        **Note** : This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.

        :param policy_id: The ID of the Agent policy
        :type policy_id: str
        :rtype: CloudWorkloadSecurityAgentPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        return self._get_csm_threats_agent_policy_endpoint.call_with_http_info(**kwargs)

    def get_csm_threats_agent_rule(
        self,
        agent_rule_id: str,
        *,
        policy_id: Union[str, UnsetType] = unset,
    ) -> CloudWorkloadSecurityAgentRuleResponse:
        """Get a Workload Protection agent rule.

        Get the details of a specific Workload Protection agent rule.

        **Note** : This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.

        :param agent_rule_id: The ID of the Agent rule
        :type agent_rule_id: str
        :param policy_id: The ID of the Agent policy
        :type policy_id: str, optional
        :rtype: CloudWorkloadSecurityAgentRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["agent_rule_id"] = agent_rule_id

        if policy_id is not unset:
            kwargs["policy_id"] = policy_id

        return self._get_csm_threats_agent_rule_endpoint.call_with_http_info(**kwargs)

    def list_cloud_workload_security_agent_rules(
        self,
    ) -> CloudWorkloadSecurityAgentRulesListResponse:
        """Get all Workload Protection agent rules (US1-FED).

        Get the list of agent rules.

        **Note** : This endpoint should only be used for the Government (US1-FED) site.

        :rtype: CloudWorkloadSecurityAgentRulesListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_cloud_workload_security_agent_rules_endpoint.call_with_http_info(**kwargs)

    def list_csm_threats_agent_policies(
        self,
    ) -> CloudWorkloadSecurityAgentPoliciesListResponse:
        """Get all Workload Protection policies.

        Get the list of Workload Protection policies.

        **Note** : This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.

        :rtype: CloudWorkloadSecurityAgentPoliciesListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_csm_threats_agent_policies_endpoint.call_with_http_info(**kwargs)

    def list_csm_threats_agent_rules(
        self,
        *,
        policy_id: Union[str, UnsetType] = unset,
    ) -> CloudWorkloadSecurityAgentRulesListResponse:
        """Get all Workload Protection agent rules.

        Get the list of Workload Protection agent rules.

        **Note** : This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.

        :param policy_id: The ID of the Agent policy
        :type policy_id: str, optional
        :rtype: CloudWorkloadSecurityAgentRulesListResponse
        """
        kwargs: Dict[str, Any] = {}
        if policy_id is not unset:
            kwargs["policy_id"] = policy_id

        return self._list_csm_threats_agent_rules_endpoint.call_with_http_info(**kwargs)

    def update_cloud_workload_security_agent_rule(
        self,
        agent_rule_id: str,
        body: CloudWorkloadSecurityAgentRuleUpdateRequest,
    ) -> CloudWorkloadSecurityAgentRuleResponse:
        """Update a Workload Protection agent rule (US1-FED).

        Update a specific agent rule.
        Returns the agent rule object when the request is successful.

        **Note** : This endpoint should only be used for the Government (US1-FED) site.

        :param agent_rule_id: The ID of the Agent rule
        :type agent_rule_id: str
        :param body: New definition of the agent rule
        :type body: CloudWorkloadSecurityAgentRuleUpdateRequest
        :rtype: CloudWorkloadSecurityAgentRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["agent_rule_id"] = agent_rule_id

        kwargs["body"] = body

        return self._update_cloud_workload_security_agent_rule_endpoint.call_with_http_info(**kwargs)

    def update_csm_threats_agent_policy(
        self,
        policy_id: str,
        body: CloudWorkloadSecurityAgentPolicyUpdateRequest,
    ) -> CloudWorkloadSecurityAgentPolicyResponse:
        """Update a Workload Protection policy.

        Update a specific Workload Protection policy.
        Returns the policy object when the request is successful.

        **Note** : This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.

        :param policy_id: The ID of the Agent policy
        :type policy_id: str
        :param body: New definition of the Agent policy
        :type body: CloudWorkloadSecurityAgentPolicyUpdateRequest
        :rtype: CloudWorkloadSecurityAgentPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        kwargs["body"] = body

        return self._update_csm_threats_agent_policy_endpoint.call_with_http_info(**kwargs)

    def update_csm_threats_agent_rule(
        self,
        agent_rule_id: str,
        body: CloudWorkloadSecurityAgentRuleUpdateRequest,
        *,
        policy_id: Union[str, UnsetType] = unset,
    ) -> CloudWorkloadSecurityAgentRuleResponse:
        """Update a Workload Protection agent rule.

        Update a specific Workload Protection Agent rule.
        Returns the agent rule object when the request is successful.

        **Note** : This endpoint is not available for the Government (US1-FED) site. Please reference the (US1-FED) specific resource below.

        :param agent_rule_id: The ID of the Agent rule
        :type agent_rule_id: str
        :param body: New definition of the agent rule
        :type body: CloudWorkloadSecurityAgentRuleUpdateRequest
        :param policy_id: The ID of the Agent policy
        :type policy_id: str, optional
        :rtype: CloudWorkloadSecurityAgentRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["agent_rule_id"] = agent_rule_id

        if policy_id is not unset:
            kwargs["policy_id"] = policy_id

        kwargs["body"] = body

        return self._update_csm_threats_agent_rule_endpoint.call_with_http_info(**kwargs)
