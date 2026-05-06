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
    from datadog_api_client.v2.model.create_backfilled_maintenance_request_data_attributes_updates_items import (
        CreateBackfilledMaintenanceRequestDataAttributesUpdatesItems,
    )


class CreateBackfilledMaintenanceRequestDataAttributes(ModelNormal):
    validations = {
        "updates": {
            "max_items": 2,
            "min_items": 2,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_backfilled_maintenance_request_data_attributes_updates_items import (
            CreateBackfilledMaintenanceRequestDataAttributesUpdatesItems,
        )

        return {
            "title": (str,),
            "updates": ([CreateBackfilledMaintenanceRequestDataAttributesUpdatesItems],),
        }

    attribute_map = {
        "title": "title",
        "updates": "updates",
    }

    def __init__(
        self_, title: str, updates: List[CreateBackfilledMaintenanceRequestDataAttributesUpdatesItems], **kwargs
    ):
        """
        The supported attributes for creating a backfilled maintenance.

        :param title: The title of the backfilled maintenance.
        :type title: str

        :param updates: The list of updates. Exactly two updates are required: the start ( ``in_progress`` ) and the end ( ``completed`` ).
        :type updates: [CreateBackfilledMaintenanceRequestDataAttributesUpdatesItems]
        """
        super().__init__(kwargs)

        self_.title = title
        self_.updates = updates
