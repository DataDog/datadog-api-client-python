# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.remediation_group_owner_list import RemediationGroupOwnerList


class RemediationGroupOwners(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_group_owner_list import RemediationGroupOwnerList

        return {
            "codeowners": (RemediationGroupOwnerList,),
            "teams": (RemediationGroupOwnerList,),
        }

    attribute_map = {
        "codeowners": "codeowners",
        "teams": "teams",
    }

    def __init__(self_, codeowners: RemediationGroupOwnerList, teams: RemediationGroupOwnerList, **kwargs):
        """
        Who should fix the group: the code owners of the group's findings, from their ``@git.codeowners`` attribute,
        and their Datadog teams, from their ``team`` tag. A group with no owners has empty ``items`` and a ``total`` of 0.

        :param codeowners: Owners of the group's open findings. ``items`` lists at most 5 owners, the owners of the most findings first,
            then by name. ``total`` counts every distinct owner, so the list is cut when ``total`` is larger than the number
            of items.
        :type codeowners: RemediationGroupOwnerList

        :param teams: Owners of the group's open findings. ``items`` lists at most 5 owners, the owners of the most findings first,
            then by name. ``total`` counts every distinct owner, so the list is cut when ``total`` is larger than the number
            of items.
        :type teams: RemediationGroupOwnerList
        """
        super().__init__(kwargs)

        self_.codeowners = codeowners
        self_.teams = teams
