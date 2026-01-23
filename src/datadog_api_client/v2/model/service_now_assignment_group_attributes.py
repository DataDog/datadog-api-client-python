# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class ServiceNowAssignmentGroupAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assignment_group_name": (str,),
            "assignment_group_sys_id": (str,),
            "instance_id": (UUID,),
        }

    attribute_map = {
        "assignment_group_name": "assignment_group_name",
        "assignment_group_sys_id": "assignment_group_sys_id",
        "instance_id": "instance_id",
    }

    def __init__(self_, assignment_group_name: str, assignment_group_sys_id: str, instance_id: UUID, **kwargs):
        """
        Attributes of a ServiceNow assignment group

        :param assignment_group_name: The name of the assignment group
        :type assignment_group_name: str

        :param assignment_group_sys_id: The system ID of the assignment group in ServiceNow
        :type assignment_group_sys_id: str

        :param instance_id: The ID of the ServiceNow instance
        :type instance_id: UUID
        """
        super().__init__(kwargs)

        self_.assignment_group_name = assignment_group_name
        self_.assignment_group_sys_id = assignment_group_sys_id
        self_.instance_id = instance_id
