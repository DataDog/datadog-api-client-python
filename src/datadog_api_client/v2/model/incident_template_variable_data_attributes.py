# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentTemplateVariableDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "display_name": (str,),
            "domain": (str,),
            "variable": (str,),
        }

    attribute_map = {
        "description": "description",
        "display_name": "display_name",
        "domain": "domain",
        "variable": "variable",
    }

    def __init__(self_, description: str, display_name: str, domain: str, variable: str, **kwargs):
        """
        Attributes of a template variable.

        :param description: A description of the template variable.
        :type description: str

        :param display_name: The display name of the template variable.
        :type display_name: str

        :param domain: The domain of the template variable.
        :type domain: str

        :param variable: The variable name used in templates.
        :type variable: str
        """
        super().__init__(kwargs)

        self_.description = description
        self_.display_name = display_name
        self_.domain = domain
        self_.variable = variable
