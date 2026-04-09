# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsAnnotatedInteractionsType(ModelSimple):
    """
    Resource type for annotated interactions.

    :param value: If omitted defaults to "annotated_interactions". Must be one of ["annotated_interactions"].
    :type value: str
    """

    allowed_values = {
        "annotated_interactions",
    }
    ANNOTATED_INTERACTIONS: ClassVar["LLMObsAnnotatedInteractionsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsAnnotatedInteractionsType.ANNOTATED_INTERACTIONS = LLMObsAnnotatedInteractionsType("annotated_interactions")
