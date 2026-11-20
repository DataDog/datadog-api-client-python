# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.claude_compliance_integration_account_update_attributes import (
        ClaudeComplianceIntegrationAccountUpdateAttributes,
    )
    from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType


class ClaudeComplianceIntegrationAccountUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.claude_compliance_integration_account_update_attributes import (
            ClaudeComplianceIntegrationAccountUpdateAttributes,
        )
        from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

        return {
            "attributes": (ClaudeComplianceIntegrationAccountUpdateAttributes,),
            "id": (str,),
            "type": (IntegrationAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ClaudeComplianceIntegrationAccountUpdateAttributes,
        id: str,
        type: IntegrationAccountType,
        **kwargs,
    ):
        """
        Data envelope for updating a Claude Compliance integration account.

        :param attributes: Writable attributes used to update a Claude Compliance integration account. Every field is optional. Only the provided fields are changed.
        :type attributes: ClaudeComplianceIntegrationAccountUpdateAttributes

        :param id: Unique identifier of the Claude Compliance integration account to update.
        :type id: str

        :param type: The type of the integration account resource. Always ``integration-account``.
        :type type: IntegrationAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
