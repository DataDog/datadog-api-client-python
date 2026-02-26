# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AWSCcmConfigType(ModelSimple):
    """
    AWS CCM Config resource type.

    :param value: If omitted defaults to "ccm_config". Must be one of ["ccm_config"].
    :type value: str
    """

    allowed_values = {
        "ccm_config",
    }
    CCM_CONFIG: ClassVar["AWSCcmConfigType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AWSCcmConfigType.CCM_CONFIG = AWSCcmConfigType("ccm_config")
