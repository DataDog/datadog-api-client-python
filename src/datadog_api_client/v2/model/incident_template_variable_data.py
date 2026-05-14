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
    from datadog_api_client.v2.model.incident_template_variable_data_attributes import (
        IncidentTemplateVariableDataAttributes,
    )
    from datadog_api_client.v2.model.incident_template_variable_type import IncidentTemplateVariableType


class IncidentTemplateVariableData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_template_variable_data_attributes import (
            IncidentTemplateVariableDataAttributes,
        )
        from datadog_api_client.v2.model.incident_template_variable_type import IncidentTemplateVariableType

        return {
            "attributes": (IncidentTemplateVariableDataAttributes,),
            "id": (str,),
            "type": (IncidentTemplateVariableType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: IncidentTemplateVariableDataAttributes, id: str, type: IncidentTemplateVariableType, **kwargs
    ):
        """
        Template variable data.

        :param attributes: Attributes of a template variable.
        :type attributes: IncidentTemplateVariableDataAttributes

        :param id: The template variable identifier.
        :type id: str

        :param type: Template variable resource type.
        :type type: IncidentTemplateVariableType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
