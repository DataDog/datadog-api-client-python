# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AWSCcmConfigValidationType(ModelSimple):
    """
    AWS CCM config validation resource type.

    :param value: If omitted defaults to "ccm_config_validation". Must be one of ["ccm_config_validation"].
    :type value: str
    """

    allowed_values = {
        "ccm_config_validation",
    }
    CCM_CONFIG_VALIDATION: ClassVar["AWSCcmConfigValidationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AWSCcmConfigValidationType.CCM_CONFIG_VALIDATION = AWSCcmConfigValidationType("ccm_config_validation")
