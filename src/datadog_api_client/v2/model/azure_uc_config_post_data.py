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
    from datadog_api_client.v2.model.azure_uc_config_post_request_attributes import AzureUCConfigPostRequestAttributes
    from datadog_api_client.v2.model.azure_uc_config_post_request_type import AzureUCConfigPostRequestType


class AzureUCConfigPostData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.azure_uc_config_post_request_attributes import (
            AzureUCConfigPostRequestAttributes,
        )
        from datadog_api_client.v2.model.azure_uc_config_post_request_type import AzureUCConfigPostRequestType

        return {
            "attributes": (AzureUCConfigPostRequestAttributes,),
            "type": (AzureUCConfigPostRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: AzureUCConfigPostRequestType,
        attributes: Union[AzureUCConfigPostRequestAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Azure config Post data.

        :param attributes: Attributes for Azure config Post Request.
        :type attributes: AzureUCConfigPostRequestAttributes, optional

        :param type: Type of Azure config Post Request.
        :type type: AzureUCConfigPostRequestType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
