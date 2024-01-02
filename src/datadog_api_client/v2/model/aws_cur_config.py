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
    from datadog_api_client.v2.model.aws_cur_config_attributes import AwsCURConfigAttributes
    from datadog_api_client.v2.model.aws_cur_config_type import AwsCURConfigType


class AwsCURConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_cur_config_attributes import AwsCURConfigAttributes
        from datadog_api_client.v2.model.aws_cur_config_type import AwsCURConfigType

        return {
            "attributes": (AwsCURConfigAttributes,),
            "id": (int,),
            "type": (AwsCURConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AwsCURConfigAttributes, type: AwsCURConfigType, id: Union[int, UnsetType] = unset, **kwargs
    ):
        """
        AWS CUR config.

        :param attributes: Attributes for An AWS CUR config.
        :type attributes: AwsCURConfigAttributes

        :param id: The ID of the AWS CUR config.
        :type id: int, optional

        :param type: Type of AWS CUR config.
        :type type: AwsCURConfigType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
