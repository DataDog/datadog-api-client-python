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
    from datadog_api_client.v2.model.sample_log_generation_subscription_attributes import (
        SampleLogGenerationSubscriptionAttributes,
    )
    from datadog_api_client.v2.model.sample_log_generation_subscription_resource_type import (
        SampleLogGenerationSubscriptionResourceType,
    )


class SampleLogGenerationSubscriptionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sample_log_generation_subscription_attributes import (
            SampleLogGenerationSubscriptionAttributes,
        )
        from datadog_api_client.v2.model.sample_log_generation_subscription_resource_type import (
            SampleLogGenerationSubscriptionResourceType,
        )

        return {
            "attributes": (SampleLogGenerationSubscriptionAttributes,),
            "id": (str,),
            "type": (SampleLogGenerationSubscriptionResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SampleLogGenerationSubscriptionAttributes,
        id: str,
        type: SampleLogGenerationSubscriptionResourceType,
        **kwargs,
    ):
        """
        A sample log generation subscription.

        :param attributes: The attributes describing a sample log generation subscription.
        :type attributes: SampleLogGenerationSubscriptionAttributes

        :param id: The unique identifier of the subscription.
        :type id: str

        :param type: The type of the resource. The value should always be ``subscriptions``.
        :type type: SampleLogGenerationSubscriptionResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
