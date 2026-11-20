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
    from datadog_api_client.v2.model.integration_account_dataflow_status import IntegrationAccountDataflowStatus


class ClaudeComplianceComplianceLogsIntegrationDataflowResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_account_dataflow_status import IntegrationAccountDataflowStatus

        return {
            "enabled": (bool,),
            "status": (IntegrationAccountDataflowStatus,),
        }

    attribute_map = {
        "enabled": "enabled",
        "status": "status",
    }
    read_only_vars = {
        "enabled",
        "status",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        status: Union[IntegrationAccountDataflowStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        Audit activity logs from the Anthropic Compliance API, such as SSO sign-ins, API key lifecycle events, member and role changes, and Claude chat and file access. `Cloud SIEM <https://docs.datadoghq.com/security/cloud_siem/>`_ uses these logs to detect security-sensitive activity. Requires an Anthropic Enterprise plan with the Compliance API enabled in the organization's Data and privacy settings. Without it, this dataflow collects no data. This dataflow is always on and cannot be turned off, so it appears in responses only.

        :param enabled: Whether Datadog collects this data. Always ``true`` , because this collection cannot be turned off.
        :type enabled: bool, optional

        :param status: Read-only collection status of a dataflow.
        :type status: IntegrationAccountDataflowStatus, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
