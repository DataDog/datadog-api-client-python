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
    from datadog_api_client.v2.model.rum_retention_quota_config_update_data import RumRetentionQuotaConfigUpdateData


class RumRetentionQuotaConfigUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_quota_config_update_data import RumRetentionQuotaConfigUpdateData

        return {
            "data": (RumRetentionQuotaConfigUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RumRetentionQuotaConfigUpdateData, **kwargs):
        """
        The body of a request to create or update a RUM retention quota configuration.

        :param data: The RUM retention quota configuration to create or update.
        :type data: RumRetentionQuotaConfigUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
