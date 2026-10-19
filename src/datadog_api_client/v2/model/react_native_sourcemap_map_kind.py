# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ReactNativeSourcemapMapKind(ModelSimple):
    """
    The type of source map. Always `react` for React Native source maps.

    :param value: If omitted defaults to "react". Must be one of ["react"].
    :type value: str
    """

    allowed_values = {
        "react",
    }
    REACT: ClassVar["ReactNativeSourcemapMapKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ReactNativeSourcemapMapKind.REACT = ReactNativeSourcemapMapKind("react")
