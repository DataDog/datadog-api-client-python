# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class STIXSpecVersion(ModelSimple):
    """
    The supported STIX specification version.

    :param value: If omitted defaults to "2.1". Must be one of ["2.1"].
    :type value: str
    """

    allowed_values = {
        "2.1",
    }
    VERSION_2_1: ClassVar["STIXSpecVersion"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


STIXSpecVersion.VERSION_2_1 = STIXSpecVersion("2.1")
