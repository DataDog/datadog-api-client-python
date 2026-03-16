# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamSyncSelectionStateScope(ModelSimple):
    """
    The scope of the selection. When set to `subtree`,
        synchronization includes the referenced team or
        organization and everything nested under it.

    :param value: If omitted defaults to "subtree". Must be one of ["subtree"].
    :type value: str
    """

    allowed_values = {
        "subtree",
    }
    SUBTREE: ClassVar["TeamSyncSelectionStateScope"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamSyncSelectionStateScope.SUBTREE = TeamSyncSelectionStateScope("subtree")
