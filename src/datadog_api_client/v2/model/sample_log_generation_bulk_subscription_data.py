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
    from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_attributes import (
        SampleLogGenerationBulkSubscriptionAttributes,
    )
    from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_request_type import (
        SampleLogGenerationBulkSubscriptionRequestType,
    )


class SampleLogGenerationBulkSubscriptionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_attributes import (
            SampleLogGenerationBulkSubscriptionAttributes,
        )
        from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_request_type import (
            SampleLogGenerationBulkSubscriptionRequestType,
        )

        return {
            "attributes": (SampleLogGenerationBulkSubscriptionAttributes,),
            "type": (SampleLogGenerationBulkSubscriptionRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SampleLogGenerationBulkSubscriptionAttributes,
        type: SampleLogGenerationBulkSubscriptionRequestType,
        **kwargs,
    ):
        """
        The bulk subscription request body.

        :param attributes: The attributes for creating sample log generation subscriptions for multiple content packs.
        :type attributes: SampleLogGenerationBulkSubscriptionAttributes

        :param type: The type of the resource. The value should always be ``bulk_subscription_requests``.
        :type type: SampleLogGenerationBulkSubscriptionRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
