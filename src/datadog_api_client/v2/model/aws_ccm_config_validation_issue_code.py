# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AWSCcmConfigValidationIssueCode(ModelSimple):
    """
    Identifies the specific reason a Cost and Usage Report (CUR) 2.0 configuration failed validation.

    :param value: Must be one of ["ISSUE_CODE_UNSPECIFIED", "CREDENTIAL_ERROR", "BUCKET_NAME_INVALID_GOVCLOUD", "S3_LIST_PERMISSION_MISSING", "S3_GET_PERMISSION_MISSING", "S3_BUCKET_REGION_MISMATCH", "S3_BUCKET_NOT_ACCESSIBLE", "EXPORT_LIST_PERMISSION_MISSING", "EXPORT_GET_PERMISSION_MISSING", "EXPORT_NOT_FOUND", "EXPORT_STATUS_UNHEALTHY", "TIME_GRANULARITY_INVALID", "FILE_FORMAT_INVALID", "INCLUDE_RESOURCES_DISABLED", "REFRESH_CADENCE_INVALID", "OVERWRITE_MODE_INVALID", "QUERY_STATEMENT_INVALID"].
    :type value: str
    """

    allowed_values = {
        "ISSUE_CODE_UNSPECIFIED",
        "CREDENTIAL_ERROR",
        "BUCKET_NAME_INVALID_GOVCLOUD",
        "S3_LIST_PERMISSION_MISSING",
        "S3_GET_PERMISSION_MISSING",
        "S3_BUCKET_REGION_MISMATCH",
        "S3_BUCKET_NOT_ACCESSIBLE",
        "EXPORT_LIST_PERMISSION_MISSING",
        "EXPORT_GET_PERMISSION_MISSING",
        "EXPORT_NOT_FOUND",
        "EXPORT_STATUS_UNHEALTHY",
        "TIME_GRANULARITY_INVALID",
        "FILE_FORMAT_INVALID",
        "INCLUDE_RESOURCES_DISABLED",
        "REFRESH_CADENCE_INVALID",
        "OVERWRITE_MODE_INVALID",
        "QUERY_STATEMENT_INVALID",
    }
    ISSUE_CODE_UNSPECIFIED: ClassVar["AWSCcmConfigValidationIssueCode"]
    CREDENTIAL_ERROR: ClassVar["AWSCcmConfigValidationIssueCode"]
    BUCKET_NAME_INVALID_GOVCLOUD: ClassVar["AWSCcmConfigValidationIssueCode"]
    S3_LIST_PERMISSION_MISSING: ClassVar["AWSCcmConfigValidationIssueCode"]
    S3_GET_PERMISSION_MISSING: ClassVar["AWSCcmConfigValidationIssueCode"]
    S3_BUCKET_REGION_MISMATCH: ClassVar["AWSCcmConfigValidationIssueCode"]
    S3_BUCKET_NOT_ACCESSIBLE: ClassVar["AWSCcmConfigValidationIssueCode"]
    EXPORT_LIST_PERMISSION_MISSING: ClassVar["AWSCcmConfigValidationIssueCode"]
    EXPORT_GET_PERMISSION_MISSING: ClassVar["AWSCcmConfigValidationIssueCode"]
    EXPORT_NOT_FOUND: ClassVar["AWSCcmConfigValidationIssueCode"]
    EXPORT_STATUS_UNHEALTHY: ClassVar["AWSCcmConfigValidationIssueCode"]
    TIME_GRANULARITY_INVALID: ClassVar["AWSCcmConfigValidationIssueCode"]
    FILE_FORMAT_INVALID: ClassVar["AWSCcmConfigValidationIssueCode"]
    INCLUDE_RESOURCES_DISABLED: ClassVar["AWSCcmConfigValidationIssueCode"]
    REFRESH_CADENCE_INVALID: ClassVar["AWSCcmConfigValidationIssueCode"]
    OVERWRITE_MODE_INVALID: ClassVar["AWSCcmConfigValidationIssueCode"]
    QUERY_STATEMENT_INVALID: ClassVar["AWSCcmConfigValidationIssueCode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AWSCcmConfigValidationIssueCode.ISSUE_CODE_UNSPECIFIED = AWSCcmConfigValidationIssueCode("ISSUE_CODE_UNSPECIFIED")
AWSCcmConfigValidationIssueCode.CREDENTIAL_ERROR = AWSCcmConfigValidationIssueCode("CREDENTIAL_ERROR")
AWSCcmConfigValidationIssueCode.BUCKET_NAME_INVALID_GOVCLOUD = AWSCcmConfigValidationIssueCode(
    "BUCKET_NAME_INVALID_GOVCLOUD"
)
AWSCcmConfigValidationIssueCode.S3_LIST_PERMISSION_MISSING = AWSCcmConfigValidationIssueCode(
    "S3_LIST_PERMISSION_MISSING"
)
AWSCcmConfigValidationIssueCode.S3_GET_PERMISSION_MISSING = AWSCcmConfigValidationIssueCode("S3_GET_PERMISSION_MISSING")
AWSCcmConfigValidationIssueCode.S3_BUCKET_REGION_MISMATCH = AWSCcmConfigValidationIssueCode("S3_BUCKET_REGION_MISMATCH")
AWSCcmConfigValidationIssueCode.S3_BUCKET_NOT_ACCESSIBLE = AWSCcmConfigValidationIssueCode("S3_BUCKET_NOT_ACCESSIBLE")
AWSCcmConfigValidationIssueCode.EXPORT_LIST_PERMISSION_MISSING = AWSCcmConfigValidationIssueCode(
    "EXPORT_LIST_PERMISSION_MISSING"
)
AWSCcmConfigValidationIssueCode.EXPORT_GET_PERMISSION_MISSING = AWSCcmConfigValidationIssueCode(
    "EXPORT_GET_PERMISSION_MISSING"
)
AWSCcmConfigValidationIssueCode.EXPORT_NOT_FOUND = AWSCcmConfigValidationIssueCode("EXPORT_NOT_FOUND")
AWSCcmConfigValidationIssueCode.EXPORT_STATUS_UNHEALTHY = AWSCcmConfigValidationIssueCode("EXPORT_STATUS_UNHEALTHY")
AWSCcmConfigValidationIssueCode.TIME_GRANULARITY_INVALID = AWSCcmConfigValidationIssueCode("TIME_GRANULARITY_INVALID")
AWSCcmConfigValidationIssueCode.FILE_FORMAT_INVALID = AWSCcmConfigValidationIssueCode("FILE_FORMAT_INVALID")
AWSCcmConfigValidationIssueCode.INCLUDE_RESOURCES_DISABLED = AWSCcmConfigValidationIssueCode(
    "INCLUDE_RESOURCES_DISABLED"
)
AWSCcmConfigValidationIssueCode.REFRESH_CADENCE_INVALID = AWSCcmConfigValidationIssueCode("REFRESH_CADENCE_INVALID")
AWSCcmConfigValidationIssueCode.OVERWRITE_MODE_INVALID = AWSCcmConfigValidationIssueCode("OVERWRITE_MODE_INVALID")
AWSCcmConfigValidationIssueCode.QUERY_STATEMENT_INVALID = AWSCcmConfigValidationIssueCode("QUERY_STATEMENT_INVALID")
