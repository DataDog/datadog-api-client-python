# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_maintenance_request_data_attributes_updates_items_components_affected_items import (
        CreateMaintenanceRequestDataAttributesUpdatesItemsComponentsAffectedItems,
    )
    from datadog_api_client.v2.model.create_maintenance_request_data_attributes_updates_items_status import (
        CreateMaintenanceRequestDataAttributesUpdatesItemsStatus,
    )


class CreateMaintenanceRequestDataAttributesUpdatesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_maintenance_request_data_attributes_updates_items_components_affected_items import (
            CreateMaintenanceRequestDataAttributesUpdatesItemsComponentsAffectedItems,
        )
        from datadog_api_client.v2.model.create_maintenance_request_data_attributes_updates_items_status import (
            CreateMaintenanceRequestDataAttributesUpdatesItemsStatus,
        )

        return {
            "components_affected": ([CreateMaintenanceRequestDataAttributesUpdatesItemsComponentsAffectedItems],),
            "description": (str,),
            "started_at": (datetime,),
            "status": (CreateMaintenanceRequestDataAttributesUpdatesItemsStatus,),
        }

    attribute_map = {
        "components_affected": "components_affected",
        "description": "description",
        "started_at": "started_at",
        "status": "status",
    }

    def __init__(
        self_,
        components_affected: List[CreateMaintenanceRequestDataAttributesUpdatesItemsComponentsAffectedItems],
        description: str,
        started_at: datetime,
        status: CreateMaintenanceRequestDataAttributesUpdatesItemsStatus,
        **kwargs,
    ):
        """
        A maintenance update entry.

        :param components_affected: The components affected.
        :type components_affected: [CreateMaintenanceRequestDataAttributesUpdatesItemsComponentsAffectedItems]

        :param description: A description of the update.
        :type description: str

        :param started_at: Timestamp of when the update occurred.
        :type started_at: datetime

        :param status: The status of a maintenance update.
        :type status: CreateMaintenanceRequestDataAttributesUpdatesItemsStatus
        """
        super().__init__(kwargs)

        self_.components_affected = components_affected
        self_.description = description
        self_.started_at = started_at
        self_.status = status
