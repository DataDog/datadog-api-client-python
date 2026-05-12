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
    from datadog_api_client.v2.model.create_backfilled_degradation_request_data_attributes_updates_items import (
        CreateBackfilledDegradationRequestDataAttributesUpdatesItems,
    )


class CreateBackfilledDegradationRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_backfilled_degradation_request_data_attributes_updates_items import (
            CreateBackfilledDegradationRequestDataAttributesUpdatesItems,
        )

        return {
            "title": (str,),
            "updates": ([CreateBackfilledDegradationRequestDataAttributesUpdatesItems],),
        }

    attribute_map = {
        "title": "title",
        "updates": "updates",
    }

    def __init__(
        self_, title: str, updates: List[CreateBackfilledDegradationRequestDataAttributesUpdatesItems], **kwargs
    ):
        """
        The supported attributes for creating a backfilled degradation.

        :param title: The title of the backfilled degradation.
        :type title: str

        :param updates: The list of status updates describing the timeline of the degradation.
        :type updates: [CreateBackfilledDegradationRequestDataAttributesUpdatesItems]
        """
        super().__init__(kwargs)

        self_.title = title
        self_.updates = updates
