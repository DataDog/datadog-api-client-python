# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SBOMFormat(ModelSimple):
    """
    The SBOM standard

    :param value: Must be one of ["CycloneDX", "SPDX"].
    :type value: str
    """

    allowed_values = {
        "CycloneDX",
        "SPDX",
    }
    CYCLONEDX: ClassVar["SBOMFormat"]
    SPDX: ClassVar["SBOMFormat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SBOMFormat.CYCLONEDX = SBOMFormat("CycloneDX")
SBOMFormat.SPDX = SBOMFormat("SPDX")
