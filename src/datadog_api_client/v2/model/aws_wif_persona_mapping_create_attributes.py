# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AwsWifPersonaMappingCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_identifier": (str,),
            "arn_pattern": (str,),
        }

    attribute_map = {
        "account_identifier": "account_identifier",
        "arn_pattern": "arn_pattern",
    }

    def __init__(self_, account_identifier: str, arn_pattern: str, **kwargs):
        """
        Attributes for creating an AWS WIF persona mapping.

        :param account_identifier: The Datadog user handle (email address) to map the AWS principal to.
        :type account_identifier: str

        :param arn_pattern: The AWS IAM ARN pattern identifying the role or user that will be mapped.
            Supports wildcards ( ``*`` ) to match multiple principals within an account.
        :type arn_pattern: str
        """
        super().__init__(kwargs)

        self_.account_identifier = account_identifier
        self_.arn_pattern = arn_pattern
