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


class SegmentTemplateBlock(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_from": (str,),
            "name": (str,),
            "parameters": (
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
            "template_id": (str,),
            "to": (str,),
        }

    attribute_map = {
        "_from": "from",
        "name": "name",
        "parameters": "parameters",
        "template_id": "template_id",
        "to": "to",
    }

    def __init__(
        self_,
        parameters: Dict[str, Any],
        template_id: str,
        _from: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        to: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Selects users or accounts with a segment template.

        :param _from: Start of the time range, in epoch milliseconds.
        :type _from: str, optional

        :param name: Name of the block, used in ``combination``.
        :type name: str, optional

        :param parameters: Template parameter values, keyed by parameter name.
        :type parameters: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}

        :param template_id: ID of the segment template, such as ``time-spent-v1``.
        :type template_id: str

        :param to: End of the time range, in epoch milliseconds.
        :type to: str, optional
        """
        if _from is not unset:
            kwargs["_from"] = _from
        if name is not unset:
            kwargs["name"] = name
        if to is not unset:
            kwargs["to"] = to
        super().__init__(kwargs)

        self_.parameters = parameters
        self_.template_id = template_id
