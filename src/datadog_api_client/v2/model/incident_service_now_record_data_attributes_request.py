# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IncidentServiceNowRecordDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assignment_group": (str,),
            "configuration_item_mapping": (str,),
            "instance_name": (str,),
            "record_id": (str,),
        }

    attribute_map = {
        "assignment_group": "assignment_group",
        "configuration_item_mapping": "configuration_item_mapping",
        "instance_name": "instance_name",
        "record_id": "record_id",
    }

    def __init__(
        self_,
        assignment_group: str,
        configuration_item_mapping: str,
        instance_name: str,
        record_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a ServiceNow record for an incident.

        :param assignment_group: The ServiceNow assignment group.
        :type assignment_group: str

        :param configuration_item_mapping: The ServiceNow configuration item mapping.
        :type configuration_item_mapping: str

        :param instance_name: The ServiceNow instance name.
        :type instance_name: str

        :param record_id: An existing ServiceNow record ID (Sys ID) to link instead of creating a new record.
        :type record_id: str, optional
        """
        if record_id is not unset:
            kwargs["record_id"] = record_id
        super().__init__(kwargs)

        self_.assignment_group = assignment_group
        self_.configuration_item_mapping = configuration_item_mapping
        self_.instance_name = instance_name
