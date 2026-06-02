# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class StatuspageUrlSettingType(ModelSimple):
    """
    Statuspage URL setting resource type.

    :param value: If omitted defaults to "statuspage-url-setting". Must be one of ["statuspage-url-setting"].
    :type value: str
    """

    allowed_values = {
        "statuspage-url-setting",
    }
    STATUSPAGE_URL_SETTING: ClassVar["StatuspageUrlSettingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


StatuspageUrlSettingType.STATUSPAGE_URL_SETTING = StatuspageUrlSettingType("statuspage-url-setting")
