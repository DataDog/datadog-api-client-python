# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineRemoveFieldsProcessorType(ModelSimple):
    """
    The processor type. The value should always be `remove_fields`.

    :param value: If omitted defaults to "remove_fields". Must be one of ["remove_fields"].
    :type value: str
    """

    allowed_values = {
        "remove_fields",
    }
    REMOVE_FIELDS: ClassVar["ObservabilityPipelineRemoveFieldsProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineRemoveFieldsProcessorType.REMOVE_FIELDS = ObservabilityPipelineRemoveFieldsProcessorType(
    "remove_fields"
)
