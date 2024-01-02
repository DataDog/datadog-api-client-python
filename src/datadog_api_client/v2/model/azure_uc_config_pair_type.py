# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AzureUCConfigPairType(ModelSimple):
    """
    Type of Azure config pair.

    :param value: If omitted defaults to "azure_uc_configs". Must be one of ["azure_uc_configs"].
    :type value: str
    """

    allowed_values = {
        "azure_uc_configs",
    }
    AZURE_UC_CONFIGS: ClassVar["AzureUCConfigPairType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AzureUCConfigPairType.AZURE_UC_CONFIGS = AzureUCConfigPairType("azure_uc_configs")
