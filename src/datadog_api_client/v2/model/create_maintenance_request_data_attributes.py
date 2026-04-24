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


class CreateMaintenanceRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_maintenance_request_data_attributes_components_affected_items import (
            CreateMaintenanceRequestDataAttributesComponentsAffectedItems,
        )

        return {
            "completed_date": (datetime,),
            "completed_description": (str,),
            "components_affected": ([CreateMaintenanceRequestDataAttributesComponentsAffectedItems],),
            "in_progress_description": (str,),
            "scheduled_description": (str,),
            "start_date": (datetime,),
            "title": (str,),
        }

    attribute_map = {
        "completed_date": "completed_date",
        "completed_description": "completed_description",
        "components_affected": "components_affected",
        "in_progress_description": "in_progress_description",
        "scheduled_description": "scheduled_description",
        "start_date": "start_date",
        "title": "title",
    }

    def __init__(
        self_,
        completed_date: datetime,
        completed_description: str,
        components_affected: List[CreateMaintenanceRequestDataAttributesComponentsAffectedItems],
        in_progress_description: str,
        scheduled_description: str,
        start_date: datetime,
        title: str,
        **kwargs,
    ):
        """
        The supported attributes for creating a maintenance.

        :param completed_date: Timestamp of when the maintenance was completed.
        :type completed_date: datetime

        :param completed_description: The description shown when the maintenance is completed.
        :type completed_description: str

        :param components_affected: The components affected by the maintenance.
        :type components_affected: [CreateMaintenanceRequestDataAttributesComponentsAffectedItems]

        :param in_progress_description: The description shown while the maintenance is in progress.
        :type in_progress_description: str

        :param scheduled_description: The description shown when the maintenance is scheduled.
        :type scheduled_description: str

        :param start_date: Timestamp of when the maintenance is scheduled to start.
        :type start_date: datetime

        :param title: The title of the maintenance.
        :type title: str
        """
        super().__init__(kwargs)

        self_.completed_date = completed_date
        self_.completed_description = completed_description
        self_.components_affected = components_affected
        self_.in_progress_description = in_progress_description
        self_.scheduled_description = scheduled_description
        self_.start_date = start_date
        self_.title = title
