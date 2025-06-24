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
from datadog_api_client.v2.model.monitor_notification_rule_list_response import MonitorNotificationRuleListResponse
from datadog_api_client.v2.model.monitor_notification_rule_response import MonitorNotificationRuleResponse
from datadog_api_client.v2.model.monitor_notification_rule_create_request import MonitorNotificationRuleCreateRequest
from datadog_api_client.v2.model.monitor_notification_rule_update_request import MonitorNotificationRuleUpdateRequest
from datadog_api_client.v2.model.monitor_config_policy_list_response import MonitorConfigPolicyListResponse
from datadog_api_client.v2.model.monitor_config_policy_response import MonitorConfigPolicyResponse
from datadog_api_client.v2.model.monitor_config_policy_create_request import MonitorConfigPolicyCreateRequest
from datadog_api_client.v2.model.monitor_config_policy_edit_request import MonitorConfigPolicyEditRequest
from datadog_api_client.v2.model.monitor_user_template_list_response import MonitorUserTemplateListResponse
from datadog_api_client.v2.model.monitor_user_template_create_response import MonitorUserTemplateCreateResponse
from datadog_api_client.v2.model.monitor_user_template_create_request import MonitorUserTemplateCreateRequest
from datadog_api_client.v2.model.monitor_user_template_response import MonitorUserTemplateResponse
from datadog_api_client.v2.model.monitor_user_template_update_request import MonitorUserTemplateUpdateRequest


