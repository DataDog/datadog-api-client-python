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
    from datadog_api_client.v2.model.rum_sdk_config_attributes import RUMSdkConfigAttributes
    from datadog_api_client.v2.model.rum_sdk_config_meta import RUMSdkConfigMeta
    from datadog_api_client.v2.model.rum_sdk_config_type import RUMSdkConfigType


class RUMSdkConfigData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_sdk_config_attributes import RUMSdkConfigAttributes
        from datadog_api_client.v2.model.rum_sdk_config_meta import RUMSdkConfigMeta
        from datadog_api_client.v2.model.rum_sdk_config_type import RUMSdkConfigType

        return {
            "attributes": (RUMSdkConfigAttributes,),
            "id": (str,),
            "meta": (RUMSdkConfigMeta,),
            "type": (RUMSdkConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: RUMSdkConfigAttributes,
        id: str,
        type: RUMSdkConfigType,
        meta: Union[RUMSdkConfigMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        The RUM SDK configuration data object.

        :param attributes: Attributes of the RUM SDK configuration.
        :type attributes: RUMSdkConfigAttributes

        :param id: The unique identifier of the RUM SDK configuration.
        :type id: str

        :param meta: Metadata associated with a RUM SDK configuration.
        :type meta: RUMSdkConfigMeta, optional

        :param type: The type of the resource. The value should always be ``rum_sdk_config``.
        :type type: RUMSdkConfigType
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
