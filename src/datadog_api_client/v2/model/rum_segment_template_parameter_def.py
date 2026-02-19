# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RumSegmentTemplateParameterDef(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "default": (str,),
            "description": (str,),
            "validate": (str,),
        }

    attribute_map = {
        "default": "default",
        "description": "description",
        "validate": "validate",
    }

    def __init__(self_, default: str, description: str, validate: str, **kwargs):
        """
        A parameter definition for a segment template.

        :param default: The default value for the parameter.
        :type default: str

        :param description: A description of the parameter.
        :type description: str

        :param validate: Validation rules for the parameter.
        :type validate: str
        """
        super().__init__(kwargs)

        self_.default = default
        self_.description = description
        self_.validate = validate
