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


class FleetAccessScopeFeatures(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "configure": (bool,),
            "install": (bool,),
            "upgrade": (bool,),
        }

    attribute_map = {
        "configure": "configure",
        "install": "install",
        "upgrade": "upgrade",
    }

    def __init__(
        self_,
        configure: Union[bool, UnsetType] = unset,
        install: Union[bool, UnsetType] = unset,
        upgrade: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Fleet actions authorized on agents matching the access scope query.

        :param configure: Whether the scope permits configuration changes.
        :type configure: bool, optional

        :param install: Whether the scope permits Agent installation.
        :type install: bool, optional

        :param upgrade: Whether the scope permits package upgrades.
        :type upgrade: bool, optional
        """
        if configure is not unset:
            kwargs["configure"] = configure
        if install is not unset:
            kwargs["install"] = install
        if upgrade is not unset:
            kwargs["upgrade"] = upgrade
        super().__init__(kwargs)
