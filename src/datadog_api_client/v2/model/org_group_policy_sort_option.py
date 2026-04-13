# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgGroupPolicySortOption(ModelSimple):
    """
    Field to sort policies by.

    :param value: If omitted defaults to "id". Must be one of ["id", "-id", "name", "-name"].
    :type value: str
    """

    allowed_values = {
        "id",
        "-id",
        "name",
        "-name",
    }
    ID: ClassVar["OrgGroupPolicySortOption"]
    MINUS_ID: ClassVar["OrgGroupPolicySortOption"]
    NAME: ClassVar["OrgGroupPolicySortOption"]
    MINUS_NAME: ClassVar["OrgGroupPolicySortOption"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgGroupPolicySortOption.ID = OrgGroupPolicySortOption("id")
OrgGroupPolicySortOption.MINUS_ID = OrgGroupPolicySortOption("-id")
OrgGroupPolicySortOption.NAME = OrgGroupPolicySortOption("name")
OrgGroupPolicySortOption.MINUS_NAME = OrgGroupPolicySortOption("-name")
