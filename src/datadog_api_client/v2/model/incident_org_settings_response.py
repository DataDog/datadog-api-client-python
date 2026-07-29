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
    from datadog_api_client.v2.model.incident_org_settings_data_response import IncidentOrgSettingsDataResponse


class IncidentOrgSettingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_org_settings_data_response import IncidentOrgSettingsDataResponse

        return {
            "data": (IncidentOrgSettingsDataResponse,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentOrgSettingsDataResponse, **kwargs):
        """
        Response with a single incident org settings resource.

        :param data: Incident org settings data in a response.
        :type data: IncidentOrgSettingsDataResponse
        """
        super().__init__(kwargs)

        self_.data = data
