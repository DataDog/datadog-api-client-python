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
    from datadog_api_client.v2.model.nebius_cloud_integration_account_create_data import (
        NebiusCloudIntegrationAccountCreateData,
    )


class NebiusCloudIntegrationAccountCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nebius_cloud_integration_account_create_data import (
            NebiusCloudIntegrationAccountCreateData,
        )

        return {
            "data": (NebiusCloudIntegrationAccountCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: NebiusCloudIntegrationAccountCreateData, **kwargs):
        """
        Request payload to create a Nebius Cloud integration account.

        :param data: Data envelope for creating a Nebius Cloud integration account.
        :type data: NebiusCloudIntegrationAccountCreateData
        """
        super().__init__(kwargs)

        self_.data = data
