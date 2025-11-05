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
    from datadog_api_client.v2.model.fleet_deployment import FleetDeployment
    from datadog_api_client.v2.model.fleet_deployment_response_meta import FleetDeploymentResponseMeta


class FleetDeploymentResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment import FleetDeployment
        from datadog_api_client.v2.model.fleet_deployment_response_meta import FleetDeploymentResponseMeta

        return {
            "data": (FleetDeployment,),
            "meta": (FleetDeploymentResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[FleetDeployment, UnsetType] = unset,
        meta: Union[FleetDeploymentResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a single deployment.

        :param data: A deployment that defines automated configuration changes for a fleet of hosts.
        :type data: FleetDeployment, optional

        :param meta: Metadata for a single deployment response, including pagination information for hosts.
        :type meta: FleetDeploymentResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
