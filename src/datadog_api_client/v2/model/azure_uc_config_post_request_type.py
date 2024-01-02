# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AzureUCConfigPostRequestType(ModelSimple):
    """
    Type of Azure config Post Request.

    :param value: If omitted defaults to "azure_uc_config_post_request". Must be one of ["azure_uc_config_post_request"].
    :type value: str
    """

    allowed_values = {
        "azure_uc_config_post_request",
    }
    AZURE_UC_CONFIG_POST_REQUEST: ClassVar["AzureUCConfigPostRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AzureUCConfigPostRequestType.AZURE_UC_CONFIG_POST_REQUEST = AzureUCConfigPostRequestType("azure_uc_config_post_request")
