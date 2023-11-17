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
    from datadog_api_client.v2.model.dora_incident_response_data import DORAIncidentResponseData


class DORAIncidentResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_incident_response_data import DORAIncidentResponseData

        return {
            "data": (DORAIncidentResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: DORAIncidentResponseData, **kwargs):
        """
        Response after receiving a DORA incident event.

        :param data: Response after receiving a DORA incident event.
        :type data: DORAIncidentResponseData
        """
        super().__init__(kwargs)

        self_.data = data
