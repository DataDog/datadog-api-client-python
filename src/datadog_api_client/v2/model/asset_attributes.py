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
    from datadog_api_client.v2.model.asset_operating_system import AssetOperatingSystem
    from datadog_api_client.v2.model.asset_risks import AssetRisks
    from datadog_api_client.v2.model.asset_type import AssetType
    from datadog_api_client.v2.model.asset_version import AssetVersion


class AssetAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.asset_operating_system import AssetOperatingSystem
        from datadog_api_client.v2.model.asset_risks import AssetRisks
        from datadog_api_client.v2.model.asset_type import AssetType
        from datadog_api_client.v2.model.asset_version import AssetVersion

        return {
            "arch": (str,),
            "environments": ([str],),
            "name": (str,),
            "operating_system": (AssetOperatingSystem,),
            "risks": (AssetRisks,),
            "teams": ([str],),
            "type": (AssetType,),
            "version": (AssetVersion,),
        }

    attribute_map = {
        "arch": "arch",
        "environments": "environments",
        "name": "name",
        "operating_system": "operating_system",
        "risks": "risks",
        "teams": "teams",
        "type": "type",
        "version": "version",
    }

    def __init__(
        self_,
        environments: List[str],
        name: str,
        risks: AssetRisks,
        type: AssetType,
        arch: Union[str, UnsetType] = unset,
        operating_system: Union[AssetOperatingSystem, UnsetType] = unset,
        teams: Union[List[str], UnsetType] = unset,
        version: Union[AssetVersion, UnsetType] = unset,
        **kwargs,
    ):
        """
        The JSON:API attributes of the asset.

        :param arch: Asset architecture.
        :type arch: str, optional

        :param environments: List of environments where the asset is deployed.
        :type environments: [str]

        :param name: Asset name.
        :type name: str

        :param operating_system: Asset operating system.
        :type operating_system: AssetOperatingSystem, optional

        :param risks: Asset risks.
        :type risks: AssetRisks

        :param teams: List of teams that own the asset.
        :type teams: [str], optional

        :param type: The asset type
        :type type: AssetType

        :param version: Asset version.
        :type version: AssetVersion, optional
        """
        if arch is not unset:
            kwargs["arch"] = arch
        if operating_system is not unset:
            kwargs["operating_system"] = operating_system
        if teams is not unset:
            kwargs["teams"] = teams
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.environments = environments
        self_.name = name
        self_.risks = risks
        self_.type = type
