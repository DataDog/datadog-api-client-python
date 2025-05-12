# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_page_request_data_attributes_target import (
        CreatePageRequestDataAttributesTarget,
    )
    from datadog_api_client.v2.model.page_urgency import PageUrgency


class CreatePageRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_page_request_data_attributes_target import (
            CreatePageRequestDataAttributesTarget,
        )
        from datadog_api_client.v2.model.page_urgency import PageUrgency

        return {
            "description": (str,),
            "tags": ([str],),
            "target": (CreatePageRequestDataAttributesTarget,),
            "title": (str,),
            "urgency": (PageUrgency,),
        }

    attribute_map = {
        "description": "description",
        "tags": "tags",
        "target": "target",
        "title": "title",
        "urgency": "urgency",
    }

    def __init__(
        self_,
        target: CreatePageRequestDataAttributesTarget,
        title: str,
        urgency: PageUrgency,
        description: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Details about the On-Call Page you want to create.

        :param description: A short summary of the issue or context.
        :type description: str, optional

        :param tags: Tags to help categorize or filter the page.
        :type tags: [str], optional

        :param target: Information about the target to notify (such as a team or user).
        :type target: CreatePageRequestDataAttributesTarget

        :param title: The title of the page.
        :type title: str

        :param urgency: On-Call Page urgency level.
        :type urgency: PageUrgency
        """
        if description is not unset:
            kwargs["description"] = description
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.target = target
        self_.title = title
        self_.urgency = urgency
