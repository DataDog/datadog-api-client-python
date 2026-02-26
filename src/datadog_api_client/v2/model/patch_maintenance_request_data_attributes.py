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
    from datadog_api_client.v2.model.patch_maintenance_request_data_attributes_components_affected_items import (
        PatchMaintenanceRequestDataAttributesComponentsAffectedItems,
    )
    from datadog_api_client.v2.model.maintenance_data_attributes_status import MaintenanceDataAttributesStatus


class PatchMaintenanceRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_maintenance_request_data_attributes_components_affected_items import (
            PatchMaintenanceRequestDataAttributesComponentsAffectedItems,
        )
        from datadog_api_client.v2.model.maintenance_data_attributes_status import MaintenanceDataAttributesStatus

        return {
            "completed_date": (datetime,),
            "completed_description": (str,),
            "components_affected": ([PatchMaintenanceRequestDataAttributesComponentsAffectedItems],),
            "in_progress_description": (str,),
            "scheduled_description": (str,),
            "start_date": (datetime,),
            "status": (MaintenanceDataAttributesStatus,),
            "title": (str,),
        }

    attribute_map = {
        "completed_date": "completed_date",
        "completed_description": "completed_description",
        "components_affected": "components_affected",
        "in_progress_description": "in_progress_description",
        "scheduled_description": "scheduled_description",
        "start_date": "start_date",
        "status": "status",
        "title": "title",
    }

    def __init__(
        self_,
        completed_date: Union[datetime, UnsetType] = unset,
        completed_description: Union[str, UnsetType] = unset,
        components_affected: Union[
            List[PatchMaintenanceRequestDataAttributesComponentsAffectedItems], UnsetType
        ] = unset,
        in_progress_description: Union[str, UnsetType] = unset,
        scheduled_description: Union[str, UnsetType] = unset,
        start_date: Union[datetime, UnsetType] = unset,
        status: Union[MaintenanceDataAttributesStatus, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The supported attributes for updating a maintenance.

        :param completed_date: Timestamp of when the maintenance was completed.
        :type completed_date: datetime, optional

        :param completed_description: The description shown when the maintenance is completed.
        :type completed_description: str, optional

        :param components_affected: The components affected by the maintenance.
        :type components_affected: [PatchMaintenanceRequestDataAttributesComponentsAffectedItems], optional

        :param in_progress_description: The description shown while the maintenance is in progress.
        :type in_progress_description: str, optional

        :param scheduled_description: The description shown when the maintenance is scheduled.
        :type scheduled_description: str, optional

        :param start_date: Timestamp of when the maintenance is scheduled to start.
        :type start_date: datetime, optional

        :param status: The status of the maintenance.
        :type status: MaintenanceDataAttributesStatus, optional

        :param title: The title of the maintenance.
        :type title: str, optional
        """
        if completed_date is not unset:
            kwargs["completed_date"] = completed_date
        if completed_description is not unset:
            kwargs["completed_description"] = completed_description
        if components_affected is not unset:
            kwargs["components_affected"] = components_affected
        if in_progress_description is not unset:
            kwargs["in_progress_description"] = in_progress_description
        if scheduled_description is not unset:
            kwargs["scheduled_description"] = scheduled_description
        if start_date is not unset:
            kwargs["start_date"] = start_date
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
