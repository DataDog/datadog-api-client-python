# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_rendered_template_data_attributes import (
        IncidentRenderedTemplateDataAttributes,
    )
    from datadog_api_client.v2.model.incident_rendered_template_type import IncidentRenderedTemplateType


class IncidentRenderedTemplateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_rendered_template_data_attributes import (
            IncidentRenderedTemplateDataAttributes,
        )
        from datadog_api_client.v2.model.incident_rendered_template_type import IncidentRenderedTemplateType

        return {
            "attributes": (IncidentRenderedTemplateDataAttributes,),
            "id": (UUID,),
            "type": (IncidentRenderedTemplateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentRenderedTemplateDataAttributes,
        id: UUID,
        type: IncidentRenderedTemplateType,
        **kwargs,
    ):
        """
        Rendered template data.

        :param attributes: Attributes of a rendered template.
        :type attributes: IncidentRenderedTemplateDataAttributes

        :param id: The rendered template identifier.
        :type id: UUID

        :param type: Rendered template resource type.
        :type type: IncidentRenderedTemplateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
