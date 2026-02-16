# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DataTransformationContext(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "context_variables": (str,),
            "current_script": (str,),
        }

    attribute_map = {
        "context_variables": "contextVariables",
        "current_script": "currentScript",
    }

    def __init__(self_, context_variables: str, current_script: str, **kwargs):
        """


        :param context_variables: Available context variables for the transformation.
        :type context_variables: str

        :param current_script: The current script to modify or enhance.
        :type current_script: str
        """
        super().__init__(kwargs)

        self_.context_variables = context_variables
        self_.current_script = current_script
