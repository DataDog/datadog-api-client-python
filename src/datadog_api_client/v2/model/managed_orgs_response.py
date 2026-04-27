# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.managed_orgs_data import ManagedOrgsData
    from datadog_api_client.v2.model.org_data import OrgData


class ManagedOrgsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.managed_orgs_data import ManagedOrgsData
        from datadog_api_client.v2.model.org_data import OrgData

        return {
            "data": (ManagedOrgsData,),
            "included": ([OrgData],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(self_, data: ManagedOrgsData, included: List[OrgData], **kwargs):
        """
        Response containing the current organization and its managed organizations.

        :param data: The managed organizations resource.
        :type data: ManagedOrgsData

        :param included: Included organization resources.
        :type included: [OrgData]
        """
        super().__init__(kwargs)

        self_.data = data
        self_.included = included
