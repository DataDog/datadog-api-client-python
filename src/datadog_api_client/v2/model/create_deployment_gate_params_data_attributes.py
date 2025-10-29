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


class CreateDeploymentGateParamsDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "dry_run": (bool,),
            "env": (str,),
            "identifier": (str,),
            "service": (str,),
        }

    attribute_map = {
        "dry_run": "dry_run",
        "env": "env",
        "identifier": "identifier",
        "service": "service",
    }

    def __init__(
        self_,
        env: str,
        service: str,
        dry_run: Union[bool, UnsetType] = unset,
        identifier: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Parameters for creating a deployment gate.

        :param dry_run: Whether this gate is run in dry-run mode.
        :type dry_run: bool, optional

        :param env: The environment of the deployment gate.
        :type env: str

        :param identifier: The identifier of the deployment gate.
        :type identifier: str, optional

        :param service: The service of the deployment gate.
        :type service: str
        """
        if dry_run is not unset:
            kwargs["dry_run"] = dry_run
        if identifier is not unset:
            kwargs["identifier"] = identifier
        super().__init__(kwargs)

        self_.env = env
        self_.service = service
