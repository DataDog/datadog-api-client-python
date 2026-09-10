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
    from datadog_api_client.v2.model.files_coverage_request_attributes import FilesCoverageRequestAttributes
    from datadog_api_client.v2.model.files_coverage_request_type import FilesCoverageRequestType


class FilesCoverageRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.files_coverage_request_attributes import FilesCoverageRequestAttributes
        from datadog_api_client.v2.model.files_coverage_request_type import FilesCoverageRequestType

        return {
            "attributes": (FilesCoverageRequestAttributes,),
            "type": (FilesCoverageRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: FilesCoverageRequestAttributes, type: FilesCoverageRequestType, **kwargs):
        """
        Data object for files coverage request.

        :param attributes: Attributes for requesting per-file code coverage data. Exactly one of ``commit_sha`` , ``branch`` , or ``pr_number`` must be provided. At most one of ``service`` , ``codeowner`` , or ``flag`` may be provided.
        :type attributes: FilesCoverageRequestAttributes

        :param type: JSON:API type for files coverage request. The value must always be ``ci_app_coverage_files_request``.
        :type type: FilesCoverageRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
