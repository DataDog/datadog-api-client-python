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
    from datadog_api_client.v2.model.git_hub_costs_integration_account_update_attributes import (
        GitHubCostsIntegrationAccountUpdateAttributes,
    )
    from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType


class GitHubCostsIntegrationAccountUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.git_hub_costs_integration_account_update_attributes import (
            GitHubCostsIntegrationAccountUpdateAttributes,
        )
        from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

        return {
            "attributes": (GitHubCostsIntegrationAccountUpdateAttributes,),
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
        attributes: GitHubCostsIntegrationAccountUpdateAttributes,
        id: str,
        type: IntegrationAccountType,
        **kwargs,
    ):
        """
        Data envelope for updating a GitHub Costs integration account.

        :param attributes: Writable attributes used to update a GitHub Costs integration account. Every field is optional; only the fields provided are changed.
        :type attributes: GitHubCostsIntegrationAccountUpdateAttributes

        :param id: Unique identifier of the GitHub Costs integration account to update.
        :type id: str

        :param type: The type of the integration account resource. Always ``integration-account``.
        :type type: IntegrationAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
