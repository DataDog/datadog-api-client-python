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
    from datadog_api_client.v2.model.web_integration_account_create_request_attributes import (
        WebIntegrationAccountCreateRequestAttributes,
    )
    from datadog_api_client.v2.model.web_integration_account_type import WebIntegrationAccountType


class WebIntegrationAccountCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.web_integration_account_create_request_attributes import (
            WebIntegrationAccountCreateRequestAttributes,
        )
        from datadog_api_client.v2.model.web_integration_account_type import WebIntegrationAccountType

        return {
            "attributes": (WebIntegrationAccountCreateRequestAttributes,),
            "type": (WebIntegrationAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: WebIntegrationAccountCreateRequestAttributes, type: WebIntegrationAccountType, **kwargs
    ):
        """
        Data object for creating a web integration account.

        :param attributes: Attributes for creating a web integration account.
        :type attributes: WebIntegrationAccountCreateRequestAttributes

        :param type: The JSON:API type for web integration accounts.
        :type type: WebIntegrationAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
