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
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: Union[str, UnsetType] = unset,
        type: Union[DORADeploymentPatchRemediationType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Remediation details for the deployment. Optional, but required to calculate failed deployment recovery time.

        :param id: The ID of the remediation deployment. Required when the failed deployment must be linked to a remediation deployment.
        :type id: str, optional

        :param type: The type of remediation action taken. Required when the failed deployment must be linked to a remediation deployment.
        :type type: DORADeploymentPatchRemediationType, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
