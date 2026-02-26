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
    from datadog_api_client.v2.model.aws_ccm_config_response_attributes import AWSCcmConfigResponseAttributes
    from datadog_api_client.v2.model.aws_ccm_config_type import AWSCcmConfigType


class AWSCcmConfigResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_ccm_config_response_attributes import AWSCcmConfigResponseAttributes
        from datadog_api_client.v2.model.aws_ccm_config_type import AWSCcmConfigType

        return {
            "attributes": (AWSCcmConfigResponseAttributes,),
            "id": (str,),
            "type": (AWSCcmConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: AWSCcmConfigType,
        attributes: Union[AWSCcmConfigResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS CCM Config response data.

        :param attributes: AWS CCM Config response attributes.
        :type attributes: AWSCcmConfigResponseAttributes, optional

        :param id: Unique Datadog ID of the AWS Account Integration Config.
            To get the config ID for an account, use the
            `List all AWS integrations <https://docs.datadoghq.com/api/latest/aws-integration/#list-all-aws-integrations>`_
            endpoint and query by AWS Account ID.
        :type id: str, optional

        :param type: AWS CCM Config resource type.
        :type type: AWSCcmConfigType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
