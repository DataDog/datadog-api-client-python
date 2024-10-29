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
    from datadog_api_client.v2.model.incident_type_create_data import IncidentTypeCreateData


class IncidentTypeCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_type_create_data import IncidentTypeCreateData

        return {
            "data": (IncidentTypeCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentTypeCreateData, **kwargs):
        """
        Create request for an incident type.

        :param data: Incident type data for a create request.
        :type data: IncidentTypeCreateData
        """
        super().__init__(kwargs)

        self_.data = data
