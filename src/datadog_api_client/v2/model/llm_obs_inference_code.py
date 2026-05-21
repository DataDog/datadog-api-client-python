# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsInferenceCode(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "code": (str,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "code": "code",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, code: str, id: str, type: str, **kwargs):
        """
        A generated code snippet for running an inference request programmatically.

        :param code: The generated code content.
        :type code: str

        :param id: Unique identifier for the code snippet.
        :type id: str

        :param type: The programming language or SDK type of the code snippet.
        :type type: str
        """
        super().__init__(kwargs)

        self_.code = code
        self_.id = id
        self_.type = type
