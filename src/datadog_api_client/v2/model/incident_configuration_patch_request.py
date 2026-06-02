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
    from datadog_api_client.v2.model.incident_configuration_patch_data_request import (
        IncidentConfigurationPatchDataRequest,
    )


class IncidentConfigurationPatchRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_configuration_patch_data_request import (
            IncidentConfigurationPatchDataRequest,
        )

        return {
            "data": (IncidentConfigurationPatchDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentConfigurationPatchDataRequest, **kwargs):
        """
        Request payload for patching an incident configuration.

        :param data: Incident configuration data in a patch request.
        :type data: IncidentConfigurationPatchDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
