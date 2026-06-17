# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AwsWifIntakeMappingAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "arn_pattern": (str,),
        }

    attribute_map = {
        "arn_pattern": "arn_pattern",
    }

    def __init__(self_, arn_pattern: str, **kwargs):
        """
        Attributes of an AWS WIF intake mapping.

        :param arn_pattern: The AWS IAM ARN pattern identifying the role or user permitted to obtain an intake API key.
            Supports wildcards ( ``*`` ) to match multiple principals within an account.
        :type arn_pattern: str
        """
        super().__init__(kwargs)

        self_.arn_pattern = arn_pattern
