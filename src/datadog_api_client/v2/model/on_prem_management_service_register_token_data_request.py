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
    from datadog_api_client.v2.model.on_prem_management_service_register_token_attributes import (
        OnPremManagementServiceRegisterTokenAttributes,
    )
    from datadog_api_client.v2.model.on_prem_management_service_register_token_type import (
        OnPremManagementServiceRegisterTokenType,
    )


class OnPremManagementServiceRegisterTokenDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_prem_management_service_register_token_attributes import (
            OnPremManagementServiceRegisterTokenAttributes,
        )
        from datadog_api_client.v2.model.on_prem_management_service_register_token_type import (
            OnPremManagementServiceRegisterTokenType,
        )

        return {
            "attributes": (OnPremManagementServiceRegisterTokenAttributes,),
            "type": (OnPremManagementServiceRegisterTokenType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OnPremManagementServiceRegisterTokenAttributes,
        type: OnPremManagementServiceRegisterTokenType,
        **kwargs,
    ):
        """
        Data for registering a token.

        :param attributes: Attributes for registering a token.
        :type attributes: OnPremManagementServiceRegisterTokenAttributes

        :param type: The type of the resource. The value should always be registerTokenRequest.
        :type type: OnPremManagementServiceRegisterTokenType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
