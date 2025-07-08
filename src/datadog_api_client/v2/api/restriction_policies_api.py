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
from datadog_api_client.v2.model.restriction_policy_response import RestrictionPolicyResponse
from datadog_api_client.v2.model.restriction_policy_update_request import RestrictionPolicyUpdateRequest


class RestrictionPoliciesApi:
    """
    A restriction policy defines the access control rules for a resource, mapping a set of relations
    (such as editor and viewer) to a set of allowed principals (such as roles, teams, or users).
    The restriction policy determines who is authorized to perform what actions on the resource.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._delete_restriction_policy_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/restriction_policy/{resource_id}",
                "operation_id": "delete_restriction_policy",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "resource_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "resource_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_restriction_policy_endpoint = _Endpoint(
            settings={
                "response_type": (RestrictionPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/restriction_policy/{resource_id}",
                "operation_id": "get_restriction_policy",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "resource_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "resource_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_restriction_policy_endpoint = _Endpoint(
            settings={
                "response_type": (RestrictionPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/restriction_policy/{resource_id}",
                "operation_id": "update_restriction_policy",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "resource_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "resource_id",
                    "location": "path",
                },
                "allow_self_lockout": {
                    "openapi_types": (bool,),
                    "attribute": "allow_self_lockout",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RestrictionPolicyUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def delete_restriction_policy(
        self,
        resource_id: str,
    ) -> None:
        """Delete a restriction policy.

        Deletes the restriction policy associated with a specified resource.

        :param resource_id: Identifier, formatted as ``type:id``. Supported types: ``connection`` , ``dashboard`` , ``integration-account`` , ``integration-service`` , ``integration-webhook`` , ``notebook`` , ``reference-table`` , ``security-rule`` , ``slo`` , ``workflow`` , ``app-builder-app`` , ``connection`` , ``connection-group`` , ``rum-application`` , ``cross-org-connection`` , ``spreadsheet``.
        :type resource_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["resource_id"] = resource_id

        return self._delete_restriction_policy_endpoint.call_with_http_info(**kwargs)

    def get_restriction_policy(
        self,
        resource_id: str,
    ) -> RestrictionPolicyResponse:
        """Get a restriction policy.

        Retrieves the restriction policy associated with a specified resource.

        :param resource_id: Identifier, formatted as ``type:id``. Supported types: ``connection`` , ``dashboard`` , ``integration-account`` , ``integration-service`` , ``integration-webhook`` , ``notebook`` , ``reference-table`` , ``security-rule`` , ``slo`` , ``workflow`` , ``app-builder-app`` , ``connection`` , ``connection-group`` , ``rum-application`` , ``cross-org-connection`` , ``spreadsheet``.
        :type resource_id: str
        :rtype: RestrictionPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["resource_id"] = resource_id

        return self._get_restriction_policy_endpoint.call_with_http_info(**kwargs)

    def update_restriction_policy(
        self,
        resource_id: str,
        body: RestrictionPolicyUpdateRequest,
        *,
        allow_self_lockout: Union[bool, UnsetType] = unset,
    ) -> RestrictionPolicyResponse:
        """Update a restriction policy.

        Updates the restriction policy associated with a resource.

        **Supported resources**

        Restriction policies can be applied to the following resources:

        * Dashboards: ``dashboard``
        * Integration Accounts: ``integration-account``
        * Integration Services: ``integration-service``
        * Integration Webhooks: ``integration-webhook``
        * Notebooks: ``notebook``
        * Powerpacks: ``powerpack``
        * Reference Tables: ``reference-table``
        * Security Rules: ``security-rule``
        * Service Level Objectives: ``slo``
        * Synthetic Global Variables: ``synthetics-global-variable``
        * Synthetic Tests: ``synthetics-test``
        * Synthetic Private Locations: ``synthetics-private-location``
        * Monitors: ``monitor``
        * Workflows: ``workflow``
        * App Builder Apps: ``app-builder-app``
        * Connections: ``connection``
        * Connection Groups: ``connection-group``
        * RUM Applications: ``rum-application``
        * Cross Org Connections: ``cross-org-connection``
        * Spreadsheets: ``spreadsheet``

        **Supported relations for resources**

        .. list-table::
           :header-rows: 1

           * - Resource Type
             - Supported Relations
           * - Dashboards
             - ``viewer`` , ``editor``
           * - Integration Accounts
             - ``viewer`` , ``editor``
           * - Integration Services
             - ``viewer`` , ``editor``
           * - Integration Webhooks
             - ``viewer`` , ``editor``
           * - Notebooks
             - ``viewer`` , ``editor``
           * - Powerpacks
             - ``viewer`` , ``editor``
           * - Security Rules
             - ``viewer`` , ``editor``
           * - Service Level Objectives
             - ``viewer`` , ``editor``
           * - Synthetic Global Variables
             - ``viewer`` , ``editor``
           * - Synthetic Tests
             - ``viewer`` , ``editor``
           * - Synthetic Private Locations
             - ``viewer`` , ``editor``
           * - Monitors
             - ``viewer`` , ``editor``
           * - Reference Tables
             - ``viewer`` , ``editor``
           * - Workflows
             - ``viewer`` , ``runner`` , ``editor``
           * - App Builder Apps
             - ``viewer`` , ``editor``
           * - Connections
             - ``viewer`` , ``resolver`` , ``editor``
           * - Connection Groups
             - ``viewer`` , ``editor``
           * - RUM Application
             - ``viewer`` , ``editor``
           * - Cross Org Connections
             - ``viewer`` , ``editor``
           * - Spreadsheets
             - ``viewer`` , ``editor``


        :param resource_id: Identifier, formatted as ``type:id``. Supported types: ``connection`` , ``dashboard`` , ``integration-account`` , ``integration-service`` , ``integration-webhook`` , ``notebook`` , ``reference-table`` , ``security-rule`` , ``slo`` , ``workflow`` , ``app-builder-app`` , ``connection`` , ``connection-group`` , ``rum-application`` , ``cross-org-connection`` , ``spreadsheet``.
        :type resource_id: str
        :param body: Restriction policy payload
        :type body: RestrictionPolicyUpdateRequest
        :param allow_self_lockout: Allows admins (users with the ``user_access_manage`` permission) to remove their own access from the resource if set to ``true``. By default, this is set to ``false`` , preventing admins from locking themselves out.
        :type allow_self_lockout: bool, optional
        :rtype: RestrictionPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["resource_id"] = resource_id

        if allow_self_lockout is not unset:
            kwargs["allow_self_lockout"] = allow_self_lockout

        kwargs["body"] = body

        return self._update_restriction_policy_endpoint.call_with_http_info(**kwargs)
