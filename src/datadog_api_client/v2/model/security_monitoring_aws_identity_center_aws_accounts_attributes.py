# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_aws_identity_center_aws_account import (
        SecurityMonitoringAWSIdentityCenterAWSAccount,
    )


class SecurityMonitoringAWSIdentityCenterAWSAccountsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_aws_identity_center_aws_account import (
            SecurityMonitoringAWSIdentityCenterAWSAccount,
        )

        return {
            "aws_accounts": ([SecurityMonitoringAWSIdentityCenterAWSAccount],),
            "has_valid_prerequisite": (bool,),
            "reason": (str,),
        }

    attribute_map = {
        "aws_accounts": "aws_accounts",
        "has_valid_prerequisite": "has_valid_prerequisite",
        "reason": "reason",
    }

    def __init__(
        self_,
        aws_accounts: List[SecurityMonitoringAWSIdentityCenterAWSAccount],
        has_valid_prerequisite: bool,
        reason: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of the AWS IAM Identity Center AWS account prerequisites.

        :param aws_accounts: The integrated AWS accounts that users are read from, including AWS Organization management accounts
            and any accounts that users were collected from.
        :type aws_accounts: [SecurityMonitoringAWSIdentityCenterAWSAccount]

        :param has_valid_prerequisite: Whether AWS IAM Identity Center users were collected for the organization.
        :type has_valid_prerequisite: bool

        :param reason: The missing setup step when ``has_valid_prerequisite`` is ``false``.
        :type reason: str, optional
        """
        if reason is not unset:
            kwargs["reason"] = reason
        super().__init__(kwargs)

        self_.aws_accounts = aws_accounts
        self_.has_valid_prerequisite = has_valid_prerequisite
