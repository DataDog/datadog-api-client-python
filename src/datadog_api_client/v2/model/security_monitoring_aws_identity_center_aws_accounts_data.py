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
    from datadog_api_client.v2.model.security_monitoring_aws_identity_center_aws_accounts_attributes import (
        SecurityMonitoringAWSIdentityCenterAWSAccountsAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_aws_identity_center_aws_accounts_resource_type import (
        SecurityMonitoringAWSIdentityCenterAWSAccountsResourceType,
    )


class SecurityMonitoringAWSIdentityCenterAWSAccountsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_aws_identity_center_aws_accounts_attributes import (
            SecurityMonitoringAWSIdentityCenterAWSAccountsAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_aws_identity_center_aws_accounts_resource_type import (
            SecurityMonitoringAWSIdentityCenterAWSAccountsResourceType,
        )

        return {
            "attributes": (SecurityMonitoringAWSIdentityCenterAWSAccountsAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringAWSIdentityCenterAWSAccountsResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringAWSIdentityCenterAWSAccountsAttributes,
        id: str,
        type: SecurityMonitoringAWSIdentityCenterAWSAccountsResourceType,
        **kwargs,
    ):
        """
        The AWS account prerequisites for the AWS IAM Identity Center integration.

        :param attributes: The attributes of the AWS IAM Identity Center AWS account prerequisites.
        :type attributes: SecurityMonitoringAWSIdentityCenterAWSAccountsAttributes

        :param id: The ID of the organization the AWS accounts belong to.
        :type id: str

        :param type: The type of the resource. The value should always be ``aws_identity_center_aws_accounts``.
        :type type: SecurityMonitoringAWSIdentityCenterAWSAccountsResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
