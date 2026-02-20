# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
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
        components_affected: List[CreateMaintenanceRequestDataAttributesComponentsAffectedItems],
        title: str,
        completed_date: Union[datetime, UnsetType] = unset,
        completed_description: Union[str, UnsetType] = unset,
        in_progress_description: Union[str, UnsetType] = unset,
        scheduled_description: Union[str, UnsetType] = unset,
        start_date: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        The supported attributes for creating a maintenance.

        :param completed_date: Timestamp of when the maintenance was completed.
        :type completed_date: datetime, optional

        :param completed_description: The description shown when the maintenance is completed.
        :type completed_description: str, optional

        :param components_affected: The components affected by the maintenance.
        :type components_affected: [CreateMaintenanceRequestDataAttributesComponentsAffectedItems]

        :param in_progress_description: The description shown while the maintenance is in progress.
        :type in_progress_description: str, optional

        :param scheduled_description: The description shown when the maintenance is scheduled.
        :type scheduled_description: str, optional

        :param start_date: Timestamp of when the maintenance is scheduled to start.
        :type start_date: datetime, optional

        :param title: The title of the maintenance.
        :type title: str
        """
        if completed_date is not unset:
            kwargs["completed_date"] = completed_date
        if completed_description is not unset:
            kwargs["completed_description"] = completed_description
        if in_progress_description is not unset:
            kwargs["in_progress_description"] = in_progress_description
        if scheduled_description is not unset:
            kwargs["scheduled_description"] = scheduled_description
        if start_date is not unset:
            kwargs["start_date"] = start_date
        super().__init__(kwargs)

        self_.components_affected = components_affected
        self_.title = title
