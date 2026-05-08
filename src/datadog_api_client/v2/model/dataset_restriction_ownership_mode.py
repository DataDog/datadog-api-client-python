# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DatasetRestrictionOwnershipMode(ModelSimple):
    """
    Controls how dataset ownership is determined. `disabled` turns off ownership-based access
        entirely. `team_tag_based` assigns dataset ownership based on the team tags applied to the
        data, allowing team members to see their own team's datasets.

    :param value: Must be one of ["disabled", "team_tag_based"].
    :type value: str
    """

    allowed_values = {
        "disabled",
        "team_tag_based",
    }
    DISABLED: ClassVar["DatasetRestrictionOwnershipMode"]
    TEAM_TAG_BASED: ClassVar["DatasetRestrictionOwnershipMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DatasetRestrictionOwnershipMode.DISABLED = DatasetRestrictionOwnershipMode("disabled")
DatasetRestrictionOwnershipMode.TEAM_TAG_BASED = DatasetRestrictionOwnershipMode("team_tag_based")
