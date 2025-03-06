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
    from datadog_api_client.v2.model.rum_retention_filter_update_data import RumRetentionFilterUpdateData


class RumRetentionFilterUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_filter_update_data import RumRetentionFilterUpdateData

        return {
            "data": (RumRetentionFilterUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RumRetentionFilterUpdateData, **kwargs):
        """
        The RUM retention filter body to update.

        :param data: The new RUM retention filter properties to update.
        :type data: RumRetentionFilterUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
