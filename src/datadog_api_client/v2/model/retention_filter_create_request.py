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
    from datadog_api_client.v2.model.retention_filter_create_data import RetentionFilterCreateData


class RetentionFilterCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.retention_filter_create_data import RetentionFilterCreateData

        return {
            "data": (RetentionFilterCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RetentionFilterCreateData, **kwargs):
        """
        The body of the retention filter to be created.

        :param data: The body of the retention filter to be created.
        :type data: RetentionFilterCreateData
        """
        super().__init__(kwargs)

        self_.data = data
