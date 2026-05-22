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
    from datadog_api_client.v2.model.sample_log_generation_subscription_create_data import (
        SampleLogGenerationSubscriptionCreateData,
    )


class SampleLogGenerationSubscriptionCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sample_log_generation_subscription_create_data import (
            SampleLogGenerationSubscriptionCreateData,
        )

        return {
            "data": (SampleLogGenerationSubscriptionCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SampleLogGenerationSubscriptionCreateData, **kwargs):
        """
        Request body to create a sample log generation subscription for a single content pack.

        :param data: The subscription request body.
        :type data: SampleLogGenerationSubscriptionCreateData
        """
        super().__init__(kwargs)

        self_.data = data
