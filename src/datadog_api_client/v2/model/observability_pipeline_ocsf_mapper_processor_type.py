# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineOcsfMapperProcessorType(ModelSimple):
    """
    The processor type. The value should always be `ocsf_mapper`.

    :param value: If omitted defaults to "ocsf_mapper". Must be one of ["ocsf_mapper"].
    :type value: str
    """

    allowed_values = {
        "ocsf_mapper",
    }
    OCSF_MAPPER: ClassVar["ObservabilityPipelineOcsfMapperProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineOcsfMapperProcessorType.OCSF_MAPPER = ObservabilityPipelineOcsfMapperProcessorType("ocsf_mapper")
