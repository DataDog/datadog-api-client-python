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
    from datadog_api_client.v2.model.deployment_included_attributes import DeploymentIncludedAttributes
    from datadog_api_client.v2.model.deployment_included_meta import DeploymentIncludedMeta
    from datadog_api_client.v2.model.deployment_included_type import DeploymentIncludedType


class DeploymentIncluded(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_included_attributes import DeploymentIncludedAttributes
        from datadog_api_client.v2.model.deployment_included_meta import DeploymentIncludedMeta
        from datadog_api_client.v2.model.deployment_included_type import DeploymentIncludedType

        return {
            "attributes": (DeploymentIncludedAttributes,),
            "id": (str,),
            "meta": (DeploymentIncludedMeta,),
            "type": (DeploymentIncludedType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[DeploymentIncludedAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        meta: Union[DeploymentIncludedMeta, UnsetType] = unset,
        type: Union[DeploymentIncludedType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``DeploymentIncluded`` object.

        :param attributes: The definition of ``DeploymentIncludedAttributes`` object.
        :type attributes: DeploymentIncludedAttributes, optional

        :param id: The ``DeploymentIncluded`` ``id``.
        :type id: str, optional

        :param meta: The definition of ``DeploymentIncludedMeta`` object.
        :type meta: DeploymentIncludedMeta, optional

        :param type: The definition of ``DeploymentIncludedType`` object.
        :type type: DeploymentIncludedType, optional
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
