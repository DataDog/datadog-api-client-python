# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CalculatedField(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "expression": (str,),
            "name": (str,),
        }

    attribute_map = {
        "expression": "expression",
        "name": "name",
    }

    def __init__(self_, expression: str, name: str, **kwargs):
        """
        Calculated field.

        :param expression: Expression.
        :type expression: str

        :param name: Field name.
        :type name: str
        """
        super().__init__(kwargs)

        self_.expression = expression
        self_.name = name
