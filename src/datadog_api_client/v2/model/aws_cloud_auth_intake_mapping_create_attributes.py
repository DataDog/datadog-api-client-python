# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSCloudAuthIntakeMappingCreateAttributes(ModelNormal):
    validations = {
        "arn_pattern": {
            "min_length": 1,
        },
    }

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
        Attributes for creating an AWS cloud authentication intake mapping.

        :param arn_pattern: AWS caller ARN pattern allowed to authenticate for telemetry submission. ARN syntax and AWS integration membership are validated by the server. For an assumed role, use the STS assumed-role ARN with a trailing /* wildcard to match its sessions.
        :type arn_pattern: str
        """
        super().__init__(kwargs)

        self_.arn_pattern = arn_pattern
