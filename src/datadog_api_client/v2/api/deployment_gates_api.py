# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    datetime,
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
    UUID,
)
from datadog_api_client.v2.model.deployment_gates_list_response import DeploymentGatesListResponse
from datadog_api_client.v2.model.deployment_gate_response import DeploymentGateResponse
from datadog_api_client.v2.model.create_deployment_gate_params import CreateDeploymentGateParams
from datadog_api_client.v2.model.deployment_gate_evaluations_response import DeploymentGateEvaluationsResponse
from datadog_api_client.v2.model.deployment_gates_evaluation_result_response_attributes_gate_status import (
    DeploymentGatesEvaluationResultResponseAttributesGateStatus,
)
from datadog_api_client.v2.model.deployment_gate_evaluation_data import DeploymentGateEvaluationData
from datadog_api_client.v2.model.deployment_gate_rule_evaluations_response import DeploymentGateRuleEvaluationsResponse
from datadog_api_client.v2.model.deployment_gate_rule_evaluation_type import DeploymentGateRuleEvaluationType
from datadog_api_client.v2.model.deployment_gate_rule_evaluation_data import DeploymentGateRuleEvaluationData
from datadog_api_client.v2.model.deployment_gate_rules_response import DeploymentGateRulesResponse
from datadog_api_client.v2.model.deployment_rule_response import DeploymentRuleResponse
from datadog_api_client.v2.model.create_deployment_rule_params import CreateDeploymentRuleParams
from datadog_api_client.v2.model.update_deployment_rule_params import UpdateDeploymentRuleParams
from datadog_api_client.v2.model.update_deployment_gate_params import UpdateDeploymentGateParams
from datadog_api_client.v2.model.deployment_gates_evaluation_response import DeploymentGatesEvaluationResponse
from datadog_api_client.v2.model.deployment_gates_evaluation_request import DeploymentGatesEvaluationRequest
from datadog_api_client.v2.model.deployment_gates_evaluation_result_response import (
    DeploymentGatesEvaluationResultResponse,
)


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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

        self._get_deployment_gates_evaluation_result_endpoint = _Endpoint(
            settings={
                "response_type": (DeploymentGatesEvaluationResultResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/deployments/gates/evaluation/{id}",
                "operation_id": "get_deployment_gates_evaluation_result",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

        self._list_deployment_gate_evaluations_endpoint = _Endpoint(
            settings={
                "response_type": (DeploymentGateEvaluationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/deployment_gates/evaluations",
                "operation_id": "list_deployment_gate_evaluations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_from": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[from]",
                    "location": "query",
                },
                "filter_to": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[to]",
                    "location": "query",
                },
                "filter_service": {
                    "openapi_types": ([str],),
                    "attribute": "filter[service]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_env": {
                    "openapi_types": ([str],),
                    "attribute": "filter[env]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_identifier": {
                    "openapi_types": ([str],),
                    "attribute": "filter[identifier]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_status": {
                    "openapi_types": ([DeploymentGatesEvaluationResultResponseAttributesGateStatus],),
                    "attribute": "filter[status]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_dry_run": {
                    "openapi_types": (bool,),
                    "attribute": "filter[dry_run]",
                    "location": "query",
                },
                "filter_evaluation_id": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[evaluation_id]",
                    "location": "query",
                },
                "filter_gate_id": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[gate_id]",
                    "location": "query",
                },
                "filter_version": {
                    "openapi_types": ([str],),
                    "attribute": "filter[version]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_deployment_gates_endpoint = _Endpoint(
            settings={
                "response_type": (DeploymentGatesListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/deployment_gates",
                "operation_id": "list_deployment_gates",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_service": {
                    "openapi_types": (str,),
                    "attribute": "filter[service]",
                    "location": "query",
                },
                "filter_env": {
                    "openapi_types": (str,),
                    "attribute": "filter[env]",
                    "location": "query",
                },
                "filter_identifier": {
                    "openapi_types": (str,),
                    "attribute": "filter[identifier]",
                    "location": "query",
                },
                "filter_dry_run": {
                    "openapi_types": (bool,),
                    "attribute": "filter[dry_run]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_deployment_rule_evaluations_endpoint = _Endpoint(
            settings={
                "response_type": (DeploymentGateRuleEvaluationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/deployment_gates/evaluations/rules",
                "operation_id": "list_deployment_rule_evaluations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_from": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[from]",
                    "location": "query",
                },
                "filter_to": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[to]",
                    "location": "query",
                },
                "filter_gate_evaluation_id": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[gate_evaluation_id]",
                    "location": "query",
                },
                "filter_evaluation_id": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[evaluation_id]",
                    "location": "query",
                },
                "filter_gate_id": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[gate_id]",
                    "location": "query",
                },
                "filter_rule_id": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[rule_id]",
                    "location": "query",
                },
                "filter_service": {
                    "openapi_types": ([str],),
                    "attribute": "filter[service]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_env": {
                    "openapi_types": ([str],),
                    "attribute": "filter[env]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_identifier": {
                    "openapi_types": ([str],),
                    "attribute": "filter[identifier]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_version": {
                    "openapi_types": ([str],),
                    "attribute": "filter[version]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_status": {
                    "openapi_types": ([DeploymentGatesEvaluationResultResponseAttributesGateStatus],),
                    "attribute": "filter[status]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_type": {
                    "openapi_types": ([DeploymentGateRuleEvaluationType],),
                    "attribute": "filter[type]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_dry_run": {
                    "openapi_types": (bool,),
                    "attribute": "filter[dry_run]",
                    "location": "query",
                },
                "filter_gate_dry_run": {
                    "openapi_types": (bool,),
                    "attribute": "filter[gate_dry_run]",
                    "location": "query",
                },
                "filter_name": {
                    "openapi_types": ([str],),
                    "attribute": "filter[name]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._trigger_deployment_gates_evaluation_endpoint = _Endpoint(
            settings={
                "response_type": (DeploymentGatesEvaluationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/deployments/gates/evaluation",
                "operation_id": "trigger_deployment_gates_evaluation",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DeploymentGatesEvaluationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_deployment_gate_endpoint = _Endpoint(
            settings={
                "response_type": (DeploymentGateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

    def get_deployment_gates_evaluation_result(
        self,
        id: UUID,
    ) -> DeploymentGatesEvaluationResultResponse:
        """Get a deployment gate evaluation result.

        Retrieves the result of a deployment gate evaluation by its evaluation ID.
        If the evaluation is still in progress, ``data.attributes.gate_status`` will be ``in_progress`` ;
        continue polling until it returns ``pass`` or ``fail``.
        Polling every 10-20 seconds is recommended.
        The endpoint may return a 404 if called too soon after triggering; retry after a few seconds.

        :param id: The evaluation ID returned by the trigger endpoint.
        :type id: UUID
        :rtype: DeploymentGatesEvaluationResultResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_deployment_gates_evaluation_result_endpoint.call_with_http_info(**kwargs)

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

    def list_deployment_gate_evaluations(
        self,
        *,
        filter_from: Union[datetime, UnsetType] = unset,
        filter_to: Union[datetime, UnsetType] = unset,
        filter_service: Union[List[str], UnsetType] = unset,
        filter_env: Union[List[str], UnsetType] = unset,
        filter_identifier: Union[List[str], UnsetType] = unset,
        filter_status: Union[List[DeploymentGatesEvaluationResultResponseAttributesGateStatus], UnsetType] = unset,
        filter_dry_run: Union[bool, UnsetType] = unset,
        filter_evaluation_id: Union[UUID, UnsetType] = unset,
        filter_gate_id: Union[UUID, UnsetType] = unset,
        filter_version: Union[List[str], UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
    ) -> DeploymentGateEvaluationsResponse:
        """List deployment gate evaluations.

        Returns deployment gate evaluations started in a maximum 30-day window (the default is the previous 24 hours).
        Results are ordered by start time, newest first.
        In-progress state is near-real-time and mutable. Finished state is eventually consistent.

        :param filter_from: Inclusive evaluation start time. Defaults to 24 hours before the request. Together with ``filter[to]`` , the window may span no more than 30 days.
        :type filter_from: datetime, optional
        :param filter_to: Exclusive evaluation start time. Defaults to the request time. Must be after ``filter[from]`` ; the window may span no more than 30 days.
        :type filter_to: datetime, optional
        :param filter_service: Service values. Repeated or comma-separated values are combined with OR.
        :type filter_service: [str], optional
        :param filter_env: Environment values. Repeated or comma-separated values are combined with OR.
        :type filter_env: [str], optional
        :param filter_identifier: Gate identifier values. Repeated or comma-separated values are combined with OR.
        :type filter_identifier: [str], optional
        :param filter_status: Gate outcomes. Repeated or comma-separated values are combined with OR.
        :type filter_status: [DeploymentGatesEvaluationResultResponseAttributesGateStatus], optional
        :param filter_dry_run: Gate-level dry-run state.
        :type filter_dry_run: bool, optional
        :param filter_evaluation_id: Gate evaluation UUID. No match returns an empty list.
        :type filter_evaluation_id: UUID, optional
        :param filter_gate_id: Configured gate UUID. Just-in-time evaluations have no gate ID.
        :type filter_gate_id: UUID, optional
        :param filter_version: Deployment version values. Repeated or comma-separated values are combined with OR.
        :type filter_version: [str], optional
        :param page_size: Maximum evaluations returned.
        :type page_size: int, optional
        :param page_cursor: Opaque cursor returned in ``meta.page.next_cursor`` by the previous page. Invalid cursors return 400.
        :type page_cursor: str, optional
        :rtype: DeploymentGateEvaluationsResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_from is not unset:
            kwargs["filter_from"] = filter_from

        if filter_to is not unset:
            kwargs["filter_to"] = filter_to

        if filter_service is not unset:
            kwargs["filter_service"] = filter_service

        if filter_env is not unset:
            kwargs["filter_env"] = filter_env

        if filter_identifier is not unset:
            kwargs["filter_identifier"] = filter_identifier

        if filter_status is not unset:
            kwargs["filter_status"] = filter_status

        if filter_dry_run is not unset:
            kwargs["filter_dry_run"] = filter_dry_run

        if filter_evaluation_id is not unset:
            kwargs["filter_evaluation_id"] = filter_evaluation_id

        if filter_gate_id is not unset:
            kwargs["filter_gate_id"] = filter_gate_id

        if filter_version is not unset:
            kwargs["filter_version"] = filter_version

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        return self._list_deployment_gate_evaluations_endpoint.call_with_http_info(**kwargs)

    def list_deployment_gate_evaluations_with_pagination(
        self,
        *,
        filter_from: Union[datetime, UnsetType] = unset,
        filter_to: Union[datetime, UnsetType] = unset,
        filter_service: Union[List[str], UnsetType] = unset,
        filter_env: Union[List[str], UnsetType] = unset,
        filter_identifier: Union[List[str], UnsetType] = unset,
        filter_status: Union[List[DeploymentGatesEvaluationResultResponseAttributesGateStatus], UnsetType] = unset,
        filter_dry_run: Union[bool, UnsetType] = unset,
        filter_evaluation_id: Union[UUID, UnsetType] = unset,
        filter_gate_id: Union[UUID, UnsetType] = unset,
        filter_version: Union[List[str], UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[DeploymentGateEvaluationData]:
        """List deployment gate evaluations.

        Provide a paginated version of :meth:`list_deployment_gate_evaluations`, returning all items.

        :param filter_from: Inclusive evaluation start time. Defaults to 24 hours before the request. Together with ``filter[to]`` , the window may span no more than 30 days.
        :type filter_from: datetime, optional
        :param filter_to: Exclusive evaluation start time. Defaults to the request time. Must be after ``filter[from]`` ; the window may span no more than 30 days.
        :type filter_to: datetime, optional
        :param filter_service: Service values. Repeated or comma-separated values are combined with OR.
        :type filter_service: [str], optional
        :param filter_env: Environment values. Repeated or comma-separated values are combined with OR.
        :type filter_env: [str], optional
        :param filter_identifier: Gate identifier values. Repeated or comma-separated values are combined with OR.
        :type filter_identifier: [str], optional
        :param filter_status: Gate outcomes. Repeated or comma-separated values are combined with OR.
        :type filter_status: [DeploymentGatesEvaluationResultResponseAttributesGateStatus], optional
        :param filter_dry_run: Gate-level dry-run state.
        :type filter_dry_run: bool, optional
        :param filter_evaluation_id: Gate evaluation UUID. No match returns an empty list.
        :type filter_evaluation_id: UUID, optional
        :param filter_gate_id: Configured gate UUID. Just-in-time evaluations have no gate ID.
        :type filter_gate_id: UUID, optional
        :param filter_version: Deployment version values. Repeated or comma-separated values are combined with OR.
        :type filter_version: [str], optional
        :param page_size: Maximum evaluations returned.
        :type page_size: int, optional
        :param page_cursor: Opaque cursor returned in ``meta.page.next_cursor`` by the previous page. Invalid cursors return 400.
        :type page_cursor: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[DeploymentGateEvaluationData]
        """
        kwargs: Dict[str, Any] = {}
        if filter_from is not unset:
            kwargs["filter_from"] = filter_from

        if filter_to is not unset:
            kwargs["filter_to"] = filter_to

        if filter_service is not unset:
            kwargs["filter_service"] = filter_service

        if filter_env is not unset:
            kwargs["filter_env"] = filter_env

        if filter_identifier is not unset:
            kwargs["filter_identifier"] = filter_identifier

        if filter_status is not unset:
            kwargs["filter_status"] = filter_status

        if filter_dry_run is not unset:
            kwargs["filter_dry_run"] = filter_dry_run

        if filter_evaluation_id is not unset:
            kwargs["filter_evaluation_id"] = filter_evaluation_id

        if filter_gate_id is not unset:
            kwargs["filter_gate_id"] = filter_gate_id

        if filter_version is not unset:
            kwargs["filter_version"] = filter_version

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        local_page_size = get_attribute_from_path(kwargs, "page_size", 20)
        endpoint = self._list_deployment_gate_evaluations_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "page_cursor",
            "cursor_path": "meta.page.next_cursor",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_deployment_gates(
        self,
        *,
        filter_service: Union[str, UnsetType] = unset,
        filter_env: Union[str, UnsetType] = unset,
        filter_identifier: Union[str, UnsetType] = unset,
        filter_dry_run: Union[bool, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
    ) -> DeploymentGatesListResponse:
        """Get all deployment gates.

        Returns a paginated list of all deployment gates for the organization.
        Use ``page[cursor]`` and ``page[size]`` query parameters to paginate through results.

        :param filter_service: Service name.
        :type filter_service: str, optional
        :param filter_env: Environment name.
        :type filter_env: str, optional
        :param filter_identifier: Gate identifier.
        :type filter_identifier: str, optional
        :param filter_dry_run: Dry-run state.
        :type filter_dry_run: bool, optional
        :param page_cursor: Cursor for pagination. Use the ``meta.page.next_cursor`` value from the previous response. Invalid cursors return 400.
        :type page_cursor: str, optional
        :param page_size: Number of results per page. Defaults to 50. Must be between 1 and 1000.
        :type page_size: int, optional
        :rtype: DeploymentGatesListResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_service is not unset:
            kwargs["filter_service"] = filter_service

        if filter_env is not unset:
            kwargs["filter_env"] = filter_env

        if filter_identifier is not unset:
            kwargs["filter_identifier"] = filter_identifier

        if filter_dry_run is not unset:
            kwargs["filter_dry_run"] = filter_dry_run

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if page_size is not unset:
            kwargs["page_size"] = page_size

        return self._list_deployment_gates_endpoint.call_with_http_info(**kwargs)

    def list_deployment_rule_evaluations(
        self,
        *,
        filter_from: Union[datetime, UnsetType] = unset,
        filter_to: Union[datetime, UnsetType] = unset,
        filter_gate_evaluation_id: Union[UUID, UnsetType] = unset,
        filter_evaluation_id: Union[UUID, UnsetType] = unset,
        filter_gate_id: Union[UUID, UnsetType] = unset,
        filter_rule_id: Union[UUID, UnsetType] = unset,
        filter_service: Union[List[str], UnsetType] = unset,
        filter_env: Union[List[str], UnsetType] = unset,
        filter_identifier: Union[List[str], UnsetType] = unset,
        filter_version: Union[List[str], UnsetType] = unset,
        filter_status: Union[List[DeploymentGatesEvaluationResultResponseAttributesGateStatus], UnsetType] = unset,
        filter_type: Union[List[DeploymentGateRuleEvaluationType], UnsetType] = unset,
        filter_dry_run: Union[bool, UnsetType] = unset,
        filter_gate_dry_run: Union[bool, UnsetType] = unset,
        filter_name: Union[List[str], UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
    ) -> DeploymentGateRuleEvaluationsResponse:
        """List deployment gate rule evaluations.

        Returns rule evaluations whose gate evaluation started in a maximum 30-day window (the default is the previous 24 hours).
        Filter by gate, rule, gate evaluation, or rule evaluation ID; omit IDs for cross-evaluation searches.
        Results are ordered by start time, newest first.
        In-progress state is near-real-time and mutable. Finished state is eventually consistent.
        Gate-level and rule-level dry-run states are independent.
        Pagination is deterministic but not snapshot isolated; clients should deduplicate by rule evaluation ID.

        :param filter_from: Inclusive gate evaluation start time. Defaults to 24 hours before the request. Together with ``filter[to]`` , the window may span no more than 30 days.
        :type filter_from: datetime, optional
        :param filter_to: Exclusive gate evaluation start time. Defaults to the request time. Must be after ``filter[from]`` ; the window may span no more than 30 days.
        :type filter_to: datetime, optional
        :param filter_gate_evaluation_id: Gate evaluation UUID. No match returns an empty list.
        :type filter_gate_evaluation_id: UUID, optional
        :param filter_evaluation_id: Rule evaluation UUID. No match returns an empty list.
        :type filter_evaluation_id: UUID, optional
        :param filter_gate_id: Configured gate UUID. Just-in-time evaluations have no gate ID.
        :type filter_gate_id: UUID, optional
        :param filter_rule_id: Configured rule UUID. Just-in-time rules have no rule ID.
        :type filter_rule_id: UUID, optional
        :param filter_service: Evaluated service values. Repeated or comma-separated values are combined with OR.
        :type filter_service: [str], optional
        :param filter_env: Evaluated environment values. Repeated or comma-separated values are combined with OR.
        :type filter_env: [str], optional
        :param filter_identifier: Gate identifier values. Repeated or comma-separated values are combined with OR.
        :type filter_identifier: [str], optional
        :param filter_version: Evaluated deployment version values. Repeated or comma-separated values are combined with OR.
        :type filter_version: [str], optional
        :param filter_status: Rule statuses. Repeated or comma-separated values are combined with OR.
        :type filter_status: [DeploymentGatesEvaluationResultResponseAttributesGateStatus], optional
        :param filter_type: Rule types. Repeated or comma-separated values are combined with OR.
            Defaults to all rule types.
        :type filter_type: [DeploymentGateRuleEvaluationType], optional
        :param filter_dry_run: Rule-level dry-run state. A failed dry-run rule is ignored when computing the gate outcome.
        :type filter_dry_run: bool, optional
        :param filter_gate_dry_run: Gate-level dry-run state. A failed dry-run gate blocks but does not stop deployment.
        :type filter_gate_dry_run: bool, optional
        :param filter_name: Rule names. Repeated or comma-separated values are combined with OR.
        :type filter_name: [str], optional
        :param page_size: Maximum rule evaluations returned.
        :type page_size: int, optional
        :param page_cursor: Opaque cursor returned in ``meta.page.next_cursor`` by the previous page. Invalid cursors return 400.
        :type page_cursor: str, optional
        :rtype: DeploymentGateRuleEvaluationsResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_from is not unset:
            kwargs["filter_from"] = filter_from

        if filter_to is not unset:
            kwargs["filter_to"] = filter_to

        if filter_gate_evaluation_id is not unset:
            kwargs["filter_gate_evaluation_id"] = filter_gate_evaluation_id

        if filter_evaluation_id is not unset:
            kwargs["filter_evaluation_id"] = filter_evaluation_id

        if filter_gate_id is not unset:
            kwargs["filter_gate_id"] = filter_gate_id

        if filter_rule_id is not unset:
            kwargs["filter_rule_id"] = filter_rule_id

        if filter_service is not unset:
            kwargs["filter_service"] = filter_service

        if filter_env is not unset:
            kwargs["filter_env"] = filter_env

        if filter_identifier is not unset:
            kwargs["filter_identifier"] = filter_identifier

        if filter_version is not unset:
            kwargs["filter_version"] = filter_version

        if filter_status is not unset:
            kwargs["filter_status"] = filter_status

        if filter_type is not unset:
            kwargs["filter_type"] = filter_type

        if filter_dry_run is not unset:
            kwargs["filter_dry_run"] = filter_dry_run

        if filter_gate_dry_run is not unset:
            kwargs["filter_gate_dry_run"] = filter_gate_dry_run

        if filter_name is not unset:
            kwargs["filter_name"] = filter_name

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        return self._list_deployment_rule_evaluations_endpoint.call_with_http_info(**kwargs)

    def list_deployment_rule_evaluations_with_pagination(
        self,
        *,
        filter_from: Union[datetime, UnsetType] = unset,
        filter_to: Union[datetime, UnsetType] = unset,
        filter_gate_evaluation_id: Union[UUID, UnsetType] = unset,
        filter_evaluation_id: Union[UUID, UnsetType] = unset,
        filter_gate_id: Union[UUID, UnsetType] = unset,
        filter_rule_id: Union[UUID, UnsetType] = unset,
        filter_service: Union[List[str], UnsetType] = unset,
        filter_env: Union[List[str], UnsetType] = unset,
        filter_identifier: Union[List[str], UnsetType] = unset,
        filter_version: Union[List[str], UnsetType] = unset,
        filter_status: Union[List[DeploymentGatesEvaluationResultResponseAttributesGateStatus], UnsetType] = unset,
        filter_type: Union[List[DeploymentGateRuleEvaluationType], UnsetType] = unset,
        filter_dry_run: Union[bool, UnsetType] = unset,
        filter_gate_dry_run: Union[bool, UnsetType] = unset,
        filter_name: Union[List[str], UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[DeploymentGateRuleEvaluationData]:
        """List deployment gate rule evaluations.

        Provide a paginated version of :meth:`list_deployment_rule_evaluations`, returning all items.

        :param filter_from: Inclusive gate evaluation start time. Defaults to 24 hours before the request. Together with ``filter[to]`` , the window may span no more than 30 days.
        :type filter_from: datetime, optional
        :param filter_to: Exclusive gate evaluation start time. Defaults to the request time. Must be after ``filter[from]`` ; the window may span no more than 30 days.
        :type filter_to: datetime, optional
        :param filter_gate_evaluation_id: Gate evaluation UUID. No match returns an empty list.
        :type filter_gate_evaluation_id: UUID, optional
        :param filter_evaluation_id: Rule evaluation UUID. No match returns an empty list.
        :type filter_evaluation_id: UUID, optional
        :param filter_gate_id: Configured gate UUID. Just-in-time evaluations have no gate ID.
        :type filter_gate_id: UUID, optional
        :param filter_rule_id: Configured rule UUID. Just-in-time rules have no rule ID.
        :type filter_rule_id: UUID, optional
        :param filter_service: Evaluated service values. Repeated or comma-separated values are combined with OR.
        :type filter_service: [str], optional
        :param filter_env: Evaluated environment values. Repeated or comma-separated values are combined with OR.
        :type filter_env: [str], optional
        :param filter_identifier: Gate identifier values. Repeated or comma-separated values are combined with OR.
        :type filter_identifier: [str], optional
        :param filter_version: Evaluated deployment version values. Repeated or comma-separated values are combined with OR.
        :type filter_version: [str], optional
        :param filter_status: Rule statuses. Repeated or comma-separated values are combined with OR.
        :type filter_status: [DeploymentGatesEvaluationResultResponseAttributesGateStatus], optional
        :param filter_type: Rule types. Repeated or comma-separated values are combined with OR.
            Defaults to all rule types.
        :type filter_type: [DeploymentGateRuleEvaluationType], optional
        :param filter_dry_run: Rule-level dry-run state. A failed dry-run rule is ignored when computing the gate outcome.
        :type filter_dry_run: bool, optional
        :param filter_gate_dry_run: Gate-level dry-run state. A failed dry-run gate blocks but does not stop deployment.
        :type filter_gate_dry_run: bool, optional
        :param filter_name: Rule names. Repeated or comma-separated values are combined with OR.
        :type filter_name: [str], optional
        :param page_size: Maximum rule evaluations returned.
        :type page_size: int, optional
        :param page_cursor: Opaque cursor returned in ``meta.page.next_cursor`` by the previous page. Invalid cursors return 400.
        :type page_cursor: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[DeploymentGateRuleEvaluationData]
        """
        kwargs: Dict[str, Any] = {}
        if filter_from is not unset:
            kwargs["filter_from"] = filter_from

        if filter_to is not unset:
            kwargs["filter_to"] = filter_to

        if filter_gate_evaluation_id is not unset:
            kwargs["filter_gate_evaluation_id"] = filter_gate_evaluation_id

        if filter_evaluation_id is not unset:
            kwargs["filter_evaluation_id"] = filter_evaluation_id

        if filter_gate_id is not unset:
            kwargs["filter_gate_id"] = filter_gate_id

        if filter_rule_id is not unset:
            kwargs["filter_rule_id"] = filter_rule_id

        if filter_service is not unset:
            kwargs["filter_service"] = filter_service

        if filter_env is not unset:
            kwargs["filter_env"] = filter_env

        if filter_identifier is not unset:
            kwargs["filter_identifier"] = filter_identifier

        if filter_version is not unset:
            kwargs["filter_version"] = filter_version

        if filter_status is not unset:
            kwargs["filter_status"] = filter_status

        if filter_type is not unset:
            kwargs["filter_type"] = filter_type

        if filter_dry_run is not unset:
            kwargs["filter_dry_run"] = filter_dry_run

        if filter_gate_dry_run is not unset:
            kwargs["filter_gate_dry_run"] = filter_gate_dry_run

        if filter_name is not unset:
            kwargs["filter_name"] = filter_name

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        local_page_size = get_attribute_from_path(kwargs, "page_size", 50)
        endpoint = self._list_deployment_rule_evaluations_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "page_cursor",
            "cursor_path": "meta.page.next_cursor",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def trigger_deployment_gates_evaluation(
        self,
        body: DeploymentGatesEvaluationRequest,
    ) -> DeploymentGatesEvaluationResponse:
        """Trigger a deployment gate evaluation.

        Triggers an asynchronous deployment gate evaluation for the given service and environment.
        Returns an evaluation ID that can be used to poll for the result via the
        ``GET /api/v2/deployments/gates/evaluation/{id}`` endpoint.

        When the ``configuration`` attribute is provided, rules are evaluated inline from that configuration
        and no pre-configured gate is required. When ``configuration`` is omitted, rules are resolved from the
        gate pre-configured for the given service and environment through the Datadog UI, API, or Terraform.

        :type body: DeploymentGatesEvaluationRequest
        :rtype: DeploymentGatesEvaluationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._trigger_deployment_gates_evaluation_endpoint.call_with_http_info(**kwargs)

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
