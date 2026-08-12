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
    from datadog_api_client.v2.model.dora_deployment_patch_by_version_remediation import (
        DORADeploymentPatchByVersionRemediation,
    )
    from datadog_api_client.v2.model.dora_deployment_patch_by_version_remediation_by_id import (
        DORADeploymentPatchByVersionRemediationByID,
    )
    from datadog_api_client.v2.model.dora_deployment_patch_by_version_remediation_by_version import (
        DORADeploymentPatchByVersionRemediationByVersion,
    )


class DORADeploymentPatchByVersionRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_deployment_patch_by_version_remediation import (
            DORADeploymentPatchByVersionRemediation,
        )

        return {
            "change_failure": (bool,),
            "env": (str,),
            "remediation": (DORADeploymentPatchByVersionRemediation,),
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
        remediation: Union[
            DORADeploymentPatchByVersionRemediation,
            DORADeploymentPatchByVersionRemediationByID,
            DORADeploymentPatchByVersionRemediationByVersion,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Attributes for patching a DORA deployment event identified by service, environment, and version.

        :param change_failure: Indicates whether the deployment resulted in a change failure.
        :type change_failure: bool

        :param env: The environment the deployment was performed in.
        :type env: str

        :param remediation: Remediation details for the deployment. Optional, but required to calculate failed deployment recovery time. Specify either ``id`` or ``version`` to identify the remediation deployment, but not both.
        :type remediation: DORADeploymentPatchByVersionRemediation, optional

        :param service: The name of the service that was deployed.
        :type service: str

        :param version: The version deployed. This can be seen in the Service Catalog or in the APM Deployment Tracking.
        :type version: str
        """
        if remediation is not unset:
            kwargs["remediation"] = remediation
        super().__init__(kwargs)

        self_.change_failure = change_failure
        self_.env = env
        self_.service = service
        self_.version = version
