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
    from datadog_api_client.v2.model.aws_namespaces_response_attributes import AWSNamespacesResponseAttributes
    from datadog_api_client.v2.model.aws_namespaces_response_data_type import AWSNamespacesResponseDataType


class AWSNamespacesResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_namespaces_response_attributes import AWSNamespacesResponseAttributes
        from datadog_api_client.v2.model.aws_namespaces_response_data_type import AWSNamespacesResponseDataType

        return {
            "attributes": (AWSNamespacesResponseAttributes,),
            "id": (str,),
            "type": (AWSNamespacesResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: AWSNamespacesResponseDataType,
        attributes: Union[AWSNamespacesResponseAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS Namespaces response data.

        :param attributes: AWS Namespaces response attributes.
        :type attributes: AWSNamespacesResponseAttributes, optional

        :param id: The ``AWSNamespacesResponseData`` ``id``.
        :type id: str

        :param type: The ``AWSNamespacesResponseData`` ``type``.
        :type type: AWSNamespacesResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)
        id = kwargs.get("id", "namespaces")

        self_.id = id
        self_.type = type
