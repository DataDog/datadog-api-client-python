# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fleet_deployments_v2_page import FleetDeploymentsV2Page


class FleetDeploymentsV2ResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployments_v2_page import FleetDeploymentsV2Page

        return {
            "page": (FleetDeploymentsV2Page,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: Union[FleetDeploymentsV2Page, UnsetType] = unset, **kwargs):
        """
        Metadata for the v2 list of deployments, including pagination information.

        :param page: Pagination details for the v2 list of deployments.
        :type page: FleetDeploymentsV2Page, optional
        """
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)
