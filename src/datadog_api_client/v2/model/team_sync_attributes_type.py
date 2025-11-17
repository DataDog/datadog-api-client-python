# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamSyncAttributesType(ModelSimple):
    """
    The type of synchronization operation. "link" connects teams by matching names. "provision" creates new teams when no match is found.

    :param value: Must be one of ["link", "provision"].
    :type value: str
    """

    allowed_values = {
        "link",
        "provision",
    }
    LINK: ClassVar["TeamSyncAttributesType"]
    PROVISION: ClassVar["TeamSyncAttributesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamSyncAttributesType.LINK = TeamSyncAttributesType("link")
TeamSyncAttributesType.PROVISION = TeamSyncAttributesType("provision")
