# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsSubjectTypeV2DTODataType(ModelSimple):
    """
    Subject types resource type.

    :param value: If omitted defaults to "subject-types". Must be one of ["subject-types"].
    :type value: str
    """

    allowed_values = {
        "subject-types",
    }
    SUBJECT_TYPES: ClassVar["ExperimentsSubjectTypeV2DTODataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsSubjectTypeV2DTODataType.SUBJECT_TYPES = ExperimentsSubjectTypeV2DTODataType("subject-types")
