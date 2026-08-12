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
    from datadog_api_client.v2.model.dora_deployment_patch_remediation_type import DORADeploymentPatchRemediationType


class DORADeploymentPatchRemediation(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_deployment_patch_remediation_type import (
            DORADeploymentPatchRemediationType,
        )

        return {
            "id": (str,),
            "type": (DORADeploymentPatchRemediationType,),
            "version": (str,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
        "version": "version",
    }

    def __init__(
        self_,
        id: Union[str, UnsetType] = unset,
        type: Union[DORADeploymentPatchRemediationType, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Remediation details for the deployment. Optional, but required to calculate failed deployment recovery time. Specify either ``id`` or ``version`` to identify the remediation deployment, but not both.

        :param id: The ID of the remediation deployment. Use this or ``version`` to identify the remediation deployment, but not both.
        :type id: str, optional

        :param type: The type of remediation action taken. Required when the failed deployment must be linked to a remediation deployment.
        :type type: DORADeploymentPatchRemediationType, optional

        :param version: The version of the remediation deployment, matched against the same service and environment as the failed deployment. Use this or ``id`` to identify the remediation deployment, but not both.
        :type version: str, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
