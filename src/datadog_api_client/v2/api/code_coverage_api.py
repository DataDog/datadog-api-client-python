# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.coverage_summary_response import CoverageSummaryResponse
from datadog_api_client.v2.model.branch_coverage_summary_request import BranchCoverageSummaryRequest
from datadog_api_client.v2.model.commit_coverage_summary_request import CommitCoverageSummaryRequest


class CodeCoverageApi:
    """
    Retrieve and analyze code coverage data from Code Coverage. See the `Code Coverage page <https://docs.datadoghq.com/code_coverage/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_code_coverage_branch_summary_endpoint = _Endpoint(
            settings={
                "response_type": (CoverageSummaryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/code-coverage/branch/summary",
                "operation_id": "get_code_coverage_branch_summary",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (BranchCoverageSummaryRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_code_coverage_commit_summary_endpoint = _Endpoint(
            settings={
                "response_type": (CoverageSummaryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/code-coverage/commit/summary",
                "operation_id": "get_code_coverage_commit_summary",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CommitCoverageSummaryRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def get_code_coverage_branch_summary(
        self,
        body: BranchCoverageSummaryRequest,
    ) -> CoverageSummaryResponse:
        """Get code coverage summary for a branch.

        Retrieve aggregated code coverage statistics for a specific branch in a repository.
        This endpoint provides overall coverage metrics as well as breakdowns by service
        and code owner.

        :type body: BranchCoverageSummaryRequest
        :rtype: CoverageSummaryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._get_code_coverage_branch_summary_endpoint.call_with_http_info(**kwargs)

    def get_code_coverage_commit_summary(
        self,
        body: CommitCoverageSummaryRequest,
    ) -> CoverageSummaryResponse:
        """Get code coverage summary for a commit.

        Retrieve aggregated code coverage statistics for a specific commit in a repository.
        This endpoint provides overall coverage metrics as well as breakdowns by service
        and code owner.

        The commit SHA must be a 40-character hexadecimal string (SHA-1 hash).

        :type body: CommitCoverageSummaryRequest
        :rtype: CoverageSummaryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._get_code_coverage_commit_summary_endpoint.call_with_http_info(**kwargs)
