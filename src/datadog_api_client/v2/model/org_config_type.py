# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgConfigType(ModelSimple):
    """
    Data type of an Org Config.

    :param value: If omitted defaults to "org_configs". Must be one of ["org_configs"].
    :type value: str
    """

    allowed_values = {
        "org_configs",
    }
    ORG_CONFIGS: ClassVar["OrgConfigType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgConfigType.ORG_CONFIGS = OrgConfigType("org_configs")
