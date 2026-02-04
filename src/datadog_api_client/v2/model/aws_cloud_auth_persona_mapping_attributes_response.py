# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSCloudAuthPersonaMappingAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_identifier": (str,),
            "account_uuid": (str,),
            "arn_pattern": (str,),
        }

    attribute_map = {
        "account_identifier": "account_identifier",
        "account_uuid": "account_uuid",
        "arn_pattern": "arn_pattern",
    }

    def __init__(self_, account_identifier: str, account_uuid: str, arn_pattern: str, **kwargs):
        """
        Attributes for AWS cloud authentication persona mapping response

        :param account_identifier: Datadog account identifier (email or handle) mapped to the AWS principal
        :type account_identifier: str

        :param account_uuid: Datadog account UUID
        :type account_uuid: str

        :param arn_pattern: AWS IAM ARN pattern to match for authentication
        :type arn_pattern: str
        """
        super().__init__(kwargs)

        self_.account_identifier = account_identifier
        self_.account_uuid = account_uuid
        self_.arn_pattern = arn_pattern
