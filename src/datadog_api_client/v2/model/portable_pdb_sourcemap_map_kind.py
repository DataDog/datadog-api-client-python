# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PortablePdbSourcemapMapKind(ModelSimple):
    """
    The type of source map. Always `portable_pdb` for Portable PDB files.

    :param value: If omitted defaults to "portable_pdb". Must be one of ["portable_pdb"].
    :type value: str
    """

    allowed_values = {
        "portable_pdb",
    }
    PORTABLE_PDB: ClassVar["PortablePdbSourcemapMapKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PortablePdbSourcemapMapKind.PORTABLE_PDB = PortablePdbSourcemapMapKind("portable_pdb")
