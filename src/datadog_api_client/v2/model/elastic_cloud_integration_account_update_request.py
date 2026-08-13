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
    from datadog_api_client.v2.model.elastic_cloud_integration_account_update_data import (
        ElasticCloudIntegrationAccountUpdateData,
    )


class ElasticCloudIntegrationAccountUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_integration_account_update_data import (
            ElasticCloudIntegrationAccountUpdateData,
        )

        return {
            "data": (ElasticCloudIntegrationAccountUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ElasticCloudIntegrationAccountUpdateData, **kwargs):
        """
        Request payload to update an Elastic Cloud integration account as a partial merge.

        :param data: Data envelope for updating an Elastic Cloud integration account.
        :type data: ElasticCloudIntegrationAccountUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
