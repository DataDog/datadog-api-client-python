# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayModelCatalogEntryType(ModelSimple):
    """
    Model catalog entry resource type.

    :param value: If omitted defaults to "model-catalog-entries". Must be one of ["model-catalog-entries"].
    :type value: str
    """

    allowed_values = {
        "model-catalog-entries",
    }
    MODEL_CATALOG_ENTRIES: ClassVar["AiGatewayModelCatalogEntryType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayModelCatalogEntryType.MODEL_CATALOG_ENTRIES = AiGatewayModelCatalogEntryType("model-catalog-entries")
