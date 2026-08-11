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
    from datadog_api_client.v2.model.elastic_cloud_ccm_account_update_data import ElasticCloudCcmAccountUpdateData


class ElasticCloudCcmAccountUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_ccm_account_update_data import ElasticCloudCcmAccountUpdateData

        return {
            "data": (ElasticCloudCcmAccountUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ElasticCloudCcmAccountUpdateData, **kwargs):
        """
        Request payload to update an Elastic Cloud CCM account as a partial merge.

        :param data: Data envelope for updating an Elastic Cloud CCM account.
        :type data: ElasticCloudCcmAccountUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
