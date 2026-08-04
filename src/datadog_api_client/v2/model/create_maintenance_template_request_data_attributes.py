# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CreateMaintenanceTemplateRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "completed_description": (str,),
            "component_ids": ([str],),
            "in_progress_description": (str,),
            "maintenance_title": (str,),
            "name": (str,),
            "scheduled_description": (str,),
        }

    attribute_map = {
        "completed_description": "completed_description",
        "component_ids": "component_ids",
        "in_progress_description": "in_progress_description",
        "maintenance_title": "maintenance_title",
        "name": "name",
        "scheduled_description": "scheduled_description",
    }

    def __init__(
        self_,
        name: str,
        completed_description: Union[str, UnsetType] = unset,
        component_ids: Union[List[str], UnsetType] = unset,
        in_progress_description: Union[str, UnsetType] = unset,
        maintenance_title: Union[str, UnsetType] = unset,
        scheduled_description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes for creating a maintenance template.

        :param completed_description: The description shown when a maintenance created from this template is completed.
        :type completed_description: str, optional

        :param component_ids: The IDs of the components affected by a maintenance created from this template.
        :type component_ids: [str], optional

        :param in_progress_description: The description shown while a maintenance created from this template is in progress.
        :type in_progress_description: str, optional

        :param maintenance_title: The title used for a maintenance created from this template.
        :type maintenance_title: str, optional

        :param name: The name of the maintenance template.
        :type name: str

        :param scheduled_description: The description shown when a maintenance created from this template is scheduled.
        :type scheduled_description: str, optional
        """
        if completed_description is not unset:
            kwargs["completed_description"] = completed_description
        if component_ids is not unset:
            kwargs["component_ids"] = component_ids
        if in_progress_description is not unset:
            kwargs["in_progress_description"] = in_progress_description
        if maintenance_title is not unset:
            kwargs["maintenance_title"] = maintenance_title
        if scheduled_description is not unset:
            kwargs["scheduled_description"] = scheduled_description
        super().__init__(kwargs)

        self_.name = name