class MonitorsApi:
    """
    `Monitors <https://docs.datadoghq.com/monitors>`_ allow you to watch a metric or check that you care about and
    notifies your team when a defined threshold has exceeded.

    For more information, see `Creating Monitors <https://docs.datadoghq.com/monitors/create/types/>`_ and
    `Tag Policies <https://docs.datadoghq.com/monitors/settings/>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_monitor_config_policy_endpoint = _Endpoint(
            settings={
                "response_type": (MonitorConfigPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/monitor/policy",
                "operation_id": "create_monitor_config_policy",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (MonitorConfigPolicyCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_monitor_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (MonitorNotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/monitor/notification_rule",
                "operation_id": "create_monitor_notification_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (MonitorNotificationRuleCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_monitor_user_template_endpoint = _Endpoint(
            settings={
                "response_type": (MonitorUserTemplateCreateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/monitor/template",
                "operation_id": "create_monitor_user_template",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (MonitorUserTemplateCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_monitor_config_policy_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/monitor/policy/{policy_id}",
                "operation_id": "delete_monitor_config_policy",
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

        self._delete_monitor_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/monitor/notification_rule/{rule_id}",
                "operation_id": "delete_monitor_notification_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_monitor_user_template_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/monitor/template/{template_id}",
                "operation_id": "delete_monitor_user_template",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "template_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_monitor_config_policy_endpoint = _Endpoint(
            settings={
                "response_type": (MonitorConfigPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/monitor/policy/{policy_id}",
                "operation_id": "get_monitor_config_policy",
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

        self._get_monitor_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (MonitorNotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/monitor/notification_rule/{rule_id}",
                "operation_id": "get_monitor_notification_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
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

        self._get_monitor_notification_rules_endpoint = _Endpoint(
            settings={
                "response_type": (MonitorNotificationRuleListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/monitor/notification_rule",
                "operation_id": "get_monitor_notification_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
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

        self._get_monitor_user_template_endpoint = _Endpoint(
            settings={
                "response_type": (MonitorUserTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/monitor/template/{template_id}",
                "operation_id": "get_monitor_user_template",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "template_id",
                    "location": "path",
                },
                "with_all_versions": {
                    "openapi_types": (bool,),
                    "attribute": "with_all_versions",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_monitor_config_policies_endpoint = _Endpoint(
            settings={
                "response_type": (MonitorConfigPolicyListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/monitor/policy",
                "operation_id": "list_monitor_config_policies",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_monitor_user_templates_endpoint = _Endpoint(
            settings={
                "response_type": (MonitorUserTemplateListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/monitor/template",
                "operation_id": "list_monitor_user_templates",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_monitor_config_policy_endpoint = _Endpoint(
            settings={
                "response_type": (MonitorConfigPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/monitor/policy/{policy_id}",
                "operation_id": "update_monitor_config_policy",
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
                    "openapi_types": (MonitorConfigPolicyEditRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_monitor_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (MonitorNotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/monitor/notification_rule/{rule_id}",
                "operation_id": "update_monitor_notification_rule",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (MonitorNotificationRuleUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_monitor_user_template_endpoint = _Endpoint(
            settings={
                "response_type": (MonitorUserTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/monitor/template/{template_id}",
                "operation_id": "update_monitor_user_template",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "template_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (MonitorUserTemplateUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._validate_existing_monitor_user_template_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/monitor/template/{template_id}/validate",
                "operation_id": "validate_existing_monitor_user_template",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "template_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (MonitorUserTemplateUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._validate_monitor_user_template_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/monitor/template/validate",
                "operation_id": "validate_monitor_user_template",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (MonitorUserTemplateCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_monitor_config_policy(
        self,
        body: MonitorConfigPolicyCreateRequest,
    ) -> MonitorConfigPolicyResponse:
        """Create a monitor configuration policy.

        Create a monitor configuration policy.

        :param body: Create a monitor configuration policy request body.
        :type body: MonitorConfigPolicyCreateRequest
        :rtype: MonitorConfigPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_monitor_config_policy_endpoint.call_with_http_info(**kwargs)

    def create_monitor_notification_rule(
        self,
        body: MonitorNotificationRuleCreateRequest,
    ) -> MonitorNotificationRuleResponse:
        """Create a monitor notification rule.

        Creates a monitor notification rule.

        :param body: Request body to create a monitor notification rule.
        :type body: MonitorNotificationRuleCreateRequest
        :rtype: MonitorNotificationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_monitor_notification_rule_endpoint.call_with_http_info(**kwargs)

    def create_monitor_user_template(
        self,
        body: MonitorUserTemplateCreateRequest,
    ) -> MonitorUserTemplateCreateResponse:
        """Create a monitor user template.

        Create a new monitor user template.

        :type body: MonitorUserTemplateCreateRequest
        :rtype: MonitorUserTemplateCreateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_monitor_user_template_endpoint.call_with_http_info(**kwargs)

    def delete_monitor_config_policy(
        self,
        policy_id: str,
    ) -> None:
        """Delete a monitor configuration policy.

        Delete a monitor configuration policy.

        :param policy_id: ID of the monitor configuration policy.
        :type policy_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        return self._delete_monitor_config_policy_endpoint.call_with_http_info(**kwargs)

    def delete_monitor_notification_rule(
        self,
        rule_id: str,
    ) -> None:
        """Delete a monitor notification rule.

        Deletes a monitor notification rule by ``rule_id``.

        :param rule_id: ID of the monitor notification rule to delete.
        :type rule_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._delete_monitor_notification_rule_endpoint.call_with_http_info(**kwargs)

    def delete_monitor_user_template(
        self,
        template_id: str,
    ) -> None:
        """Delete a monitor user template.

        Delete an existing monitor user template by its ID.

        :param template_id: ID of the monitor user template.
        :type template_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id

        return self._delete_monitor_user_template_endpoint.call_with_http_info(**kwargs)

    def get_monitor_config_policy(
        self,
        policy_id: str,
    ) -> MonitorConfigPolicyResponse:
        """Get a monitor configuration policy.

        Get a monitor configuration policy by ``policy_id``.

        :param policy_id: ID of the monitor configuration policy.
        :type policy_id: str
        :rtype: MonitorConfigPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        return self._get_monitor_config_policy_endpoint.call_with_http_info(**kwargs)

    def get_monitor_notification_rule(
        self,
        rule_id: str,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> MonitorNotificationRuleResponse:
        """Get a monitor notification rule.

        Returns a monitor notification rule by ``rule_id``.

        :param rule_id: ID of the monitor notification rule to fetch.
        :type rule_id: str
        :param include: Comma-separated list of resource paths for related resources to include in the response. Supported resource
            path is ``created_by``.
        :type include: str, optional
        :rtype: MonitorNotificationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        if include is not unset:
            kwargs["include"] = include

        return self._get_monitor_notification_rule_endpoint.call_with_http_info(**kwargs)

    def get_monitor_notification_rules(
        self,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> MonitorNotificationRuleListResponse:
        """Get all monitor notification rules.

        Returns a list of all monitor notification rules.

        :param include: Comma-separated list of resource paths for related resources to include in the response. Supported resource
            path is ``created_by``.
        :type include: str, optional
        :rtype: MonitorNotificationRuleListResponse
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        return self._get_monitor_notification_rules_endpoint.call_with_http_info(**kwargs)

    def get_monitor_user_template(
        self,
        template_id: str,
        *,
        with_all_versions: Union[bool, UnsetType] = unset,
    ) -> MonitorUserTemplateResponse:
        """Get a monitor user template.

        Retrieve a monitor user template by its ID.

        :param template_id: ID of the monitor user template.
        :type template_id: str
        :param with_all_versions: Whether to include all versions of the template in the response in the versions field.
        :type with_all_versions: bool, optional
        :rtype: MonitorUserTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id

        if with_all_versions is not unset:
            kwargs["with_all_versions"] = with_all_versions

        return self._get_monitor_user_template_endpoint.call_with_http_info(**kwargs)

    def list_monitor_config_policies(
        self,
    ) -> MonitorConfigPolicyListResponse:
        """Get all monitor configuration policies.

        Get all monitor configuration policies.

        :rtype: MonitorConfigPolicyListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_monitor_config_policies_endpoint.call_with_http_info(**kwargs)

    def list_monitor_user_templates(
        self,
    ) -> MonitorUserTemplateListResponse:
        """Get all monitor user templates.

        Retrieve all monitor user templates.

        :rtype: MonitorUserTemplateListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_monitor_user_templates_endpoint.call_with_http_info(**kwargs)

    def update_monitor_config_policy(
        self,
        policy_id: str,
        body: MonitorConfigPolicyEditRequest,
    ) -> MonitorConfigPolicyResponse:
        """Edit a monitor configuration policy.

        Edit a monitor configuration policy.

        :param policy_id: ID of the monitor configuration policy.
        :type policy_id: str
        :param body: Description of the update.
        :type body: MonitorConfigPolicyEditRequest
        :rtype: MonitorConfigPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        kwargs["body"] = body

        return self._update_monitor_config_policy_endpoint.call_with_http_info(**kwargs)

    def update_monitor_notification_rule(
        self,
        rule_id: str,
        body: MonitorNotificationRuleUpdateRequest,
    ) -> MonitorNotificationRuleResponse:
        """Update a monitor notification rule.

        Updates a monitor notification rule by ``rule_id``.

        :param rule_id: ID of the monitor notification rule to update.
        :type rule_id: str
        :param body: Request body to update the monitor notification rule.
        :type body: MonitorNotificationRuleUpdateRequest
        :rtype: MonitorNotificationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        kwargs["body"] = body

        return self._update_monitor_notification_rule_endpoint.call_with_http_info(**kwargs)

    def update_monitor_user_template(
        self,
        template_id: str,
        body: MonitorUserTemplateUpdateRequest,
    ) -> MonitorUserTemplateResponse:
        """Update a monitor user template to a new version.

        Creates a new version of an existing monitor user template.

        :param template_id: ID of the monitor user template.
        :type template_id: str
        :type body: MonitorUserTemplateUpdateRequest
        :rtype: MonitorUserTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id

        kwargs["body"] = body

        return self._update_monitor_user_template_endpoint.call_with_http_info(**kwargs)

    def validate_existing_monitor_user_template(
        self,
        template_id: str,
        body: MonitorUserTemplateUpdateRequest,
    ) -> None:
        """Validate an existing monitor user template.

        Validate the structure and content of an existing monitor user template being updated to a new version.

        :param template_id: ID of the monitor user template.
        :type template_id: str
        :type body: MonitorUserTemplateUpdateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id

        kwargs["body"] = body

        return self._validate_existing_monitor_user_template_endpoint.call_with_http_info(**kwargs)

    def validate_monitor_user_template(
        self,
        body: MonitorUserTemplateCreateRequest,
    ) -> None:
        """Validate a monitor user template.

        Validate the structure and content of a monitor user template.

        :type body: MonitorUserTemplateCreateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._validate_monitor_user_template_endpoint.call_with_http_info(**kwargs)
