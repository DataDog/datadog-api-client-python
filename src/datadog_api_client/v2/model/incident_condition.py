# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_tag_value import IncidentTagValue


class IncidentCondition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_tag_value import IncidentTagValue

        return {
            "tag_values": ([IncidentTagValue],),
        }

    attribute_map = {
        "tag_values": "tagValues",
    }

    def __init__(self_, tag_values: Union[List[IncidentTagValue], UnsetType] = unset, **kwargs):
        """
        Conditions that determine which incidents trigger the workflow.

        :param tag_values: Incident tags and values used to filter matching incidents.
        :type tag_values: [IncidentTagValue], optional
        """
        if tag_values is not unset:
            kwargs["tag_values"] = tag_values
        super().__init__(kwargs)
