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
    from datadog_api_client.v2.model.core_weave_cloud_integration_account_create_data import (
        CoreWeaveCloudIntegrationAccountCreateData,
    )


class CoreWeaveCloudIntegrationAccountCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.core_weave_cloud_integration_account_create_data import (
            CoreWeaveCloudIntegrationAccountCreateData,
        )

        return {
            "data": (CoreWeaveCloudIntegrationAccountCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CoreWeaveCloudIntegrationAccountCreateData, **kwargs):
        """
        Request payload to create a CoreWeave integration account.

        :param data: Data envelope for creating a CoreWeave integration account.
        :type data: CoreWeaveCloudIntegrationAccountCreateData
        """
        super().__init__(kwargs)

        self_.data = data
