# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamsOwnershipMatchType(ModelSimple):
    """
    How the `view_name` is matched against RUM view names.

    :param value: If omitted defaults to "exact". Must be one of ["exact", "prefix"].
    :type value: str
    """

    allowed_values = {
        "exact",
        "prefix",
    }
    EXACT: ClassVar["TeamsOwnershipMatchType"]
    PREFIX: ClassVar["TeamsOwnershipMatchType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamsOwnershipMatchType.EXACT = TeamsOwnershipMatchType("exact")
TeamsOwnershipMatchType.PREFIX = TeamsOwnershipMatchType("prefix")
