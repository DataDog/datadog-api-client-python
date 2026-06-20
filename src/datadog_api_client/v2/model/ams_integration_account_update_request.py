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
    from datadog_api_client.v2.model.ams_integration_account_update_request_data import (
        AmsIntegrationAccountUpdateRequestData,
    )


class AmsIntegrationAccountUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ams_integration_account_update_request_data import (
            AmsIntegrationAccountUpdateRequestData,
        )

        return {
            "data": (AmsIntegrationAccountUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AmsIntegrationAccountUpdateRequestData, **kwargs):
        """
        Payload for updating a web integration account.

        :param data: Data object for updating a web integration account.
        :type data: AmsIntegrationAccountUpdateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
