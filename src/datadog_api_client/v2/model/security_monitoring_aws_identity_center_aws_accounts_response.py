# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_aws_identity_center_aws_accounts_data import (
        SecurityMonitoringAWSIdentityCenterAWSAccountsData,
    )


class SecurityMonitoringAWSIdentityCenterAWSAccountsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_aws_identity_center_aws_accounts_data import (
            SecurityMonitoringAWSIdentityCenterAWSAccountsData,
        )

        return {
            "data": (SecurityMonitoringAWSIdentityCenterAWSAccountsData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringAWSIdentityCenterAWSAccountsData, **kwargs):
        """
        Response containing the AWS account prerequisites for the AWS IAM Identity Center integration.

        :param data: The AWS account prerequisites for the AWS IAM Identity Center integration.
        :type data: SecurityMonitoringAWSIdentityCenterAWSAccountsData
        """
        super().__init__(kwargs)

        self_.data = data
