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
    from datadog_api_client.v2.model.aws_integration_iam_permissions_response_attributes import (
        AWSIntegrationIamPermissionsResponseAttributes,
    )
    from datadog_api_client.v2.model.aws_integration_iam_permissions_response_data_type import (
        AWSIntegrationIamPermissionsResponseDataType,
    )


class AWSIntegrationIamPermissionsResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_integration_iam_permissions_response_attributes import (
            AWSIntegrationIamPermissionsResponseAttributes,
        )
        from datadog_api_client.v2.model.aws_integration_iam_permissions_response_data_type import (
            AWSIntegrationIamPermissionsResponseDataType,
        )

        return {
            "attributes": (AWSIntegrationIamPermissionsResponseAttributes,),
            "id": (str,),
            "type": (AWSIntegrationIamPermissionsResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[AWSIntegrationIamPermissionsResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[AWSIntegrationIamPermissionsResponseDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS Integration IAM Permissions response data.

        :param attributes: AWS Integration IAM Permissions response attributes.
        :type attributes: AWSIntegrationIamPermissionsResponseAttributes, optional

        :param id: The ``AWSIntegrationIamPermissionsResponseData`` ``id``.
        :type id: str, optional

        :param type: The ``AWSIntegrationIamPermissionsResponseData`` ``type``.
        :type type: AWSIntegrationIamPermissionsResponseDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
