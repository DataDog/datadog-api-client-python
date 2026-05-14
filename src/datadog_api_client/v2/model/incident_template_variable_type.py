# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentTemplateVariableType(ModelSimple):
    """
    Template variable resource type.

    :param value: If omitted defaults to "template_variables". Must be one of ["template_variables"].
    :type value: str
    """

    allowed_values = {
        "template_variables",
    }
    TEMPLATE_VARIABLES: ClassVar["IncidentTemplateVariableType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentTemplateVariableType.TEMPLATE_VARIABLES = IncidentTemplateVariableType("template_variables")
