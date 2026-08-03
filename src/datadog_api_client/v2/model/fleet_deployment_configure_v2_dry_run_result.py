# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class FleetDeploymentConfigureV2DryRunResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "config_validated": (bool,),
            "non_upgradable_by_reason": ({str: (int,)},),
            "non_upgradable_hosts": (int,),
        }

    attribute_map = {
        "config_validated": "config_validated",
        "non_upgradable_by_reason": "non_upgradable_by_reason",
        "non_upgradable_hosts": "non_upgradable_hosts",
    }

    def __init__(
        self_,
        config_validated: Union[bool, UnsetType] = unset,
        non_upgradable_by_reason: Union[Dict[str, int], UnsetType] = unset,
        non_upgradable_hosts: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Validation result of a configuration deployment dry run.

        :param config_validated: Whether the configuration passed schema validation.
        :type config_validated: bool, optional

        :param non_upgradable_by_reason: Breakdown of ineligible host counts by reason. Only includes reasons with a
            non-zero count. Absent from the response when no targeted host is ineligible.
        :type non_upgradable_by_reason: {str: (int,)}, optional

        :param non_upgradable_hosts: Number of targeted hosts that are not eligible to receive this configuration.
        :type non_upgradable_hosts: int, optional
        """
        if config_validated is not unset:
            kwargs["config_validated"] = config_validated
        if non_upgradable_by_reason is not unset:
            kwargs["non_upgradable_by_reason"] = non_upgradable_by_reason
        if non_upgradable_hosts is not unset:
            kwargs["non_upgradable_hosts"] = non_upgradable_hosts
        super().__init__(kwargs)
