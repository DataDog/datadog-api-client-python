# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fleet_deployment import FleetDeployment
    from datadog_api_client.v2.model.fleet_deployments_response_meta import FleetDeploymentsResponseMeta


class FleetDeploymentsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment import FleetDeployment
        from datadog_api_client.v2.model.fleet_deployments_response_meta import FleetDeploymentsResponseMeta

        return {
            "data": ([FleetDeployment],),
            "meta": (FleetDeploymentsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: List[FleetDeployment], meta: Union[FleetDeploymentsResponseMeta, UnsetType] = unset, **kwargs
    ):
        """
        Response containing a paginated list of deployments.

        :param data: Array of deployments matching the query criteria.
        :type data: [FleetDeployment]

        :param meta: Metadata for the list of deployments, including pagination information.
        :type meta: FleetDeploymentsResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
