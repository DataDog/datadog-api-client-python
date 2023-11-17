# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dora_incident_type import DORAIncidentType


class DORAIncidentResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_incident_type import DORAIncidentType

        return {
            "id": (str,),
            "type": (DORAIncidentType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: Union[DORAIncidentType, UnsetType] = unset, **kwargs):
        """
        Response after receiving a DORA incident event.

        :param id: The ID of the received DORA incident event.
        :type id: str

        :param type: JSON:API type for DORA incident events.
        :type type: DORAIncidentType, optional
        """
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.id = id
