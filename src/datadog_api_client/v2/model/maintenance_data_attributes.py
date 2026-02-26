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
    from datadog_api_client.v2.model.maintenance_data_attributes_components_affected_items import (
        MaintenanceDataAttributesComponentsAffectedItems,
    )
    from datadog_api_client.v2.model.maintenance_data_attributes_status import MaintenanceDataAttributesStatus
    from datadog_api_client.v2.model.maintenance_data_attributes_updates_items import (
        MaintenanceDataAttributesUpdatesItems,
    )


class MaintenanceDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.maintenance_data_attributes_components_affected_items import (
            MaintenanceDataAttributesComponentsAffectedItems,
        )
        from datadog_api_client.v2.model.maintenance_data_attributes_status import MaintenanceDataAttributesStatus
        from datadog_api_client.v2.model.maintenance_data_attributes_updates_items import (
            MaintenanceDataAttributesUpdatesItems,
        )

        return {
            "completed_date": (datetime,),
            "completed_description": (str,),
            "components_affected": ([MaintenanceDataAttributesComponentsAffectedItems],),
            "in_progress_description": (str,),
            "modified_at": (datetime,),
            "published_date": (datetime,),
            "scheduled_description": (str,),
            "start_date": (datetime,),
            "status": (MaintenanceDataAttributesStatus,),
            "title": (str,),
            "updates": ([MaintenanceDataAttributesUpdatesItems],),
        }

    attribute_map = {
        "completed_date": "completed_date",
        "completed_description": "completed_description",
        "components_affected": "components_affected",
        "in_progress_description": "in_progress_description",
        "modified_at": "modified_at",
        "published_date": "published_date",
        "scheduled_description": "scheduled_description",
        "start_date": "start_date",
        "status": "status",
        "title": "title",
        "updates": "updates",
    }

    def __init__(
        self_,
        completed_date: Union[datetime, UnsetType] = unset,
        completed_description: Union[str, UnsetType] = unset,
        components_affected: Union[List[MaintenanceDataAttributesComponentsAffectedItems], UnsetType] = unset,
        in_progress_description: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        published_date: Union[datetime, UnsetType] = unset,
        scheduled_description: Union[str, UnsetType] = unset,
        start_date: Union[datetime, UnsetType] = unset,
        status: Union[MaintenanceDataAttributesStatus, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        updates: Union[List[MaintenanceDataAttributesUpdatesItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a maintenance.

        :param completed_date: Timestamp of when the maintenance was completed.
        :type completed_date: datetime, optional

        :param completed_description: The description shown when the maintenance is completed.
        :type completed_description: str, optional

        :param components_affected: Components affected by the maintenance.
        :type components_affected: [MaintenanceDataAttributesComponentsAffectedItems], optional

        :param in_progress_description: The description shown while the maintenance is in progress.
        :type in_progress_description: str, optional

        :param modified_at: Timestamp of when the maintenance was last modified.
        :type modified_at: datetime, optional

        :param published_date: Timestamp of when the maintenance was published.
        :type published_date: datetime, optional

        :param scheduled_description: The description shown when the maintenance is scheduled.
        :type scheduled_description: str, optional

        :param start_date: Timestamp of when the maintenance is scheduled to start.
        :type start_date: datetime, optional

        :param status: The status of the maintenance.
        :type status: MaintenanceDataAttributesStatus, optional

        :param title: Title of the maintenance.
        :type title: str, optional

        :param updates: Past updates made to the maintenance.
        :type updates: [MaintenanceDataAttributesUpdatesItems], optional
        """
        if completed_date is not unset:
            kwargs["completed_date"] = completed_date
        if completed_description is not unset:
            kwargs["completed_description"] = completed_description
        if components_affected is not unset:
            kwargs["components_affected"] = components_affected
        if in_progress_description is not unset:
            kwargs["in_progress_description"] = in_progress_description
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if published_date is not unset:
            kwargs["published_date"] = published_date
        if scheduled_description is not unset:
            kwargs["scheduled_description"] = scheduled_description
        if start_date is not unset:
            kwargs["start_date"] = start_date
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        if updates is not unset:
            kwargs["updates"] = updates
        super().__init__(kwargs)
