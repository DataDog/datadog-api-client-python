# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.deployment_gate_response import DeploymentGateResponse
from datadog_api_client.v2.model.create_deployment_gate_params import CreateDeploymentGateParams
from datadog_api_client.v2.model.deployment_gate_rules_response import DeploymentGateRulesResponse
from datadog_api_client.v2.model.deployment_rule_response import DeploymentRuleResponse
from datadog_api_client.v2.model.create_deployment_rule_params import CreateDeploymentRuleParams
from datadog_api_client.v2.model.update_deployment_rule_params import UpdateDeploymentRuleParams
from datadog_api_client.v2.model.update_deployment_gate_params import UpdateDeploymentGateParams


class DeploymentGatesApi:
    """
    Manage Deployment Gates using this API to reduce the likelihood and impact of incidents caused by deployments. See the `Deployment Gates documentation <https://docs.datadoghq.com/deployment_gates/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_deployment_gate_endpoint = _Endpoint(
            settings={
                "response_type": (DeploymentGateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/deployment_gates",
                "operation_id": "create_deployment_gate",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateDeploymentGateParams,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_deployment_rule_endpoint = _Endpoint(
            settings={
                "response_type": (DeploymentRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/deployment_gates/{gate_id}/rules",
                "operation_id": "create_deployment_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "gate_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "gate_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CreateDeploymentRuleParams,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_deployment_gate_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/deployment_gates/{id}",
                "operation_id": "delete_deployment_gate",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_deployment_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/deployment_gates/{gate_id}/rules/{id}",
                "operation_id": "delete_deployment_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "gate_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "gate_id",
                    "location": "path",
                },
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_deployment_gate_endpoint = _Endpoint(
            settings={
                "response_type": (DeploymentGateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/deployment_gates/{id}",
                "operation_id": "get_deployment_gate",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_deployment_gate_rules_endpoint = _Endpoint(
            settings={
                "response_type": (DeploymentGateRulesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/deployment_gates/{gate_id}/rules",
                "operation_id": "get_deployment_gate_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "gate_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "gate_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_deployment_rule_endpoint = _Endpoint(
            settings={
                "response_type": (DeploymentRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/deployment_gates/{gate_id}/rules/{id}",
                "operation_id": "get_deployment_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "gate_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "gate_id",
                    "location": "path",
                },
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_deployment_gate_endpoint = _Endpoint(
            settings={
                "response_type": (DeploymentGateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/deployment_gates/{id}",
                "operation_id": "update_deployment_gate",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateDeploymentGateParams,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_deployment_rule_endpoint = _Endpoint(
            settings={
                "response_type": (DeploymentRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/deployment_gates/{gate_id}/rules/{id}",
                "operation_id": "update_deployment_rule",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "gate_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "gate_id",
                    "location": "path",
                },
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateDeploymentRuleParams,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_deployment_gate(
        self,
        body: CreateDeploymentGateParams,
    ) -> DeploymentGateResponse:
        """Create deployment gate.

        Endpoint to create a deployment gate.

        :type body: CreateDeploymentGateParams
        :rtype: DeploymentGateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_deployment_gate_endpoint.call_with_http_info(**kwargs)

    def create_deployment_rule(
        self,
        gate_id: str,
        body: CreateDeploymentRuleParams,
    ) -> DeploymentRuleResponse:
        """Create deployment rule.

        Endpoint to create a deployment rule. A gate for the rule must already exist.

        :param gate_id: The ID of the deployment gate.
        :type gate_id: str
        :type body: CreateDeploymentRuleParams
        :rtype: DeploymentRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["gate_id"] = gate_id

        kwargs["body"] = body

        return self._create_deployment_rule_endpoint.call_with_http_info(**kwargs)

    def delete_deployment_gate(
        self,
        id: str,
    ) -> None:
        """Delete deployment gate.

        Endpoint to delete a deployment gate. Rules associated with the gate are also deleted.

        :param id: The ID of the deployment gate.
        :type id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_deployment_gate_endpoint.call_with_http_info(**kwargs)

    def delete_deployment_rule(
        self,
        gate_id: str,
        id: str,
    ) -> None:
        """Delete deployment rule.

        Endpoint to delete a deployment rule.

        :param gate_id: The ID of the deployment gate.
        :type gate_id: str
        :param id: The ID of the deployment rule.
        :type id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["gate_id"] = gate_id

        kwargs["id"] = id

        return self._delete_deployment_rule_endpoint.call_with_http_info(**kwargs)

    def get_deployment_gate(
        self,
        id: str,
    ) -> DeploymentGateResponse:
        """Get deployment gate.

        Endpoint to get a deployment gate.

        :param id: The ID of the deployment gate.
        :type id: str
        :rtype: DeploymentGateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_deployment_gate_endpoint.call_with_http_info(**kwargs)

    def get_deployment_gate_rules(
        self,
        gate_id: str,
    ) -> DeploymentGateRulesResponse:
        """Get rules for a deployment gate.

        Endpoint to get rules for a deployment gate.

        :param gate_id: The ID of the deployment gate.
        :type gate_id: str
        :rtype: DeploymentGateRulesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["gate_id"] = gate_id

        return self._get_deployment_gate_rules_endpoint.call_with_http_info(**kwargs)

    def get_deployment_rule(
        self,
        gate_id: str,
        id: str,
    ) -> DeploymentRuleResponse:
        """Get deployment rule.

        Endpoint to get a deployment rule.

        :param gate_id: The ID of the deployment gate.
        :type gate_id: str
        :param id: The ID of the deployment rule.
        :type id: str
        :rtype: DeploymentRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["gate_id"] = gate_id

        kwargs["id"] = id

        return self._get_deployment_rule_endpoint.call_with_http_info(**kwargs)

    def update_deployment_gate(
        self,
        id: str,
        body: UpdateDeploymentGateParams,
    ) -> DeploymentGateResponse:
        """Update deployment gate.

        Endpoint to update a deployment gate.

        :param id: The ID of the deployment gate.
        :type id: str
        :type body: UpdateDeploymentGateParams
        :rtype: DeploymentGateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_deployment_gate_endpoint.call_with_http_info(**kwargs)

    def update_deployment_rule(
        self,
        gate_id: str,
        id: str,
        body: UpdateDeploymentRuleParams,
    ) -> DeploymentRuleResponse:
        """Update deployment rule.

        Endpoint to update a deployment rule.

        :param gate_id: The ID of the deployment gate.
        :type gate_id: str
        :param id: The ID of the deployment rule.
        :type id: str
        :type body: UpdateDeploymentRuleParams
        :rtype: DeploymentRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["gate_id"] = gate_id

        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_deployment_rule_endpoint.call_with_http_info(**kwargs)
