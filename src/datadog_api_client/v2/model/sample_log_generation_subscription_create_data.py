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
    from datadog_api_client.v2.model.sample_log_generation_subscription_create_attributes import (
        SampleLogGenerationSubscriptionCreateAttributes,
    )
    from datadog_api_client.v2.model.sample_log_generation_subscription_request_type import (
        SampleLogGenerationSubscriptionRequestType,
    )


class SampleLogGenerationSubscriptionCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sample_log_generation_subscription_create_attributes import (
            SampleLogGenerationSubscriptionCreateAttributes,
        )
        from datadog_api_client.v2.model.sample_log_generation_subscription_request_type import (
            SampleLogGenerationSubscriptionRequestType,
        )

        return {
            "attributes": (SampleLogGenerationSubscriptionCreateAttributes,),
            "type": (SampleLogGenerationSubscriptionRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SampleLogGenerationSubscriptionCreateAttributes,
        type: SampleLogGenerationSubscriptionRequestType,
        **kwargs,
    ):
        """
        The subscription request body.

        :param attributes: The attributes for creating a sample log generation subscription.
        :type attributes: SampleLogGenerationSubscriptionCreateAttributes

        :param type: The type of the resource. The value should always be ``subscription_requests``.
        :type type: SampleLogGenerationSubscriptionRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
