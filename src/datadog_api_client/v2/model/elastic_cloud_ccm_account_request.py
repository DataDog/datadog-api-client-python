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
    from datadog_api_client.v2.model.elastic_cloud_ccm_account_create_data import ElasticCloudCcmAccountCreateData


class ElasticCloudCcmAccountRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_ccm_account_create_data import ElasticCloudCcmAccountCreateData

        return {
            "data": (ElasticCloudCcmAccountCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ElasticCloudCcmAccountCreateData, **kwargs):
        """
        Request payload to create an Elastic Cloud CCM (Cloud Cost Management) account.

        :param data: Data envelope for creating an Elastic Cloud CCM account.
        :type data: ElasticCloudCcmAccountCreateData
        """
        super().__init__(kwargs)

        self_.data = data
