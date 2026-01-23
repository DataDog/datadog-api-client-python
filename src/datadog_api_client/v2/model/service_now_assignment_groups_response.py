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
    from datadog_api_client.v2.model.service_now_assignment_group_data import ServiceNowAssignmentGroupData


class ServiceNowAssignmentGroupsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_now_assignment_group_data import ServiceNowAssignmentGroupData

        return {
            "data": ([ServiceNowAssignmentGroupData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[ServiceNowAssignmentGroupData], **kwargs):
        """
        Response containing ServiceNow assignment groups

        :param data: Array of ServiceNow assignment group data objects
        :type data: [ServiceNowAssignmentGroupData]
        """
        super().__init__(kwargs)

        self_.data = data
