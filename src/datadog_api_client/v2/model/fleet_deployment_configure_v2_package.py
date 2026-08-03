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


class FleetDeploymentConfigureV2Package(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "apm_instrumentation": (str,),
            "name": (str,),
            "version": (str,),
        }

    attribute_map = {
        "apm_instrumentation": "apm_instrumentation",
        "name": "name",
        "version": "version",
    }

    def __init__(self_, name: str, version: str, apm_instrumentation: Union[str, UnsetType] = unset, **kwargs):
        """
        A package and its target version to additionally deploy alongside a configuration change.

        :param apm_instrumentation: APM auto-instrumentation mode to enable for this package, if applicable.
        :type apm_instrumentation: str, optional

        :param name: The name of the package to deploy.
        :type name: str

        :param version: The target version of the package to deploy.
        :type version: str
        """
        if apm_instrumentation is not unset:
            kwargs["apm_instrumentation"] = apm_instrumentation
        super().__init__(kwargs)

        self_.name = name
        self_.version = version
