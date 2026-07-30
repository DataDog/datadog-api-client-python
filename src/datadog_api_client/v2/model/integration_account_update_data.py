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
    from datadog_api_client.v2.model.integration_account_update_attributes import IntegrationAccountUpdateAttributes
    from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType


class IntegrationAccountUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_account_update_attributes import IntegrationAccountUpdateAttributes
        from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

        return {
            "attributes": (IntegrationAccountUpdateAttributes,),
            "type": (IntegrationAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: IntegrationAccountUpdateAttributes, type: IntegrationAccountType, **kwargs):
        """
        Data envelope for updating an integration account.

        :param attributes: Updatable attributes of an integration account. Every field is optional; only the fields provided are changed.
        :type attributes: IntegrationAccountUpdateAttributes

        :param type: JSON:API resource type for an integration account. Always ``integration-account``.
        :type type: IntegrationAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
