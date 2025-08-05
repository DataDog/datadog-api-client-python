# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamSyncAttributesSource(ModelSimple):
    """
    The external source platform for team synchronization. Only "github" is supported.

    :param value: If omitted defaults to "github". Must be one of ["github"].
    :type value: str
    """

    allowed_values = {
        "github",
    }
    GITHUB: ClassVar["TeamSyncAttributesSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamSyncAttributesSource.GITHUB = TeamSyncAttributesSource("github")
