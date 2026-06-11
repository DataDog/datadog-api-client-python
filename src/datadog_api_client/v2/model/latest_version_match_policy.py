# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LatestVersionMatchPolicy(ModelSimple):
    """
    The policy for matching the latest form version during an upsert operation.

    :param value: Must be one of ["none", "if_etag_match"].
    :type value: str
    """

    allowed_values = {
        "none",
        "if_etag_match",
    }
    NONE: ClassVar["LatestVersionMatchPolicy"]
    IF_ETAG_MATCH: ClassVar["LatestVersionMatchPolicy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LatestVersionMatchPolicy.NONE = LatestVersionMatchPolicy("none")
LatestVersionMatchPolicy.IF_ETAG_MATCH = LatestVersionMatchPolicy("if_etag_match")
