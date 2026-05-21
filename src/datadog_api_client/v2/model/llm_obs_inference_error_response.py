# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsInferenceErrorResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "message": (str,),
            "type": (str,),
        }

    attribute_map = {
        "message": "message",
        "type": "type",
    }

    def __init__(self_, message: str, type: str, **kwargs):
        """
        Error details returned when an inference provider returns an error.

        :param message: A human-readable description of the error.
        :type message: str

        :param type: The provider-specific error type.
        :type type: str
        """
        super().__init__(kwargs)

        self_.message = message
        self_.type = type
