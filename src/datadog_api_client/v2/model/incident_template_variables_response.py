# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_template_variable_data import IncidentTemplateVariableData


class IncidentTemplateVariablesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_template_variable_data import IncidentTemplateVariableData

        return {
            "data": ([IncidentTemplateVariableData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[IncidentTemplateVariableData], **kwargs):
        """
        Response with a list of template variables.

        :param data: List of template variables.
        :type data: [IncidentTemplateVariableData]
        """
        super().__init__(kwargs)

        self_.data = data
