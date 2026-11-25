# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GeneratedMetricAttributesType(ModelSimple):
    """
    The generated metric attributes resource type.

    :param value: If omitted defaults to "generated_metric_attributes". Must be one of ["generated_metric_attributes"].
    :type value: str
    """

    allowed_values = {
        "generated_metric_attributes",
    }
    GENERATED_METRIC_ATTRIBUTES: ClassVar["GeneratedMetricAttributesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GeneratedMetricAttributesType.GENERATED_METRIC_ATTRIBUTES = GeneratedMetricAttributesType("generated_metric_attributes")
