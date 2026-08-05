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
    from datadog_api_client.v2.model.dora_deployment_patch_remediation import DORADeploymentPatchRemediation


class DORADeploymentPatchByVersionRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_deployment_patch_remediation import DORADeploymentPatchRemediation

        return {
            "change_failure": (bool,),
            "env": (str,),
            "remediation": (DORADeploymentPatchRemediation,),
            "service": (str,),
            "version": (str,),
        }

    attribute_map = {
        "change_failure": "change_failure",
        "env": "env",
        "remediation": "remediation",
        "service": "service",
        "version": "version",
    }

    def __init__(
        self_,
        change_failure: bool,
        env: str,
        service: str,
        version: str,
        remediation: Union[DORADeploymentPatchRemediation, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for patching a DORA deployment event identified by service, environment, and version.

        :param change_failure: Indicates whether the deployment resulted in a change failure.
        :type change_failure: bool

        :param env: The environment the deployment was performed in.
        :type env: str

        :param remediation: Remediation details for the deployment. Optional, but required to calculate failed deployment recovery time.
        :type remediation: DORADeploymentPatchRemediation, optional

        :param service: The name of the service that was deployed.
        :type service: str

        :param version: The version deployed. This is the same version used to correlate with `APM Deployment Tracking <https://docs.datadoghq.com/tracing/services/deployment_tracking/>`_.
        :type version: str
        """
        if remediation is not unset:
            kwargs["remediation"] = remediation
        super().__init__(kwargs)

        self_.change_failure = change_failure
        self_.env = env
        self_.service = service
        self_.version = version
