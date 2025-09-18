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
    from datadog_api_client.v2.model.aws_cur_config_post_request_attributes import AwsCURConfigPostRequestAttributes
    from datadog_api_client.v2.model.aws_cur_config_post_request_type import AwsCURConfigPostRequestType


class AwsCURConfigPostData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_cur_config_post_request_attributes import AwsCURConfigPostRequestAttributes
        from datadog_api_client.v2.model.aws_cur_config_post_request_type import AwsCURConfigPostRequestType

        return {
            "attributes": (AwsCURConfigPostRequestAttributes,),
            "type": (AwsCURConfigPostRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: AwsCURConfigPostRequestType,
        attributes: Union[AwsCURConfigPostRequestAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS CUR config Post data.

        :param attributes: Attributes for AWS CUR config Post Request.
        :type attributes: AwsCURConfigPostRequestAttributes, optional

        :param type: Type of AWS CUR config Post Request.
        :type type: AwsCURConfigPostRequestType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
