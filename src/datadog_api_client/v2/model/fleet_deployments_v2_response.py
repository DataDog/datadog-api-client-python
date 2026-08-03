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
    from datadog_api_client.v2.model.fleet_deployment_v2 import FleetDeploymentV2
    from datadog_api_client.v2.model.fleet_deployments_v2_response_meta import FleetDeploymentsV2ResponseMeta


class FleetDeploymentsV2Response(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_v2 import FleetDeploymentV2
        from datadog_api_client.v2.model.fleet_deployments_v2_response_meta import FleetDeploymentsV2ResponseMeta

        return {
            "data": ([FleetDeploymentV2],),
            "meta": (FleetDeploymentsV2ResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: List[FleetDeploymentV2], meta: Union[FleetDeploymentsV2ResponseMeta, UnsetType] = unset, **kwargs
    ):
        """
        Response containing a paginated list of deployments.

        :param data: Array of deployments matching the query criteria.
        :type data: [FleetDeploymentV2]

        :param meta: Metadata for the v2 list of deployments, including pagination information.
        :type meta: FleetDeploymentsV2ResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
