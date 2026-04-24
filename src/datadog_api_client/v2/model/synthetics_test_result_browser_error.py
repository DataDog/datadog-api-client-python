# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class SyntheticsTestResultBrowserError(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "method": (str,),
            "name": (str,),
            "status": (int,),
            "type": (str,),
            "url": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
        }

    attribute_map = {
        "description": "description",
        "method": "method",
        "name": "name",
        "status": "status",
        "type": "type",
        "url": "url",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        method: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        status: Union[int, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        url: Union[Dict[str, Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        A browser error captured during a browser test step.

        :param description: Error description.
        :type description: str, optional

        :param method: HTTP method associated with the error (for network errors).
        :type method: str, optional

        :param name: Error name.
        :type name: str, optional

        :param status: HTTP status code associated with the error (for network errors).
        :type status: int, optional

        :param type: Type of the browser error.
        :type type: str, optional

        :param url: URL associated with the error.
        :type url: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if method is not unset:
            kwargs["method"] = method
        if name is not unset:
            kwargs["name"] = name
        if status is not unset:
            kwargs["status"] = status
        if type is not unset:
            kwargs["type"] = type
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
