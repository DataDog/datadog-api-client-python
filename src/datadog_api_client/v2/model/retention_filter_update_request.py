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
    from datadog_api_client.v2.model.retention_filter_update_data import RetentionFilterUpdateData


class RetentionFilterUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.retention_filter_update_data import RetentionFilterUpdateData

        return {
            "data": (RetentionFilterUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RetentionFilterUpdateData, **kwargs):
        """
        The body of the retention filter to be updated.

        :param data: The body of the retention filter to be updated.
        :type data: RetentionFilterUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
