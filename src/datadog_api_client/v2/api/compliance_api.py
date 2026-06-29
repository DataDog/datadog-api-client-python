# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union
import warnings

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.rule_based_view_response import RuleBasedViewResponse


class ComplianceApi:
    """
    Datadog Cloud Security Misconfigurations provides aggregated views of
    compliance rules and findings across your cloud resources, helping you assess
    posture against industry frameworks (such as HIPAA, SOC 2, ISO 27001) and custom
    frameworks. Learn more at https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/#maintain-compliance-with-industry-frameworks-and-benchmarks.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_rule_based_view_endpoint = _Endpoint(
            settings={
                "response_type": (RuleBasedViewResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/compliance_findings/rule_based_view",
                "operation_id": "get_rule_based_view",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "to": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "to",
                    "location": "query",
                },
                "framework": {
                    "openapi_types": (str,),
                    "attribute": "framework",
                    "location": "query",
                },
                "version": {
                    "openapi_types": (str,),
                    "attribute": "version",
                    "location": "query",
                },
                "query_findings_without_framework_version": {
                    "openapi_types": (bool,),
                    "attribute": "query_findings_without_framework_version",
                    "location": "query",
                },
                "include_rules_without_findings": {
                    "openapi_types": (bool,),
                    "attribute": "include_rules_without_findings",
                    "location": "query",
                },
                "is_custom": {
                    "openapi_types": (bool,),
                    "attribute": "is_custom",
                    "location": "query",
                },
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def get_rule_based_view(
        self,
        to: int,
        *,
        framework: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        query_findings_without_framework_version: Union[bool, UnsetType] = unset,
        include_rules_without_findings: Union[bool, UnsetType] = unset,
        is_custom: Union[bool, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
    ) -> RuleBasedViewResponse:
        """Get the rule-based view of compliance findings. **Deprecated**.

        **This endpoint is deprecated.** Use the `Security Monitoring - Search Security Findings <https://docs.datadoghq.com/api/latest/security-monitoring/search-security-findings/>`_ endpoint instead.

        Get an aggregated view of compliance rules with their pass, fail, and muted finding counts.
        Supports filtering by compliance framework, framework version, and additional query filters.

        :param to: Timestamp of the query end, in milliseconds since the Unix epoch.
        :type to: int
        :param framework: Compliance framework handle to filter rules and findings by.
        :type framework: str, optional
        :param version: Version of the compliance framework to filter rules and findings by.
        :type version: str, optional
        :param query_findings_without_framework_version: When ``true`` , returns findings without a ``framework_version`` tag. Used for findings from custom frameworks or those created before framework versioning was introduced.
        :type query_findings_without_framework_version: bool, optional
        :param include_rules_without_findings: When ``true`` , includes rules in the response that have no associated findings.
        :type include_rules_without_findings: bool, optional
        :param is_custom: Set to ``true`` when the requested ``framework`` is a custom framework.
        :type is_custom: bool, optional
        :param query: Additional event-platform filters applied to the underlying findings query. For example, ``scored:true project_id:datadog-prod-us5``.
        :type query: str, optional
        :rtype: RuleBasedViewResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["to"] = to

        if framework is not unset:
            kwargs["framework"] = framework

        if version is not unset:
            kwargs["version"] = version

        if query_findings_without_framework_version is not unset:
            kwargs["query_findings_without_framework_version"] = query_findings_without_framework_version

        if include_rules_without_findings is not unset:
            kwargs["include_rules_without_findings"] = include_rules_without_findings

        if is_custom is not unset:
            kwargs["is_custom"] = is_custom

        if query is not unset:
            kwargs["query"] = query

        warnings.warn("get_rule_based_view is deprecated", DeprecationWarning, stacklevel=2)
        return self._get_rule_based_view_endpoint.call_with_http_info(**kwargs)
