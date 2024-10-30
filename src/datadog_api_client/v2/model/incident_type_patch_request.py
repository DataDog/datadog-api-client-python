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
    from datadog_api_client.v2.model.incident_type_patch_data import IncidentTypePatchData


class IncidentTypePatchRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_type_patch_data import IncidentTypePatchData

        return {
            "data": (IncidentTypePatchData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentTypePatchData, **kwargs):
        """
        Patch request for an incident type.

        :param data: Incident type data for a patch request.
        :type data: IncidentTypePatchData
        """
        super().__init__(kwargs)

        self_.data = data
