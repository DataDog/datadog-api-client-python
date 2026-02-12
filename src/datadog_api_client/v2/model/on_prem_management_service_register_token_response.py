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
    from datadog_api_client.v2.model.on_prem_management_service_register_token_response_data import (
        OnPremManagementServiceRegisterTokenResponseData,
    )


class OnPremManagementServiceRegisterTokenResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_prem_management_service_register_token_response_data import (
            OnPremManagementServiceRegisterTokenResponseData,
        )

        return {
            "data": (OnPremManagementServiceRegisterTokenResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OnPremManagementServiceRegisterTokenResponseData, **kwargs):
        """
        Response for registering a token.

        :param data: Data for the registered token.
        :type data: OnPremManagementServiceRegisterTokenResponseData
        """
        super().__init__(kwargs)

        self_.data = data
