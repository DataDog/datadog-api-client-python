# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsMobileStepParamsVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "example": (str,),
            "name": (str,),
        }

    attribute_map = {
        "example": "example",
        "name": "name",
    }

    def __init__(self_, example: str, name: str, **kwargs):
        """
        Variable object for ``extractVariable`` step type.

        :param example: An example for the variable.
        :type example: str

        :param name: The variable name.
        :type name: str
        """
        super().__init__(kwargs)

        self_.example = example
        self_.name = name
