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
    from datadog_api_client.v2.model.attachment_data import AttachmentData
    from datadog_api_client.v2.model.attachment_included import AttachmentIncluded
    from datadog_api_client.v2.model.user140420082644000 import User140420082644000


class AttachmentArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.attachment_data import AttachmentData
        from datadog_api_client.v2.model.attachment_included import AttachmentIncluded

        return {
            "data": ([AttachmentData],),
            "included": ([AttachmentIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: List[AttachmentData],
        included: Union[List[Union[AttachmentIncluded, User140420082644000]], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param data:
        :type data: [AttachmentData]

        :param included:
        :type included: [AttachmentIncluded], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
