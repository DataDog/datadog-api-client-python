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
    from datadog_api_client.v2.model.rum_permanent_retention_filter_update_data import (
        RumPermanentRetentionFilterUpdateData,
    )


class RumPermanentRetentionFilterUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_permanent_retention_filter_update_data import (
            RumPermanentRetentionFilterUpdateData,
        )

        return {
            "data": (RumPermanentRetentionFilterUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RumPermanentRetentionFilterUpdateData, **kwargs):
        """
        The permanent retention filter body to update.

        :param data: The permanent retention filter properties to update.
        :type data: RumPermanentRetentionFilterUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
