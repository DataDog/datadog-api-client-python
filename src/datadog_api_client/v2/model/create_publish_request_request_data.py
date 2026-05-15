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
    from datadog_api_client.v2.model.create_publish_request_request_data_attributes import (
        CreatePublishRequestRequestDataAttributes,
    )
    from datadog_api_client.v2.model.publish_request_type import PublishRequestType


class CreatePublishRequestRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_publish_request_request_data_attributes import (
            CreatePublishRequestRequestDataAttributes,
        )
        from datadog_api_client.v2.model.publish_request_type import PublishRequestType

        return {
            "attributes": (CreatePublishRequestRequestDataAttributes,),
            "type": (PublishRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[CreatePublishRequestRequestDataAttributes, UnsetType] = unset,
        type: Union[PublishRequestType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for creating a publish request.

        :param attributes: Attributes for creating a publish request.
        :type attributes: CreatePublishRequestRequestDataAttributes, optional

        :param type: The publish-request resource type.
        :type type: PublishRequestType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
