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
    from datadog_api_client.v2.model.disable_app_response_data_attributes import DisableAppResponseDataAttributes
    from datadog_api_client.v2.model.deployment_meta import DeploymentMeta
    from datadog_api_client.v2.model.disable_app_response_data_type import DisableAppResponseDataType


class DisableAppResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.disable_app_response_data_attributes import DisableAppResponseDataAttributes
        from datadog_api_client.v2.model.deployment_meta import DeploymentMeta
        from datadog_api_client.v2.model.disable_app_response_data_type import DisableAppResponseDataType

        return {
            "attributes": (DisableAppResponseDataAttributes,),
            "id": (str,),
            "meta": (DeploymentMeta,),
            "type": (DisableAppResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[DisableAppResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        meta: Union[DeploymentMeta, UnsetType] = unset,
        type: Union[DisableAppResponseDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``DisableAppResponseData`` object.

        :param attributes: The definition of ``DisableAppResponseDataAttributes`` object.
        :type attributes: DisableAppResponseDataAttributes, optional

        :param id: The ``data`` ``id``.
        :type id: str, optional

        :param meta: The definition of ``DeploymentMeta`` object.
        :type meta: DeploymentMeta, optional

        :param type: The definition of ``DisableAppResponseDataType`` object.
        :type type: DisableAppResponseDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if meta is not unset:
            kwargs["meta"] = meta
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
