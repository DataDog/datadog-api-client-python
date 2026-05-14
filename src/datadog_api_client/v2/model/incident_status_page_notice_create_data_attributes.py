# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IncidentStatusPageNoticeCreateDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "components": ({str: (str,)},),
            "message": (str,),
            "status": (str,),
            "title": (str,),
        }

    attribute_map = {
        "components": "components",
        "message": "message",
        "status": "status",
        "title": "title",
    }

    def __init__(
        self_,
        components: Union[Dict[str, str], UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for publishing a status page notice.

        :param components: Map of component identifiers to their status.
        :type components: {str: (str,)}, optional

        :param message: The message body of the notice.
        :type message: str, optional

        :param status: The status of the notice.
        :type status: str, optional

        :param title: The title of the notice.
        :type title: str, optional
        """
        if components is not unset:
            kwargs["components"] = components
        if message is not unset:
            kwargs["message"] = message
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
