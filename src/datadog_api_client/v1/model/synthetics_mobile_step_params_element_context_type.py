# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsMobileStepParamsElementContextType(ModelSimple):
    """
    Type of the context that the element is in.

    :param value: Must be one of ["native", "web"].
    :type value: str
    """

    allowed_values = {
        "native",
        "web",
    }
    NATIVE: ClassVar["SyntheticsMobileStepParamsElementContextType"]
    WEB: ClassVar["SyntheticsMobileStepParamsElementContextType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsMobileStepParamsElementContextType.NATIVE = SyntheticsMobileStepParamsElementContextType("native")
SyntheticsMobileStepParamsElementContextType.WEB = SyntheticsMobileStepParamsElementContextType("web")
