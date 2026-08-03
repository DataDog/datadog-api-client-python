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
    from datadog_api_client.v2.model.fleet_deployment_configure_v2_dry_run_result import (
        FleetDeploymentConfigureV2DryRunResult,
    )


class FleetDeploymentConfigureV2DryRunAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_configure_v2_dry_run_result import (
            FleetDeploymentConfigureV2DryRunResult,
        )

        return {
            "dry_run": (FleetDeploymentConfigureV2DryRunResult,),
            "query": (str,),
            "total_hosts": (int,),
        }

    attribute_map = {
        "dry_run": "dry_run",
        "query": "query",
        "total_hosts": "total_hosts",
    }

    def __init__(
        self_,
        dry_run: Union[FleetDeploymentConfigureV2DryRunResult, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        total_hosts: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a configuration deployment dry-run response.

        :param dry_run: Validation result of a configuration deployment dry run.
        :type dry_run: FleetDeploymentConfigureV2DryRunResult, optional

        :param query: Query used to filter and select target hosts for the deployment.
        :type query: str, optional

        :param total_hosts: Total number of hosts targeted by the dry run.
        :type total_hosts: int, optional
        """
        if dry_run is not unset:
            kwargs["dry_run"] = dry_run
        if query is not unset:
            kwargs["query"] = query
        if total_hosts is not unset:
            kwargs["total_hosts"] = total_hosts
        super().__init__(kwargs)
