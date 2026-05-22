# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentRenderedTemplateType(ModelSimple):
    """
    Rendered template resource type.

    :param value: If omitted defaults to "rendered_templates". Must be one of ["rendered_templates"].
    :type value: str
    """

    allowed_values = {
        "rendered_templates",
    }
    RENDERED_TEMPLATES: ClassVar["IncidentRenderedTemplateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentRenderedTemplateType.RENDERED_TEMPLATES = IncidentRenderedTemplateType("rendered_templates")
