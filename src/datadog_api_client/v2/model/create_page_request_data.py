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
    from datadog_api_client.v2.model.create_page_request_data_attributes import CreatePageRequestDataAttributes
    from datadog_api_client.v2.model.create_page_request_data_type import CreatePageRequestDataType


class CreatePageRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_page_request_data_attributes import CreatePageRequestDataAttributes
        from datadog_api_client.v2.model.create_page_request_data_type import CreatePageRequestDataType

        return {
            "attributes": (CreatePageRequestDataAttributes,),
            "type": (CreatePageRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: CreatePageRequestDataType,
        attributes: Union[CreatePageRequestDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        The main request body, including attributes and resource type.

        :param attributes: Details about the On-Call Page you want to create.
        :type attributes: CreatePageRequestDataAttributes, optional

        :param type: The type of resource used when creating an On-Call Page.
        :type type: CreatePageRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
