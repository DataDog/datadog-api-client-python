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
    from datadog_api_client.v2.model.incident_create_page_response_data import IncidentCreatePageResponseData


class IncidentCreatePageResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_create_page_response_data import IncidentCreatePageResponseData

        return {
            "data": (IncidentCreatePageResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentCreatePageResponseData, **kwargs):
        """
        Response from creating a page from an incident.

        :param data: Data from creating a page.
        :type data: IncidentCreatePageResponseData
        """
        super().__init__(kwargs)

        self_.data = data
