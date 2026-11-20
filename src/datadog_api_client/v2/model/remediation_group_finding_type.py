# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RemediationGroupFindingType(ModelSimple):
    """
    Value of the findings' `@finding_type` attribute that a grouping definition covers.

    :param value: Must be one of ["library_vulnerability", "host_and_container_vulnerability"].
    :type value: str
    """

    allowed_values = {
        "library_vulnerability",
        "host_and_container_vulnerability",
    }
    LIBRARY_VULNERABILITY: ClassVar["RemediationGroupFindingType"]
    HOST_AND_CONTAINER_VULNERABILITY: ClassVar["RemediationGroupFindingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RemediationGroupFindingType.LIBRARY_VULNERABILITY = RemediationGroupFindingType("library_vulnerability")
RemediationGroupFindingType.HOST_AND_CONTAINER_VULNERABILITY = RemediationGroupFindingType(
    "host_and_container_vulnerability"
)
