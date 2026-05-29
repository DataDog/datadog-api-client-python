# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HostMapWidgetScalarRequestResponseFormat(ModelSimple):
    """
    Response format for the scalar formula request. Only `scalar` is supported.

    :param value: If omitted defaults to "scalar". Must be one of ["scalar"].
    :type value: str
    """

    allowed_values = {
        "scalar",
    }
    SCALAR: ClassVar["HostMapWidgetScalarRequestResponseFormat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HostMapWidgetScalarRequestResponseFormat.SCALAR = HostMapWidgetScalarRequestResponseFormat("scalar")
