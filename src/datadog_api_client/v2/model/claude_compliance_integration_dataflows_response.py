# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.claude_compliance_compliance_logs_integration_dataflow_response import (
        ClaudeComplianceComplianceLogsIntegrationDataflowResponse,
    )


class ClaudeComplianceIntegrationDataflowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.claude_compliance_compliance_logs_integration_dataflow_response import (
            ClaudeComplianceComplianceLogsIntegrationDataflowResponse,
        )

        return {
            "anthropic_compliance_logs": (ClaudeComplianceComplianceLogsIntegrationDataflowResponse,),
        }

    attribute_map = {
        "anthropic_compliance_logs": "anthropic-compliance-logs",
    }

    def __init__(
        self_,
        anthropic_compliance_logs: Union[ClaudeComplianceComplianceLogsIntegrationDataflowResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from Claude Compliance, keyed by dataflow ID.

        :param anthropic_compliance_logs: Audit activity logs from the Anthropic Compliance API, such as SSO sign-ins, API key lifecycle events, member and role changes, and Claude chat and file access. `Cloud SIEM <https://docs.datadoghq.com/security/cloud_siem/>`_ uses these logs to detect security-sensitive activity. Requires an Anthropic Enterprise plan with the Compliance API enabled in the organization's Data and privacy settings. Without it, this dataflow collects no data. This dataflow is always on and cannot be turned off, so it appears in responses only.
        :type anthropic_compliance_logs: ClaudeComplianceComplianceLogsIntegrationDataflowResponse, optional
        """
        if anthropic_compliance_logs is not unset:
            kwargs["anthropic_compliance_logs"] = anthropic_compliance_logs
        super().__init__(kwargs)
