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
    from datadog_api_client.v2.model.web_integration_account_response_attributes import (
        WebIntegrationAccountResponseAttributes,
    )
    from datadog_api_client.v2.model.web_integration_account_type import WebIntegrationAccountType


class WebIntegrationAccountResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.web_integration_account_response_attributes import (
            WebIntegrationAccountResponseAttributes,
        )
        from datadog_api_client.v2.model.web_integration_account_type import WebIntegrationAccountType

        return {
            "attributes": (WebIntegrationAccountResponseAttributes,),
            "id": (str,),
            "type": (WebIntegrationAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: WebIntegrationAccountResponseAttributes, id: str, type: WebIntegrationAccountType, **kwargs
    ):
        """
        Data object of a web integration account.

        :param attributes: Attributes object of a web integration account. Secrets are never returned.
        :type attributes: WebIntegrationAccountResponseAttributes

        :param id: The unique identifier of the web integration account.
        :type id: str

        :param type: Account resource type.
        :type type: WebIntegrationAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
