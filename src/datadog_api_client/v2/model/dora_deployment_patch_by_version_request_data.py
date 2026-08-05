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
    from datadog_api_client.v2.model.dora_deployment_patch_by_version_request_attributes import (
        DORADeploymentPatchByVersionRequestAttributes,
    )
    from datadog_api_client.v2.model.dora_deployment_patch_request_data_type import DORADeploymentPatchRequestDataType


class DORADeploymentPatchByVersionRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_deployment_patch_by_version_request_attributes import (
            DORADeploymentPatchByVersionRequestAttributes,
        )
        from datadog_api_client.v2.model.dora_deployment_patch_request_data_type import (
            DORADeploymentPatchRequestDataType,
        )

        return {
            "attributes": (DORADeploymentPatchByVersionRequestAttributes,),
            "type": (DORADeploymentPatchRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: DORADeploymentPatchByVersionRequestAttributes,
        type: DORADeploymentPatchRequestDataType,
        **kwargs,
    ):
        """
        The JSON:API data for patching a deployment identified by service, environment, and version.

        :param attributes: Attributes for patching a DORA deployment event identified by service, environment, and version.
        :type attributes: DORADeploymentPatchByVersionRequestAttributes

        :param type: JSON:API type for DORA deployment patch request.
        :type type: DORADeploymentPatchRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
