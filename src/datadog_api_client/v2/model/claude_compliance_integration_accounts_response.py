# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.claude_compliance_integration_account_response_data import (
        ClaudeComplianceIntegrationAccountResponseData,
    )


class ClaudeComplianceIntegrationAccountsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.claude_compliance_integration_account_response_data import (
            ClaudeComplianceIntegrationAccountResponseData,
        )

        return {
            "data": ([ClaudeComplianceIntegrationAccountResponseData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[ClaudeComplianceIntegrationAccountResponseData], **kwargs):
        """
        Response payload for a list of Claude Compliance integration accounts.

        :param data: List of Claude Compliance integration accounts.
        :type data: [ClaudeComplianceIntegrationAccountResponseData]
        """
        super().__init__(kwargs)

        self_.data = data
