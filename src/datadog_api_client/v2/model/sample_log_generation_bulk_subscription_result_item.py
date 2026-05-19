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
    from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_item_meta import (
        SampleLogGenerationBulkSubscriptionItemMeta,
    )
    from datadog_api_client.v2.model.sample_log_generation_subscription_resource_type import (
        SampleLogGenerationSubscriptionResourceType,
    )


class SampleLogGenerationBulkSubscriptionResultItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sample_log_generation_subscription_attributes import (
            SampleLogGenerationSubscriptionAttributes,
        )
        from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_item_meta import (
            SampleLogGenerationBulkSubscriptionItemMeta,
        )
        from datadog_api_client.v2.model.sample_log_generation_subscription_resource_type import (
            SampleLogGenerationSubscriptionResourceType,
        )

        return {
            "attributes": (SampleLogGenerationSubscriptionAttributes,),
            "id": (str,),
            "meta": (SampleLogGenerationBulkSubscriptionItemMeta,),
            "type": (SampleLogGenerationSubscriptionResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SampleLogGenerationSubscriptionAttributes,
        id: str,
        meta: SampleLogGenerationBulkSubscriptionItemMeta,
        type: SampleLogGenerationSubscriptionResourceType,
        **kwargs,
    ):
        """
        A single result entry returned by the bulk subscription endpoint.

        :param attributes: The attributes describing a sample log generation subscription.
        :type attributes: SampleLogGenerationSubscriptionAttributes

        :param id: The unique identifier of the subscription, when one was created.
        :type id: str

        :param meta: Per-item status returned for a bulk subscription request.
        :type meta: SampleLogGenerationBulkSubscriptionItemMeta

        :param type: The type of the resource. The value should always be ``subscriptions``.
        :type type: SampleLogGenerationSubscriptionResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.meta = meta
        self_.type = type
