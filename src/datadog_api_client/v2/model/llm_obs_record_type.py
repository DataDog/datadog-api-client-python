# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsRecordType(ModelSimple):
    """
    Resource type of LLM Observability dataset records.

    :param value: If omitted defaults to "records". Must be one of ["records"].
    :type value: str
    """

    allowed_values = {
        "records",
    }
    RECORDS: ClassVar["LLMObsRecordType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsRecordType.RECORDS = LLMObsRecordType("records")
