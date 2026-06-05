# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aws_ccm_config_validation_issue import AWSCcmConfigValidationIssue


class AWSCcmConfigValidationResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_ccm_config_validation_issue import AWSCcmConfigValidationIssue

        return {
            "account_id": (str,),
            "issues": ([AWSCcmConfigValidationIssue],),
        }

    attribute_map = {
        "account_id": "account_id",
        "issues": "issues",
    }

    def __init__(self_, account_id: str, issues: List[AWSCcmConfigValidationIssue], **kwargs):
        """
        Attributes for an AWS CCM config validation response.

        :param account_id: Your AWS Account ID without dashes.
        :type account_id: str

        :param issues: List of validation issues found for the Cost and Usage Report (CUR) 2.0 configuration. Empty when the configuration is valid.
        :type issues: [AWSCcmConfigValidationIssue]
        """
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.issues = issues
