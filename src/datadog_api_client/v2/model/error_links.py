# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.error_links_about import ErrorLinksAbout
    from datadog_api_client.v2.model.link_object import LinkObject


class ErrorLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.error_links_about import ErrorLinksAbout

        return {
            "about": (ErrorLinksAbout,),
        }

    attribute_map = {
        "about": "about",
    }

    def __init__(self_, about: Union[ErrorLinksAbout, str, LinkObject], **kwargs):
        """


        :param about:
        :type about: ErrorLinksAbout
        """
        super().__init__(kwargs)

        self_.about = about
