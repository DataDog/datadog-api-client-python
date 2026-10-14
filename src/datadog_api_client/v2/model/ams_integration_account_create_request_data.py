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
    from datadog_api_client.v2.model.ams_integration_account_create_request_attributes import (
        AmsIntegrationAccountCreateRequestAttributes,
    )
    from datadog_api_client.v2.model.ams_integration_account_type import AmsIntegrationAccountType


class AmsIntegrationAccountCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ams_integration_account_create_request_attributes import (
            AmsIntegrationAccountCreateRequestAttributes,
        )
        from datadog_api_client.v2.model.ams_integration_account_type import AmsIntegrationAccountType

        return {
            "attributes": (AmsIntegrationAccountCreateRequestAttributes,),
            "type": (AmsIntegrationAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: AmsIntegrationAccountCreateRequestAttributes, type: AmsIntegrationAccountType, **kwargs
    ):
        """
        Data object for creating a web integration account.

        :param attributes: Attributes for creating a web integration account.
        :type attributes: AmsIntegrationAccountCreateRequestAttributes

        :param type: The JSON:API type for web integration accounts.
        :type type: AmsIntegrationAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
