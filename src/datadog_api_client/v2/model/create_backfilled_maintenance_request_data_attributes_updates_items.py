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
    from datadog_api_client.v2.model.create_maintenance_request_data_attributes_components_affected_items import (
        CreateMaintenanceRequestDataAttributesComponentsAffectedItems,
    )
    from datadog_api_client.v2.model.create_backfilled_maintenance_request_data_attributes_updates_items_status import (
        CreateBackfilledMaintenanceRequestDataAttributesUpdatesItemsStatus,
    )


class CreateBackfilledMaintenanceRequestDataAttributesUpdatesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_maintenance_request_data_attributes_components_affected_items import (
            CreateMaintenanceRequestDataAttributesComponentsAffectedItems,
        )
        from datadog_api_client.v2.model.create_backfilled_maintenance_request_data_attributes_updates_items_status import (
            CreateBackfilledMaintenanceRequestDataAttributesUpdatesItemsStatus,
        )

        return {
            "components_affected": ([CreateMaintenanceRequestDataAttributesComponentsAffectedItems],),
            "description": (str,),
            "started_at": (datetime,),
            "status": (CreateBackfilledMaintenanceRequestDataAttributesUpdatesItemsStatus,),
        }

    attribute_map = {
        "components_affected": "components_affected",
        "description": "description",
        "started_at": "started_at",
        "status": "status",
    }

    def __init__(
        self_,
        components_affected: List[CreateMaintenanceRequestDataAttributesComponentsAffectedItems],
        description: str,
        started_at: datetime,
        status: CreateBackfilledMaintenanceRequestDataAttributesUpdatesItemsStatus,
        **kwargs,
    ):
        """
        A backfilled maintenance update entry.

        :param components_affected: The components affected.
        :type components_affected: [CreateMaintenanceRequestDataAttributesComponentsAffectedItems]

        :param description: A description of the update.
        :type description: str

        :param started_at: Timestamp of when the update occurred.
        :type started_at: datetime

        :param status: The status of a backfilled maintenance update.
        :type status: CreateBackfilledMaintenanceRequestDataAttributesUpdatesItemsStatus
        """
        super().__init__(kwargs)

        self_.components_affected = components_affected
        self_.description = description
        self_.started_at = started_at
        self_.status = status
