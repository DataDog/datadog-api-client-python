# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.elastic_cloud_integration_account_data import ElasticCloudIntegrationAccountData


class ElasticCloudIntegrationAccountResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_integration_account_data import (
            ElasticCloudIntegrationAccountData,
        )

        return {
            "data": (ElasticCloudIntegrationAccountData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[ElasticCloudIntegrationAccountData, UnsetType] = unset, **kwargs):
        """
        Response payload for a single Elastic Cloud integration account.

        :param data: Data envelope of an Elastic Cloud integration account, including server-assigned identity.
        :type data: ElasticCloudIntegrationAccountData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
