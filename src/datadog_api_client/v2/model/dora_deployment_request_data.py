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
    from datadog_api_client.v2.model.dora_deployment_request_attributes import DORADeploymentRequestAttributes


class DORADeploymentRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_deployment_request_attributes import DORADeploymentRequestAttributes

        return {
            "attributes": (DORADeploymentRequestAttributes,),
        }

    attribute_map = {
        "attributes": "attributes",
    }

    def __init__(self_, attributes: DORADeploymentRequestAttributes, **kwargs):
        """
        The JSON:API data.

        :param attributes: Attributes to create a DORA deployment event.
        :type attributes: DORADeploymentRequestAttributes
        """
        super().__init__(kwargs)

        self_.attributes = attributes
