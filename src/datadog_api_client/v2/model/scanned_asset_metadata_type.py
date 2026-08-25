# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScannedAssetMetadataType(ModelSimple):
    """
    The JSON:API type.

    :param value: If omitted defaults to "scanned-assets-metadata". Must be one of ["scanned-assets-metadata"].
    :type value: str
    """

    allowed_values = {
        "scanned-assets-metadata",
    }
    SCANNED_ASSETS_METADATA: ClassVar["ScannedAssetMetadataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScannedAssetMetadataType.SCANNED_ASSETS_METADATA = ScannedAssetMetadataType("scanned-assets-metadata")
