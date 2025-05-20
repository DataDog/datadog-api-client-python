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
    from datadog_api_client.v2.model.resource_filter_attributes import ResourceFilterAttributes
    from datadog_api_client.v2.model.resource_filter_request_type import ResourceFilterRequestType


class UpdateResourceEvaluationFiltersResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.resource_filter_attributes import ResourceFilterAttributes
        from datadog_api_client.v2.model.resource_filter_request_type import ResourceFilterRequestType

        return {
            "attributes": (ResourceFilterAttributes,),
            "id": (str,),
            "type": (ResourceFilterRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ResourceFilterAttributes,
        type: ResourceFilterRequestType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``UpdateResourceFilterResponseData`` object.

        :param attributes: Attributes of a resource filter.
        :type attributes: ResourceFilterAttributes

        :param id: The ``data`` ``id``.
        :type id: str, optional

        :param type: Constant string to identify the request type.
        :type type: ResourceFilterRequestType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
