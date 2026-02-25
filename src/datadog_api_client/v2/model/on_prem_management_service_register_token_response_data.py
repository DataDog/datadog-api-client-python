# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.on_prem_management_service_register_token_response_attributes import (
        OnPremManagementServiceRegisterTokenResponseAttributes,
    )
    from datadog_api_client.v2.model.on_prem_management_service_register_token_response_type import (
        OnPremManagementServiceRegisterTokenResponseType,
    )


class OnPremManagementServiceRegisterTokenResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_prem_management_service_register_token_response_attributes import (
            OnPremManagementServiceRegisterTokenResponseAttributes,
        )
        from datadog_api_client.v2.model.on_prem_management_service_register_token_response_type import (
            OnPremManagementServiceRegisterTokenResponseType,
        )

        return {
            "attributes": (OnPremManagementServiceRegisterTokenResponseAttributes,),
            "id": (UUID,),
            "type": (OnPremManagementServiceRegisterTokenResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OnPremManagementServiceRegisterTokenResponseAttributes,
        id: UUID,
        type: OnPremManagementServiceRegisterTokenResponseType,
        **kwargs,
    ):
        """
        Data for the registered token.

        :param attributes: Attributes for the registered token.
        :type attributes: OnPremManagementServiceRegisterTokenResponseAttributes

        :param id: The token identifier.
        :type id: UUID

        :param type: The type of the resource. The value should always be tokenDefinitions.
        :type type: OnPremManagementServiceRegisterTokenResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
