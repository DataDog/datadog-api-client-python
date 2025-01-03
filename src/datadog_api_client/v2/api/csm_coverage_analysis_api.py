# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.csm_cloud_accounts_coverage_analysis_response import (
    CsmCloudAccountsCoverageAnalysisResponse,
)
from datadog_api_client.v2.model.csm_hosts_and_containers_coverage_analysis_response import (
    CsmHostsAndContainersCoverageAnalysisResponse,
)
from datadog_api_client.v2.model.csm_serverless_coverage_analysis_response import CsmServerlessCoverageAnalysisResponse


class CSMCoverageAnalysisApi:
    """
    Datadog Cloud Security Management (CSM) delivers real-time threat detection
    and continuous configuration audits across your entire cloud infrastructure,
    all in a unified view for seamless collaboration and faster remediation.
    Go to https://docs.datadoghq.com/security/cloud_security_management to learn more.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_csm_cloud_accounts_coverage_analysis_endpoint = _Endpoint(
            settings={
                "response_type": (CsmCloudAccountsCoverageAnalysisResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/onboarding/coverage_analysis/cloud_accounts",
                "operation_id": "get_csm_cloud_accounts_coverage_analysis",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_csm_hosts_and_containers_coverage_analysis_endpoint = _Endpoint(
            settings={
                "response_type": (CsmHostsAndContainersCoverageAnalysisResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/onboarding/coverage_analysis/hosts_and_containers",
                "operation_id": "get_csm_hosts_and_containers_coverage_analysis",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_csm_serverless_coverage_analysis_endpoint = _Endpoint(
            settings={
                "response_type": (CsmServerlessCoverageAnalysisResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/onboarding/coverage_analysis/serverless",
                "operation_id": "get_csm_serverless_coverage_analysis",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def get_csm_cloud_accounts_coverage_analysis(
        self,
    ) -> CsmCloudAccountsCoverageAnalysisResponse:
        """Get the CSM Cloud Accounts Coverage Analysis.

        Get the CSM Coverage Analysis of your Cloud Accounts.
        This is calculated based on the number of your Cloud Accounts that are
        scanned for security issues.

        :rtype: CsmCloudAccountsCoverageAnalysisResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_csm_cloud_accounts_coverage_analysis_endpoint.call_with_http_info(**kwargs)

    def get_csm_hosts_and_containers_coverage_analysis(
        self,
    ) -> CsmHostsAndContainersCoverageAnalysisResponse:
        """Get the CSM Hosts and Containers Coverage Analysis.

        Get the CSM Coverage Analysis of your Hosts and Containers.
        This is calculated based on the number of agents running on your Hosts
        and Containers with CSM feature(s) enabled.

        :rtype: CsmHostsAndContainersCoverageAnalysisResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_csm_hosts_and_containers_coverage_analysis_endpoint.call_with_http_info(**kwargs)

    def get_csm_serverless_coverage_analysis(
        self,
    ) -> CsmServerlessCoverageAnalysisResponse:
        """Get the CSM Serverless Coverage Analysis.

        Get the CSM Coverage Analysis of your Serverless Resources.
        This is calculated based on the number of agents running on your Serverless
        Resources with CSM feature(s) enabled.

        :rtype: CsmServerlessCoverageAnalysisResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_csm_serverless_coverage_analysis_endpoint.call_with_http_info(**kwargs)
