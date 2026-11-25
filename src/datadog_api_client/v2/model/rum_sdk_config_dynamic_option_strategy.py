# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMSdkConfigDynamicOptionStrategy(ModelSimple):
    """
    The strategy used to extract the dynamic value.

    :param value: Must be one of ["js", "cookie", "dom", "localStorage"].
    :type value: str
    """

    allowed_values = {
        "js",
        "cookie",
        "dom",
        "localStorage",
    }
    JS: ClassVar["RUMSdkConfigDynamicOptionStrategy"]
    COOKIE: ClassVar["RUMSdkConfigDynamicOptionStrategy"]
    DOM: ClassVar["RUMSdkConfigDynamicOptionStrategy"]
    LOCAL_STORAGE: ClassVar["RUMSdkConfigDynamicOptionStrategy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMSdkConfigDynamicOptionStrategy.JS = RUMSdkConfigDynamicOptionStrategy("js")
RUMSdkConfigDynamicOptionStrategy.COOKIE = RUMSdkConfigDynamicOptionStrategy("cookie")
RUMSdkConfigDynamicOptionStrategy.DOM = RUMSdkConfigDynamicOptionStrategy("dom")
RUMSdkConfigDynamicOptionStrategy.LOCAL_STORAGE = RUMSdkConfigDynamicOptionStrategy("localStorage")
