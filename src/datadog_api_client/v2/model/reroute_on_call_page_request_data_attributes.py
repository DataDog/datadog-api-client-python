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
    from datadog_api_client.v2.model.create_page_request_data_attributes_target import (
        CreatePageRequestDataAttributesTarget,
    )


class RerouteOnCallPageRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_page_request_data_attributes_target import (
            CreatePageRequestDataAttributesTarget,
        )

        return {
            "comment": (str,),
            "target": (CreatePageRequestDataAttributesTarget,),
        }

    attribute_map = {
        "comment": "comment",
        "target": "target",
    }

    def __init__(
        self_, target: CreatePageRequestDataAttributesTarget, comment: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Details about where to reroute the On-Call Page.

        :param comment: An optional comment explaining why the page is being rerouted.
        :type comment: str, optional

        :param target: Information about the target to notify (such as a team or user).
        :type target: CreatePageRequestDataAttributesTarget
        """
        if comment is not unset:
            kwargs["comment"] = comment
        super().__init__(kwargs)

        self_.target = target
