# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOFormula(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "formula": (str,),
        }

    attribute_map = {
        "formula": "formula",
    }

    def __init__(self_, formula: str, **kwargs):
        """
        A formula that specifies how to combine the results of multiple queries.

        :param formula: The formula string, which is an expression involving named queries.
        :type formula: str
        """
        super().__init__(kwargs)

        self_.formula = formula
