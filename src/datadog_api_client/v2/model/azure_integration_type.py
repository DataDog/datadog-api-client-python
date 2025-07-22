# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AzureIntegrationType(ModelSimple):
    """
    The definition of the `AzureIntegrationType` object.

    :param value: If omitted defaults to "Azure". Must be one of ["Azure"].
    :type value: str
    """

    allowed_values = {
        "Azure",
    }
    AZURE: ClassVar["AzureIntegrationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AzureIntegrationType.AZURE = AzureIntegrationType("Azure")
