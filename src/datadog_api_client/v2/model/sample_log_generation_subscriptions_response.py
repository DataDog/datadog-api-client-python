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
    from datadog_api_client.v2.model.sample_log_generation_subscription_data import SampleLogGenerationSubscriptionData
    from datadog_api_client.v2.model.sample_log_generation_subscriptions_response_meta import (
        SampleLogGenerationSubscriptionsResponseMeta,
    )


class SampleLogGenerationSubscriptionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sample_log_generation_subscription_data import (
            SampleLogGenerationSubscriptionData,
        )
        from datadog_api_client.v2.model.sample_log_generation_subscriptions_response_meta import (
            SampleLogGenerationSubscriptionsResponseMeta,
        )

        return {
            "data": ([SampleLogGenerationSubscriptionData],),
            "meta": (SampleLogGenerationSubscriptionsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[SampleLogGenerationSubscriptionData],
        meta: SampleLogGenerationSubscriptionsResponseMeta,
        **kwargs,
    ):
        """
        Response containing a list of sample log generation subscriptions.

        :param data: The list of sample log generation subscriptions.
        :type data: [SampleLogGenerationSubscriptionData]

        :param meta: Metadata returned alongside a list of sample log generation subscriptions.
        :type meta: SampleLogGenerationSubscriptionsResponseMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
