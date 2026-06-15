# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GlobalOrgType(ModelSimple):
    """
    The resource type for global user organizations.

    :param value: If omitted defaults to "global_user_orgs". Must be one of ["global_user_orgs"].
    :type value: str
    """

    allowed_values = {
        "global_user_orgs",
    }
    GLOBAL_USER_ORGS: ClassVar["GlobalOrgType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GlobalOrgType.GLOBAL_USER_ORGS = GlobalOrgType("global_user_orgs")
