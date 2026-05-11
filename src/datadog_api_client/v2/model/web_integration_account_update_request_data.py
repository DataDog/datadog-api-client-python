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
    from datadog_api_client.v2.model.web_integration_account_update_request_attributes import (
        WebIntegrationAccountUpdateRequestAttributes,
    )
    from datadog_api_client.v2.model.web_integration_account_type import WebIntegrationAccountType


class WebIntegrationAccountUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.web_integration_account_update_request_attributes import (
            WebIntegrationAccountUpdateRequestAttributes,
        )
        from datadog_api_client.v2.model.web_integration_account_type import WebIntegrationAccountType

        return {
            "attributes": (WebIntegrationAccountUpdateRequestAttributes,),
            "type": (WebIntegrationAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: WebIntegrationAccountUpdateRequestAttributes, type: WebIntegrationAccountType, **kwargs
    ):
        """
        Data object for updating a web integration account.

        :param attributes: Attributes object for updating a web integration account.
        :type attributes: WebIntegrationAccountUpdateRequestAttributes

        :param type: Account resource type.
        :type type: WebIntegrationAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
