# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AzureStorageDestinationType(ModelSimple):
    """
    The destination type. The value should always be `azure_storage`.

    :param value: If omitted defaults to "azure_storage". Must be one of ["azure_storage"].
    :type value: str
    """

    allowed_values = {
        "azure_storage",
    }
    AZURE_STORAGE: ClassVar["AzureStorageDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AzureStorageDestinationType.AZURE_STORAGE = AzureStorageDestinationType("azure_storage")
