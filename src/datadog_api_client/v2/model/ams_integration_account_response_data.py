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
    from datadog_api_client.v2.model.ams_integration_account_attributes import AmsIntegrationAccountAttributes
    from datadog_api_client.v2.model.ams_integration_account_type import AmsIntegrationAccountType


class AmsIntegrationAccountResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ams_integration_account_attributes import AmsIntegrationAccountAttributes
        from datadog_api_client.v2.model.ams_integration_account_type import AmsIntegrationAccountType

        return {
            "attributes": (AmsIntegrationAccountAttributes,),
            "id": (str,),
            "type": (AmsIntegrationAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AmsIntegrationAccountAttributes, id: str, type: AmsIntegrationAccountType, **kwargs
    ):
        """
        Data object for a web integration account response.

        :param attributes: Attributes for a web integration account.
        :type attributes: AmsIntegrationAccountAttributes

        :param id: The unique identifier for the account.
        :type id: str

        :param type: The JSON:API type for web integration accounts.
        :type type: AmsIntegrationAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
