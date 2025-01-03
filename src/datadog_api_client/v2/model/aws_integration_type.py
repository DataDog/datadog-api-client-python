# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AWSIntegrationType(ModelSimple):
    """
    The definition of `AWSIntegrationType` object.

    :param value: If omitted defaults to "AWS". Must be one of ["AWS"].
    :type value: str
    """

    allowed_values = {
        "AWS",
    }
    AWS: ClassVar["AWSIntegrationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AWSIntegrationType.AWS = AWSIntegrationType("AWS")
