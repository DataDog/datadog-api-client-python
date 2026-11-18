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
    from datadog_api_client.v2.model.nebius_cloud_integration_account_response_data import (
        NebiusCloudIntegrationAccountResponseData,
    )


class NebiusCloudIntegrationAccountResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nebius_cloud_integration_account_response_data import (
            NebiusCloudIntegrationAccountResponseData,
        )

        return {
            "data": (NebiusCloudIntegrationAccountResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: NebiusCloudIntegrationAccountResponseData, **kwargs):
        """
        Response payload for a single Nebius Cloud integration account.

        :param data: Data envelope of a Nebius Cloud integration account, including server-assigned identity.
        :type data: NebiusCloudIntegrationAccountResponseData
        """
        super().__init__(kwargs)

        self_.data = data
