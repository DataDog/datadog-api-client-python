# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineRenameFieldsProcessorType(ModelSimple):
    """
    The processor type. The value should always be `rename_fields`.

    :param value: If omitted defaults to "rename_fields". Must be one of ["rename_fields"].
    :type value: str
    """

    allowed_values = {
        "rename_fields",
    }
    RENAME_FIELDS: ClassVar["ObservabilityPipelineRenameFieldsProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineRenameFieldsProcessorType.RENAME_FIELDS = ObservabilityPipelineRenameFieldsProcessorType(
    "rename_fields"
)
