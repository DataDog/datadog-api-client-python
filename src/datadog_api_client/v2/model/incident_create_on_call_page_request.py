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
    from datadog_api_client.v2.model.incident_create_on_call_page_data_request import (
        IncidentCreateOnCallPageDataRequest,
    )


class IncidentCreateOnCallPageRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_create_on_call_page_data_request import (
            IncidentCreateOnCallPageDataRequest,
        )

        return {
            "data": (IncidentCreateOnCallPageDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentCreateOnCallPageDataRequest, **kwargs):
        """
        Request payload for creating an on-call page from an incident.

        :param data: On-call page data in a create request.
        :type data: IncidentCreateOnCallPageDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
