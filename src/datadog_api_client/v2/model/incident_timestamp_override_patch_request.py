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
    from datadog_api_client.v2.model.incident_timestamp_override_patch_data import IncidentTimestampOverridePatchData


class IncidentTimestampOverridePatchRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_timestamp_override_patch_data import (
            IncidentTimestampOverridePatchData,
        )

        return {
            "data": (IncidentTimestampOverridePatchData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentTimestampOverridePatchData, **kwargs):
        """
        Request to patch an incident timestamp override.

        :param data: Data for patching an incident timestamp override.
        :type data: IncidentTimestampOverridePatchData
        """
        super().__init__(kwargs)

        self_.data = data
