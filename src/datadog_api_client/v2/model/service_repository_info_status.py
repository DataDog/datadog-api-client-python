# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ServiceRepositoryInfoStatus(ModelSimple):
    """
    The status of the service repository info lookup.

    :param value: Must be one of ["success", "not_found", "no_repository", "internal_error", "unknown"].
    :type value: str
    """

    allowed_values = {
        "success",
        "not_found",
        "no_repository",
        "internal_error",
        "unknown",
    }
    SUCCESS: ClassVar["ServiceRepositoryInfoStatus"]
    NOT_FOUND: ClassVar["ServiceRepositoryInfoStatus"]
    NO_REPOSITORY: ClassVar["ServiceRepositoryInfoStatus"]
    INTERNAL_ERROR: ClassVar["ServiceRepositoryInfoStatus"]
    UNKNOWN: ClassVar["ServiceRepositoryInfoStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ServiceRepositoryInfoStatus.SUCCESS = ServiceRepositoryInfoStatus("success")
ServiceRepositoryInfoStatus.NOT_FOUND = ServiceRepositoryInfoStatus("not_found")
ServiceRepositoryInfoStatus.NO_REPOSITORY = ServiceRepositoryInfoStatus("no_repository")
ServiceRepositoryInfoStatus.INTERNAL_ERROR = ServiceRepositoryInfoStatus("internal_error")
ServiceRepositoryInfoStatus.UNKNOWN = ServiceRepositoryInfoStatus("unknown")
