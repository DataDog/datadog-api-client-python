# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_segment_template_parameter_def import RumSegmentTemplateParameterDef
    from datadog_api_client.v2.model.rum_segment_template_status import RumSegmentTemplateStatus


class RumSegmentTemplateResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_segment_template_parameter_def import RumSegmentTemplateParameterDef
        from datadog_api_client.v2.model.rum_segment_template_status import RumSegmentTemplateStatus

        return {
            "category": (str,),
            "created_at": (datetime,),
            "description": (str,),
            "modified_at": (datetime,),
            "name": (str,),
            "parameters": ({str: (RumSegmentTemplateParameterDef,)},),
            "status": (RumSegmentTemplateStatus,),
            "version": (int,),
        }

    attribute_map = {
        "category": "category",
        "created_at": "created_at",
        "description": "description",
        "modified_at": "modified_at",
        "name": "name",
        "parameters": "parameters",
        "status": "status",
        "version": "version",
    }

    def __init__(
        self_,
        category: str,
        created_at: datetime,
        description: str,
        modified_at: datetime,
        name: str,
        parameters: Dict[str, RumSegmentTemplateParameterDef],
        status: RumSegmentTemplateStatus,
        version: int,
        **kwargs,
    ):
        """
        Attributes of a segment template in a response.

        :param category: The category of the template.
        :type category: str

        :param created_at: The creation timestamp in RFC 3339 format.
        :type created_at: datetime

        :param description: A description of the template.
        :type description: str

        :param modified_at: The last modification timestamp in RFC 3339 format.
        :type modified_at: datetime

        :param name: The name of the template.
        :type name: str

        :param parameters: The template parameter definitions.
        :type parameters: {str: (RumSegmentTemplateParameterDef,)}

        :param status: The status of a segment template.
        :type status: RumSegmentTemplateStatus

        :param version: The version number of the template.
        :type version: int
        """
        super().__init__(kwargs)

        self_.category = category
        self_.created_at = created_at
        self_.description = description
        self_.modified_at = modified_at
        self_.name = name
        self_.parameters = parameters
        self_.status = status
        self_.version = version
