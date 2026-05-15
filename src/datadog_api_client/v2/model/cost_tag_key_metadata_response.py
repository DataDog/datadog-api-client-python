# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cost_tag_key_metadata import CostTagKeyMetadata


class CostTagKeyMetadataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_tag_key_metadata import CostTagKeyMetadata

        return {
            "data": ([CostTagKeyMetadata],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[CostTagKeyMetadata], **kwargs):
        """
        List of Cloud Cost Management tag key metadata entries for the requested period.

        :param data: List of tag key metadata entries.
        :type data: [CostTagKeyMetadata]
        """
        super().__init__(kwargs)

        self_.data = data
