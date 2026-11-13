# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsBanditV2WarningCode(ModelSimple):
    """
    Code that identifies the warning. `datadog_flag_configuration_omitted` means the caller lacks feature flag or environment read permissions, so the response leaves out `datadog_flag_configuration`.

    :param value: If omitted defaults to "datadog_flag_configuration_omitted". Must be one of ["datadog_flag_configuration_omitted"].
    :type value: str
    """

    allowed_values = {
        "datadog_flag_configuration_omitted",
    }
    DATADOG_FLAG_CONFIGURATION_OMITTED: ClassVar["ExperimentsBanditV2WarningCode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsBanditV2WarningCode.DATADOG_FLAG_CONFIGURATION_OMITTED = ExperimentsBanditV2WarningCode(
    "datadog_flag_configuration_omitted"
)
