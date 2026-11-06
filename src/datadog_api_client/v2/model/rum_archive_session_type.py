# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumArchiveSessionType(ModelSimple):
    """
    JSON:API resource type.

    :param value: If omitted defaults to "rum_archive_session". Must be one of ["rum_archive_session"].
    :type value: str
    """

    allowed_values = {
        "rum_archive_session",
    }
    RUM_ARCHIVE_SESSION: ClassVar["RumArchiveSessionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumArchiveSessionType.RUM_ARCHIVE_SESSION = RumArchiveSessionType("rum_archive_session")
