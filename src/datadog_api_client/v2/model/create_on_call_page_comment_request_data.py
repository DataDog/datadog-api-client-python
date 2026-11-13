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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_on_call_page_comment_request_attributes import (
        CreateOnCallPageCommentRequestAttributes,
    )
    from datadog_api_client.v2.model.on_call_page_comment_type import OnCallPageCommentType


class CreateOnCallPageCommentRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_on_call_page_comment_request_attributes import (
            CreateOnCallPageCommentRequestAttributes,
        )
        from datadog_api_client.v2.model.on_call_page_comment_type import OnCallPageCommentType

        return {
            "attributes": (CreateOnCallPageCommentRequestAttributes,),
            "id": (UUID,),
            "type": (OnCallPageCommentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CreateOnCallPageCommentRequestAttributes,
        type: OnCallPageCommentType,
        id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for creating a comment on an On-Call Page.

        :param attributes: Attributes for creating a comment on an On-Call Page.
        :type attributes: CreateOnCallPageCommentRequestAttributes

        :param id: A client-generated UUID that makes the request idempotent: retrying with the same ID
            does not create a duplicate comment. If omitted or not a valid UUID, a random one is generated.
        :type id: UUID, optional

        :param type: Indicates that the resource is of type ``comments``.
        :type type: OnCallPageCommentType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
