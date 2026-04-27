# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ManagedOrgsType(ModelSimple):
    """
    The resource type for managed organizations.

    :param value: If omitted defaults to "managed_orgs". Must be one of ["managed_orgs"].
    :type value: str
    """

    allowed_values = {
        "managed_orgs",
    }
    MANAGED_ORGS: ClassVar["ManagedOrgsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ManagedOrgsType.MANAGED_ORGS = ManagedOrgsType("managed_orgs")
