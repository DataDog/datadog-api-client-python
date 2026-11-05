# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayModelMetadataSourceMatchedBy(ModelSimple):
    """
    Identifier strategy used to match the gateway catalog entry. Date-suffix and shared canonical-model fallback matches produce partial metadata.

    :param value: Must be one of ["override", "wire_id", "canonical_id", "wire_id_date_suffix", "canonical_model"].
    :type value: str
    """

    allowed_values = {
        "override",
        "wire_id",
        "canonical_id",
        "wire_id_date_suffix",
        "canonical_model",
    }
    OVERRIDE: ClassVar["AiGatewayModelMetadataSourceMatchedBy"]
    WIRE_ID: ClassVar["AiGatewayModelMetadataSourceMatchedBy"]
    CANONICAL_ID: ClassVar["AiGatewayModelMetadataSourceMatchedBy"]
    WIRE_ID_DATE_SUFFIX: ClassVar["AiGatewayModelMetadataSourceMatchedBy"]
    CANONICAL_MODEL: ClassVar["AiGatewayModelMetadataSourceMatchedBy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayModelMetadataSourceMatchedBy.OVERRIDE = AiGatewayModelMetadataSourceMatchedBy("override")
AiGatewayModelMetadataSourceMatchedBy.WIRE_ID = AiGatewayModelMetadataSourceMatchedBy("wire_id")
AiGatewayModelMetadataSourceMatchedBy.CANONICAL_ID = AiGatewayModelMetadataSourceMatchedBy("canonical_id")
AiGatewayModelMetadataSourceMatchedBy.WIRE_ID_DATE_SUFFIX = AiGatewayModelMetadataSourceMatchedBy("wire_id_date_suffix")
AiGatewayModelMetadataSourceMatchedBy.CANONICAL_MODEL = AiGatewayModelMetadataSourceMatchedBy("canonical_model")
