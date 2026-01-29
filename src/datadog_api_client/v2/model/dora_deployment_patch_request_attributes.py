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


class DORADeploymentPatchRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_deployment_patch_remediation import DORADeploymentPatchRemediation

        return {
            "change_failure": (bool,),
            "remediation": (DORADeploymentPatchRemediation,),
        }

    attribute_map = {
        "change_failure": "change_failure",
        "remediation": "remediation",
    }

    def __init__(
        self_,
        change_failure: Union[bool, UnsetType] = unset,
        remediation: Union[DORADeploymentPatchRemediation, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for patching a DORA deployment event.

        :param change_failure: Indicates whether the deployment resulted in a change failure.
        :type change_failure: bool, optional

        :param remediation: Remediation details for the deployment.
        :type remediation: DORADeploymentPatchRemediation, optional
        """
        if change_failure is not unset:
            kwargs["change_failure"] = change_failure
        if remediation is not unset:
            kwargs["remediation"] = remediation
        super().__init__(kwargs)
