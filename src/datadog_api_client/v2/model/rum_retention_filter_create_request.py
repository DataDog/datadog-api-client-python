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
    from datadog_api_client.v2.model.rum_retention_filter_create_data import RumRetentionFilterCreateData


class RumRetentionFilterCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_filter_create_data import RumRetentionFilterCreateData

        return {
            "data": (RumRetentionFilterCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RumRetentionFilterCreateData, **kwargs):
        """
        The RUM retention filter body to create.

        :param data: The new RUM retention filter properties to create.
        :type data: RumRetentionFilterCreateData
        """
        super().__init__(kwargs)

        self_.data = data
