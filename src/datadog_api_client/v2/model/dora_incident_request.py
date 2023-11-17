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
    from datadog_api_client.v2.model.dora_incident_request_data import DORAIncidentRequestData


class DORAIncidentRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_incident_request_data import DORAIncidentRequestData

        return {
            "data": (DORAIncidentRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: DORAIncidentRequestData, **kwargs):
        """
        Request to create a DORA incident event.

        :param data: The JSON:API data.
        :type data: DORAIncidentRequestData
        """
        super().__init__(kwargs)

        self_.data = data
