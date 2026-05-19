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
    from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_result_item import (
        SampleLogGenerationBulkSubscriptionResultItem,
    )


class SampleLogGenerationBulkSubscriptionResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_result_item import (
            SampleLogGenerationBulkSubscriptionResultItem,
        )

        return {
            "data": ([SampleLogGenerationBulkSubscriptionResultItem],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[SampleLogGenerationBulkSubscriptionResultItem], **kwargs):
        """
        Response containing the per-content-pack results of a bulk subscription request.

        :param data: The list of bulk subscription results, one per requested content pack.
        :type data: [SampleLogGenerationBulkSubscriptionResultItem]
        """
        super().__init__(kwargs)

        self_.data = data
