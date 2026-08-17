# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FilesCoverageResponseType(ModelSimple):
    """
    JSON:API type for files coverage response. The value must always be `ci_app_coverage_files`.

    :param value: If omitted defaults to "ci_app_coverage_files". Must be one of ["ci_app_coverage_files"].
    :type value: str
    """

    allowed_values = {
        "ci_app_coverage_files",
    }
    CI_APP_COVERAGE_FILES: ClassVar["FilesCoverageResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FilesCoverageResponseType.CI_APP_COVERAGE_FILES = FilesCoverageResponseType("ci_app_coverage_files")
