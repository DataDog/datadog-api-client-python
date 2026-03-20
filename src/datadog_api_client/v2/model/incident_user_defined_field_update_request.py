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
    from datadog_api_client.v2.model.incident_user_defined_field_update_data import IncidentUserDefinedFieldUpdateData


class IncidentUserDefinedFieldUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_field_update_data import (
            IncidentUserDefinedFieldUpdateData,
        )

        return {
            "data": (IncidentUserDefinedFieldUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentUserDefinedFieldUpdateData, **kwargs):
        """
        Request body for updating an incident user-defined field.

        :param data: Data for updating an incident user-defined field.
        :type data: IncidentUserDefinedFieldUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
