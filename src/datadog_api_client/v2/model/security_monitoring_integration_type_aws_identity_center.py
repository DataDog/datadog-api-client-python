# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringIntegrationTypeAWSIdentityCenter(ModelSimple):
    """
    The source type for an AWS IAM Identity Center entity context sync.

    :param value: If omitted defaults to "AWS_IDENTITY_CENTER". Must be one of ["AWS_IDENTITY_CENTER"].
    :type value: str
    """

    allowed_values = {
        "AWS_IDENTITY_CENTER",
    }
    AWS_IDENTITY_CENTER: ClassVar["SecurityMonitoringIntegrationTypeAWSIdentityCenter"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringIntegrationTypeAWSIdentityCenter.AWS_IDENTITY_CENTER = (
    SecurityMonitoringIntegrationTypeAWSIdentityCenter("AWS_IDENTITY_CENTER")
)
