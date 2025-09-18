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
    from datadog_api_client.v2.model.aws_cur_config_response_data_attributes import AwsCurConfigResponseDataAttributes
    from datadog_api_client.v2.model.aws_cur_config_response_data_type import AwsCurConfigResponseDataType


class AwsCurConfigResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_cur_config_response_data_attributes import (
            AwsCurConfigResponseDataAttributes,
        )
        from datadog_api_client.v2.model.aws_cur_config_response_data_type import AwsCurConfigResponseDataType

        return {
            "attributes": (AwsCurConfigResponseDataAttributes,),
            "id": (str,),
            "type": (AwsCurConfigResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: AwsCurConfigResponseDataType,
        attributes: Union[AwsCurConfigResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``AwsCurConfigResponseData`` object.

        :param attributes: The definition of ``AwsCurConfigResponseDataAttributes`` object.
        :type attributes: AwsCurConfigResponseDataAttributes, optional

        :param id: The ``AwsCurConfigResponseData`` ``id``.
        :type id: str, optional

        :param type: AWS CUR config resource type.
        :type type: AwsCurConfigResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
