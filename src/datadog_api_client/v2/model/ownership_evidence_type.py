# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OwnershipEvidenceType(ModelSimple):
    """
    The type of the ownership evidence resource. The value should always be `ownership_evidence`.

    :param value: If omitted defaults to "ownership_evidence". Must be one of ["ownership_evidence"].
    :type value: str
    """

    allowed_values = {
        "ownership_evidence",
    }
    OWNERSHIP_EVIDENCE: ClassVar["OwnershipEvidenceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OwnershipEvidenceType.OWNERSHIP_EVIDENCE = OwnershipEvidenceType("ownership_evidence")
