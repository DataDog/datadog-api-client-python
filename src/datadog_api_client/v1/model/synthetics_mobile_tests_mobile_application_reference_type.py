# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsMobileTestsMobileApplicationReferenceType(ModelSimple):
    """
    Reference type for the mobile application for a mobile synthetics test.

    :param value: Must be one of ["latest", "version"].
    :type value: str
    """

    allowed_values = {
        "latest",
        "version",
    }
    LATEST: ClassVar["SyntheticsMobileTestsMobileApplicationReferenceType"]
    VERSION: ClassVar["SyntheticsMobileTestsMobileApplicationReferenceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsMobileTestsMobileApplicationReferenceType.LATEST = SyntheticsMobileTestsMobileApplicationReferenceType(
    "latest"
)
SyntheticsMobileTestsMobileApplicationReferenceType.VERSION = SyntheticsMobileTestsMobileApplicationReferenceType(
    "version"
)
