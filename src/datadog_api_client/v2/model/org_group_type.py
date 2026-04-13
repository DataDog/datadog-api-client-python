# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgGroupType(ModelSimple):
    """
    Org groups resource type.

    :param value: If omitted defaults to "org_groups". Must be one of ["org_groups"].
    :type value: str
    """

    allowed_values = {
        "org_groups",
    }
    ORG_GROUPS: ClassVar["OrgGroupType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgGroupType.ORG_GROUPS = OrgGroupType("org_groups")
