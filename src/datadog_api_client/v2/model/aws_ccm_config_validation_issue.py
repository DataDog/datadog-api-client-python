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
    from datadog_api_client.v2.model.aws_ccm_config_validation_issue_code import AWSCcmConfigValidationIssueCode


class AWSCcmConfigValidationIssue(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_ccm_config_validation_issue_code import AWSCcmConfigValidationIssueCode

        return {
            "code": (AWSCcmConfigValidationIssueCode,),
            "description": (str,),
        }

    attribute_map = {
        "code": "code",
        "description": "description",
    }

    def __init__(self_, code: AWSCcmConfigValidationIssueCode, description: str, **kwargs):
        """
        A single validation issue found while validating an AWS Cost and Usage Report (CUR) 2.0 configuration.

        :param code: Identifies the specific reason a Cost and Usage Report (CUR) 2.0 configuration failed validation.
        :type code: AWSCcmConfigValidationIssueCode

        :param description: Human-readable description of the validation issue.
        :type description: str
        """
        super().__init__(kwargs)

        self_.code = code
        self_.description = description
