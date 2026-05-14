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
    from datadog_api_client.v2.model.incident_render_template_data_attributes_request import (
        IncidentRenderTemplateDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_rendered_template_type import IncidentRenderedTemplateType


class IncidentRenderTemplateDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_render_template_data_attributes_request import (
            IncidentRenderTemplateDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_rendered_template_type import IncidentRenderedTemplateType

        return {
            "attributes": (IncidentRenderTemplateDataAttributesRequest,),
            "type": (IncidentRenderedTemplateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: IncidentRenderTemplateDataAttributesRequest, type: IncidentRenderedTemplateType, **kwargs
    ):
        """
        Data for rendering a template.

        :param attributes: Attributes for rendering a template.
        :type attributes: IncidentRenderTemplateDataAttributesRequest

        :param type: Rendered template resource type.
        :type type: IncidentRenderedTemplateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
