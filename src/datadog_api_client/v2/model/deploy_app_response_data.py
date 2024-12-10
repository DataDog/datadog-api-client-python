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
    from datadog_api_client.v2.model.deploy_app_response_data_attributes import DeployAppResponseDataAttributes
    from datadog_api_client.v2.model.deployment_meta import DeploymentMeta
    from datadog_api_client.v2.model.deploy_app_response_data_type import DeployAppResponseDataType


class DeployAppResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deploy_app_response_data_attributes import DeployAppResponseDataAttributes
        from datadog_api_client.v2.model.deployment_meta import DeploymentMeta
        from datadog_api_client.v2.model.deploy_app_response_data_type import DeployAppResponseDataType

        return {
            "attributes": (DeployAppResponseDataAttributes,),
            "id": (str,),
            "meta": (DeploymentMeta,),
            "type": (DeployAppResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[DeployAppResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        meta: Union[DeploymentMeta, UnsetType] = unset,
        type: Union[DeployAppResponseDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``DeployAppResponseData`` object.

        :param attributes: The definition of ``DeployAppResponseDataAttributes`` object.
        :type attributes: DeployAppResponseDataAttributes, optional

        :param id: The ``data`` ``id``.
        :type id: str, optional

        :param meta: The definition of ``DeploymentMeta`` object.
        :type meta: DeploymentMeta, optional

        :param type: The definition of ``DeployAppResponseDataType`` object.
        :type type: DeployAppResponseDataType, optional
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
