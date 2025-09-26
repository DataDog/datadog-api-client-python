# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RulesetRespDataAttributesRulesItemsReferenceTableFieldPairsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "input_column": (str,),
            "output_key": (str,),
        }

    attribute_map = {
        "input_column": "input_column",
        "output_key": "output_key",
    }

    def __init__(self_, input_column: str, output_key: str, **kwargs):
        """
        The definition of ``RulesetRespDataAttributesRulesItemsReferenceTableFieldPairsItems`` object.

        :param input_column: The ``items`` ``input_column``.
        :type input_column: str

        :param output_key: The ``items`` ``output_key``.
        :type output_key: str
        """
        super().__init__(kwargs)

        self_.input_column = input_column
        self_.output_key = output_key
