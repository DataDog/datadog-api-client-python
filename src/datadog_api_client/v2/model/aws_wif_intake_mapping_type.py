# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AwsWifIntakeMappingType(ModelSimple):
    """
    Type identifier for an AWS WIF intake mapping.

    :param value: If omitted defaults to "aws_wif_intake_mapping". Must be one of ["aws_wif_intake_mapping"].
    :type value: str
    """

    allowed_values = {
        "aws_wif_intake_mapping",
    }
    AWS_WIF_INTAKE_MAPPING: ClassVar["AwsWifIntakeMappingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AwsWifIntakeMappingType.AWS_WIF_INTAKE_MAPPING = AwsWifIntakeMappingType("aws_wif_intake_mapping")
