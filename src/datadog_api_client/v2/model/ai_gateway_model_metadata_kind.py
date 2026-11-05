# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayModelMetadataKind(ModelSimple):
    """
    Primary model kind. Decision models return a choice or score instead of generated text.

    :param value: Must be one of ["language", "embedding", "image", "audio", "decision", "reranking"].
    :type value: str
    """

    allowed_values = {
        "language",
        "embedding",
        "image",
        "audio",
        "decision",
        "reranking",
    }
    LANGUAGE: ClassVar["AiGatewayModelMetadataKind"]
    EMBEDDING: ClassVar["AiGatewayModelMetadataKind"]
    IMAGE: ClassVar["AiGatewayModelMetadataKind"]
    AUDIO: ClassVar["AiGatewayModelMetadataKind"]
    DECISION: ClassVar["AiGatewayModelMetadataKind"]
    RERANKING: ClassVar["AiGatewayModelMetadataKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayModelMetadataKind.LANGUAGE = AiGatewayModelMetadataKind("language")
AiGatewayModelMetadataKind.EMBEDDING = AiGatewayModelMetadataKind("embedding")
AiGatewayModelMetadataKind.IMAGE = AiGatewayModelMetadataKind("image")
AiGatewayModelMetadataKind.AUDIO = AiGatewayModelMetadataKind("audio")
AiGatewayModelMetadataKind.DECISION = AiGatewayModelMetadataKind("decision")
AiGatewayModelMetadataKind.RERANKING = AiGatewayModelMetadataKind("reranking")
