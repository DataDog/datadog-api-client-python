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
    from datadog_api_client.v2.model.deleted_suites_request_delete_attributes import (
        DeletedSuitesRequestDeleteAttributes,
    )
    from datadog_api_client.v2.model.deleted_suites_request_type import DeletedSuitesRequestType


class DeletedSuitesRequestDelete(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deleted_suites_request_delete_attributes import (
            DeletedSuitesRequestDeleteAttributes,
        )
        from datadog_api_client.v2.model.deleted_suites_request_type import DeletedSuitesRequestType

        return {
            "attributes": (DeletedSuitesRequestDeleteAttributes,),
            "id": (str,),
            "type": (DeletedSuitesRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: DeletedSuitesRequestDeleteAttributes,
        id: Union[str, UnsetType] = unset,
        type: Union[DeletedSuitesRequestType, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: DeletedSuitesRequestDeleteAttributes

        :param id:
        :type id: str, optional

        :param type:
        :type type: DeletedSuitesRequestType, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.attributes = attributes
