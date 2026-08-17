# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FilesCoverageRequestType(ModelSimple):
    """
    JSON:API type for files coverage request. The value must always be `ci_app_coverage_files_request`.

    :param value: If omitted defaults to "ci_app_coverage_files_request". Must be one of ["ci_app_coverage_files_request"].
    :type value: str
    """

    allowed_values = {
        "ci_app_coverage_files_request",
    }
    CI_APP_COVERAGE_FILES_REQUEST: ClassVar["FilesCoverageRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FilesCoverageRequestType.CI_APP_COVERAGE_FILES_REQUEST = FilesCoverageRequestType("ci_app_coverage_files_request")
