# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsLabelSchemaType(ModelSimple):
    """
    Type of a label in an annotation queue label schema.

    :param value: Must be one of ["score", "categorical", "boolean", "text"].
    :type value: str
    """

    allowed_values = {
        "score",
        "categorical",
        "boolean",
        "text",
    }
    SCORE: ClassVar["LLMObsLabelSchemaType"]
    CATEGORICAL: ClassVar["LLMObsLabelSchemaType"]
    BOOLEAN: ClassVar["LLMObsLabelSchemaType"]
    TEXT: ClassVar["LLMObsLabelSchemaType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsLabelSchemaType.SCORE = LLMObsLabelSchemaType("score")
LLMObsLabelSchemaType.CATEGORICAL = LLMObsLabelSchemaType("categorical")
LLMObsLabelSchemaType.BOOLEAN = LLMObsLabelSchemaType("boolean")
LLMObsLabelSchemaType.TEXT = LLMObsLabelSchemaType("text")
