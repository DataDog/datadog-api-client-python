# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.escalation_policy import EscalationPolicy
from datadog_api_client.v2.model.escalation_policy_create_request import EscalationPolicyCreateRequest
from datadog_api_client.v2.model.escalation_policy_update_request import EscalationPolicyUpdateRequest
from datadog_api_client.v2.model.schedule import Schedule
from datadog_api_client.v2.model.schedule_create_request import ScheduleCreateRequest
from datadog_api_client.v2.model.schedule_update_request import ScheduleUpdateRequest
from datadog_api_client.v2.model.shift import Shift
from datadog_api_client.v2.model.team_on_call_responders import TeamOnCallResponders
from datadog_api_client.v2.model.team_routing_rules import TeamRoutingRules
from datadog_api_client.v2.model.team_routing_rules_request import TeamRoutingRulesRequest


class OnCallApi:
    """
    Configure your `Datadog On-Call <https://docs.datadoghq.com/service_management/on-call/>`_
    directly through the Datadog API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_on_call_escalation_policy_endpoint = _Endpoint(
            settings={
                "response_type": (EscalationPolicy,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/escalation-policies",
                "operation_id": "create_on_call_escalation_policy",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (EscalationPolicyCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_on_call_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (Schedule,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/schedules",
                "operation_id": "create_on_call_schedule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ScheduleCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_on_call_escalation_policy_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/escalation-policies/{policy_id}",
                "operation_id": "delete_on_call_escalation_policy",
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

        self._delete_on_call_schedule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/schedules/{schedule_id}",
                "operation_id": "delete_on_call_schedule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "schedule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "schedule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_on_call_escalation_policy_endpoint = _Endpoint(
            settings={
                "response_type": (EscalationPolicy,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/escalation-policies/{policy_id}",
                "operation_id": "get_on_call_escalation_policy",
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
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_on_call_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (Schedule,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/schedules/{schedule_id}",
                "operation_id": "get_on_call_schedule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "schedule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "schedule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_on_call_team_routing_rules_endpoint = _Endpoint(
            settings={
                "response_type": (TeamRoutingRules,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/teams/{team_id}/routing-rules",
                "operation_id": "get_on_call_team_routing_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_schedule_on_call_user_endpoint = _Endpoint(
            settings={
                "response_type": (Shift,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/schedules/{schedule_id}/on-call",
                "operation_id": "get_schedule_on_call_user",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "schedule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "schedule_id",
                    "location": "path",
                },
                "filter_at_ts": {
                    "openapi_types": (str,),
                    "attribute": "filter[at_ts]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_team_on_call_users_endpoint = _Endpoint(
            settings={
                "response_type": (TeamOnCallResponders,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/teams/{team_id}/on-call",
                "operation_id": "get_team_on_call_users",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._set_on_call_team_routing_rules_endpoint = _Endpoint(
            settings={
                "response_type": (TeamRoutingRules,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/teams/{team_id}/routing-rules",
                "operation_id": "set_on_call_team_routing_rules",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (TeamRoutingRulesRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_on_call_escalation_policy_endpoint = _Endpoint(
            settings={
                "response_type": (EscalationPolicy,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/escalation-policies/{policy_id}",
                "operation_id": "update_on_call_escalation_policy",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "policy_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "policy_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (EscalationPolicyUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_on_call_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (Schedule,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/schedules/{schedule_id}",
                "operation_id": "update_on_call_schedule",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "schedule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "schedule_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ScheduleUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_on_call_escalation_policy(
        self,
        body: EscalationPolicyCreateRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> EscalationPolicy:
        """Create On-Call escalation policy.

        Create a new On-Call escalation policy

        :type body: EscalationPolicyCreateRequest
        :param include: Comma-separated list of included relationships to be returned. Allowed values: ``teams`` , ``steps`` , ``steps.targets``.
        :type include: str, optional
        :rtype: EscalationPolicy
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._create_on_call_escalation_policy_endpoint.call_with_http_info(**kwargs)

    def create_on_call_schedule(
        self,
        body: ScheduleCreateRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> Schedule:
        """Create On-Call schedule.

        Create a new On-Call schedule

        :type body: ScheduleCreateRequest
        :param include: Comma-separated list of included relationships to be returned. Allowed values: ``teams`` , ``layers`` , ``layers.members`` , ``layers.members.user``.
        :type include: str, optional
        :rtype: Schedule
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._create_on_call_schedule_endpoint.call_with_http_info(**kwargs)

    def delete_on_call_escalation_policy(
        self,
        policy_id: str,
    ) -> None:
        """Delete On-Call escalation policy.

        Delete an On-Call escalation policy

        :param policy_id: The ID of the escalation policy
        :type policy_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        return self._delete_on_call_escalation_policy_endpoint.call_with_http_info(**kwargs)

    def delete_on_call_schedule(
        self,
        schedule_id: str,
    ) -> None:
        """Delete On-Call schedule.

        Delete an On-Call schedule

        :param schedule_id: The ID of the schedule
        :type schedule_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["schedule_id"] = schedule_id

        return self._delete_on_call_schedule_endpoint.call_with_http_info(**kwargs)

    def get_on_call_escalation_policy(
        self,
        policy_id: str,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> EscalationPolicy:
        """Get On-Call escalation policy.

        Get an On-Call escalation policy

        :param policy_id: The ID of the escalation policy
        :type policy_id: str
        :param include: Comma-separated list of included relationships to be returned. Allowed values: ``teams`` , ``steps`` , ``steps.targets``.
        :type include: str, optional
        :rtype: EscalationPolicy
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        if include is not unset:
            kwargs["include"] = include

        return self._get_on_call_escalation_policy_endpoint.call_with_http_info(**kwargs)

    def get_on_call_schedule(
        self,
        schedule_id: str,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> Schedule:
        """Get On-Call schedule.

        Get an On-Call schedule

        :param schedule_id: The ID of the schedule
        :type schedule_id: str
        :param include: Comma-separated list of included relationships to be returned. Allowed values: ``teams`` , ``layers`` , ``layers.members`` , ``layers.members.user``.
        :type include: str, optional
        :rtype: Schedule
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["schedule_id"] = schedule_id

        return self._get_on_call_schedule_endpoint.call_with_http_info(**kwargs)

    def get_on_call_team_routing_rules(
        self,
        team_id: str,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> TeamRoutingRules:
        """Get On-Call team routing rules.

        Get a team's On-Call routing rules

        :param team_id: The team ID
        :type team_id: str
        :param include: Comma-separated list of included relationships to be returned. Allowed values: ``rules`` , ``rules.policy``.
        :type include: str, optional
        :rtype: TeamRoutingRules
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        if include is not unset:
            kwargs["include"] = include

        return self._get_on_call_team_routing_rules_endpoint.call_with_http_info(**kwargs)

    def get_schedule_on_call_user(
        self,
        schedule_id: str,
        *,
        include: Union[str, UnsetType] = unset,
        filter_at_ts: Union[str, UnsetType] = unset,
    ) -> Shift:
        """Get the schedule on-call user.

        Retrieves the user who is on-call for the specified schedule at a given time.

        :param schedule_id: The ID of the schedule.
        :type schedule_id: str
        :param include: Specifies related resources to include in the response as a comma-separated list. Allowed value: ``user``.
        :type include: str, optional
        :param filter_at_ts: Retrieves the on-call user at the given timestamp (ISO-8601). Defaults to the current time if omitted."
        :type filter_at_ts: str, optional
        :rtype: Shift
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["schedule_id"] = schedule_id

        if filter_at_ts is not unset:
            kwargs["filter_at_ts"] = filter_at_ts

        return self._get_schedule_on_call_user_endpoint.call_with_http_info(**kwargs)

    def get_team_on_call_users(
        self,
        team_id: str,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> TeamOnCallResponders:
        """Get team on-call users.

        Get a team's on-call users at a given time

        :param team_id: The team ID
        :type team_id: str
        :param include: Comma-separated list of included relationships to be returned. Allowed values: ``responders`` , ``escalations`` , ``escalations.responders``.
        :type include: str, optional
        :rtype: TeamOnCallResponders
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["team_id"] = team_id

        return self._get_team_on_call_users_endpoint.call_with_http_info(**kwargs)

    def set_on_call_team_routing_rules(
        self,
        team_id: str,
        body: TeamRoutingRulesRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> TeamRoutingRules:
        """Set On-Call team routing rules.

        Set a team's On-Call routing rules

        :param team_id: The team ID
        :type team_id: str
        :type body: TeamRoutingRulesRequest
        :param include: Comma-separated list of included relationships to be returned. Allowed values: ``rules`` , ``rules.policy``.
        :type include: str, optional
        :rtype: TeamRoutingRules
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._set_on_call_team_routing_rules_endpoint.call_with_http_info(**kwargs)

    def update_on_call_escalation_policy(
        self,
        policy_id: str,
        body: EscalationPolicyUpdateRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> EscalationPolicy:
        """Update On-Call escalation policy.

        Update an On-Call escalation policy

        :param policy_id: The ID of the escalation policy
        :type policy_id: str
        :type body: EscalationPolicyUpdateRequest
        :param include: Comma-separated list of included relationships to be returned. Allowed values: ``teams`` , ``steps`` , ``steps.targets``.
        :type include: str, optional
        :rtype: EscalationPolicy
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_on_call_escalation_policy_endpoint.call_with_http_info(**kwargs)

    def update_on_call_schedule(
        self,
        schedule_id: str,
        body: ScheduleUpdateRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> Schedule:
        """Update On-Call schedule.

        Update a new On-Call schedule

        :param schedule_id: The ID of the schedule
        :type schedule_id: str
        :type body: ScheduleUpdateRequest
        :param include: Comma-separated list of included relationships to be returned. Allowed values: ``teams`` , ``layers`` , ``layers.members`` , ``layers.members.user``.
        :type include: str, optional
        :rtype: Schedule
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["schedule_id"] = schedule_id

        kwargs["body"] = body

        return self._update_on_call_schedule_endpoint.call_with_http_info(**kwargs)
