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
    from datadog_api_client.v2.model.incident_user_defined_field_response_data import (
        IncidentUserDefinedFieldResponseData,
    )


class IncidentUserDefinedFieldResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_field_response_data import (
            IncidentUserDefinedFieldResponseData,
        )

        return {
            "data": (IncidentUserDefinedFieldResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentUserDefinedFieldResponseData, **kwargs):
        """
        Response containing a single incident user-defined field.

        :param data: Data object for an incident user-defined field response.
        :type data: IncidentUserDefinedFieldResponseData
        """
        super().__init__(kwargs)

        self_.data = data
