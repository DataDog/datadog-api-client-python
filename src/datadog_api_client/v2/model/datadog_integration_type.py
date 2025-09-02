# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DatadogIntegrationType(ModelSimple):
    """
    The definition of the `DatadogIntegrationType` object.

    :param value: If omitted defaults to "Datadog". Must be one of ["Datadog"].
    :type value: str
    """

    allowed_values = {
        "Datadog",
    }
    DATADOG: ClassVar["DatadogIntegrationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DatadogIntegrationType.DATADOG = DatadogIntegrationType("Datadog")
