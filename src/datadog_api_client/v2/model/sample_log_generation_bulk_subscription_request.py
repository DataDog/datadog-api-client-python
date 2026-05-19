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
    from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_data import (
        SampleLogGenerationBulkSubscriptionData,
    )


class SampleLogGenerationBulkSubscriptionRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_data import (
            SampleLogGenerationBulkSubscriptionData,
        )

        return {
            "data": (SampleLogGenerationBulkSubscriptionData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SampleLogGenerationBulkSubscriptionData, **kwargs):
        """
        Request body to create sample log generation subscriptions for multiple content packs at once.

        :param data: The bulk subscription request body.
        :type data: SampleLogGenerationBulkSubscriptionData
        """
        super().__init__(kwargs)

        self_.data = data
