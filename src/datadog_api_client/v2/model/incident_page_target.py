# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_page_target_type import IncidentPageTargetType


class IncidentPageTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_page_target_type import IncidentPageTargetType

        return {
            "identifier": (str,),
            "type": (IncidentPageTargetType,),
        }

    attribute_map = {
        "identifier": "identifier",
        "type": "type",
    }

    def __init__(self_, identifier: str, type: IncidentPageTargetType, **kwargs):
        """
        Target for creating a page from an incident.

        :param identifier: The identifier of the target (team handle, team UUID, or user UUID).
        :type identifier: str

        :param type: Type of page target for incident pages.
        :type type: IncidentPageTargetType
        """
        super().__init__(kwargs)

        self_.identifier = identifier
        self_.type = type
