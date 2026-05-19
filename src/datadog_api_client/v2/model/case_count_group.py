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
    from datadog_api_client.v2.model.case_count_group_value import CaseCountGroupValue


class CaseCountGroup(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_count_group_value import CaseCountGroupValue

        return {
            "group": (str,),
            "group_values": ([CaseCountGroupValue],),
        }

    attribute_map = {
        "group": "group",
        "group_values": "group_values",
    }

    def __init__(self_, group: str, group_values: List[CaseCountGroupValue], **kwargs):
        """
        A facet group containing counts broken down by the distinct values of a case field (for example, status or priority).

        :param group: The name of the field being grouped on (for example, ``status`` or ``priority`` ).
        :type group: str

        :param group_values: Values within this group.
        :type group_values: [CaseCountGroupValue]
        """
        super().__init__(kwargs)

        self_.group = group
        self_.group_values = group_values
