# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dora_deployment_patch_remediation_type import DORADeploymentPatchRemediationType


class DORADeploymentPatchByVersionRemediationByID(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

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

    def __init__(self_, id: str, type: DORADeploymentPatchRemediationType, **kwargs):
        """
        Remediation details identified by the ID of the remediation deployment.

        :param id: The ID of the remediation deployment.
        :type id: str

        :param type: The type of remediation action taken. Required when the failed deployment must be linked to a remediation deployment.
        :type type: DORADeploymentPatchRemediationType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
