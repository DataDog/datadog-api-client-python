# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsTestsItems(ModelNormal):
    validations = {
        "annotation_count": {
            "inclusive_maximum": 65535,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "annotation_count": (int,),
            "code": (str,),
            "filename": (str,),
        }

    attribute_map = {
        "annotation_count": "annotation_count",
        "code": "code",
        "filename": "filename",
    }

    def __init__(
        self_,
        annotation_count: Union[int, UnsetType] = unset,
        code: Union[str, UnsetType] = unset,
        filename: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param annotation_count:
        :type annotation_count: int, optional

        :param code:
        :type code: str, optional

        :param filename:
        :type filename: str, optional
        """
        if annotation_count is not unset:
            kwargs["annotation_count"] = annotation_count
        if code is not unset:
            kwargs["code"] = code
        if filename is not unset:
            kwargs["filename"] = filename
        super().__init__(kwargs)
