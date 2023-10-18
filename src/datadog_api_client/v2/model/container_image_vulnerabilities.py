# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ContainerImageVulnerabilities(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "asset_id": (str,),
            "critical": (int,),
            "high": (int,),
            "low": (int,),
            "medium": (int,),
            "none": (int,),
            "unknown": (int,),
        }

    attribute_map = {
        "asset_id": "asset_id",
        "critical": "critical",
        "high": "high",
        "low": "low",
        "medium": "medium",
        "none": "none",
        "unknown": "unknown",
    }

    def __init__(
        self_,
        asset_id: Union[str, UnsetType] = unset,
        critical: Union[int, UnsetType] = unset,
        high: Union[int, UnsetType] = unset,
        low: Union[int, UnsetType] = unset,
        medium: Union[int, UnsetType] = unset,
        none: Union[int, UnsetType] = unset,
        unknown: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Vulnerability counts associated with the Container Image.

        :param asset_id: ID of the Container Image.
        :type asset_id: str, optional

        :param critical: Number of vulnerabilities with CVSS Critical severity.
        :type critical: int, optional

        :param high: Number of vulnerabilities with CVSS High severity.
        :type high: int, optional

        :param low: Number of vulnerabilities with CVSS Low severity.
        :type low: int, optional

        :param medium: Number of vulnerabilities with CVSS Medium severity.
        :type medium: int, optional

        :param none: Number of vulnerabilities with CVSS None severity.
        :type none: int, optional

        :param unknown: Number of vulnerabilities with an unknown CVSS severity.
        :type unknown: int, optional
        """
        if asset_id is not unset:
            kwargs["asset_id"] = asset_id
        if critical is not unset:
            kwargs["critical"] = critical
        if high is not unset:
            kwargs["high"] = high
        if low is not unset:
            kwargs["low"] = low
        if medium is not unset:
            kwargs["medium"] = medium
        if none is not unset:
            kwargs["none"] = none
        if unknown is not unset:
            kwargs["unknown"] = unknown
        super().__init__(kwargs)
