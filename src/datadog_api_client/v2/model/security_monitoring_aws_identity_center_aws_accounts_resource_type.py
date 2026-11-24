# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringAWSIdentityCenterAWSAccountsResourceType(ModelSimple):
    """
    The type of the resource. The value should always be `aws_identity_center_aws_accounts`.

    :param value: If omitted defaults to "aws_identity_center_aws_accounts". Must be one of ["aws_identity_center_aws_accounts"].
    :type value: str
    """

    allowed_values = {
        "aws_identity_center_aws_accounts",
    }
    AWS_IDENTITY_CENTER_AWS_ACCOUNTS: ClassVar["SecurityMonitoringAWSIdentityCenterAWSAccountsResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringAWSIdentityCenterAWSAccountsResourceType.AWS_IDENTITY_CENTER_AWS_ACCOUNTS = (
    SecurityMonitoringAWSIdentityCenterAWSAccountsResourceType("aws_identity_center_aws_accounts")
)
