# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


class CreateOnCallPageCommentRequestAttributes(ModelNormal):
    validations = {
        "body": {
            "max_length": 20000,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "body": (str,),
            "mentioned_user_ids": ([UUID],),
        }

    attribute_map = {
        "body": "body",
        "mentioned_user_ids": "mentioned_user_ids",
    }

    def __init__(self_, body: str, mentioned_user_ids: Union[List[UUID], UnsetType] = unset, **kwargs):
        """
        Attributes for creating a comment on an On-Call Page.

        :param body: The content of the comment.
        :type body: str

        :param mentioned_user_ids: The IDs of the users mentioned in the comment.
        :type mentioned_user_ids: [UUID], optional
        """
        if mentioned_user_ids is not unset:
            kwargs["mentioned_user_ids"] = mentioned_user_ids
        super().__init__(kwargs)

        self_.body = body
