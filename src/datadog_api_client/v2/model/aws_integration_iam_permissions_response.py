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
    from datadog_api_client.v2.model.aws_integration_iam_permissions_response_data import (
        AWSIntegrationIamPermissionsResponseData,
    )


class AWSIntegrationIamPermissionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_integration_iam_permissions_response_data import (
            AWSIntegrationIamPermissionsResponseData,
        )

        return {
            "data": (AWSIntegrationIamPermissionsResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AWSIntegrationIamPermissionsResponseData, **kwargs):
        """
        AWS Integration IAM Permissions response body.

        :param data: AWS Integration IAM Permissions response data.
        :type data: AWSIntegrationIamPermissionsResponseData
        """
        super().__init__(kwargs)

        self_.data = data
