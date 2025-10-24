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


class ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ref": (str,),
        }

    attribute_map = {
        "ref": "ref",
    }

    def __init__(self_, ref: Union[str, UnsetType] = unset, **kwargs):
        """


        :param ref:
        :type ref: str, optional
        """
        if ref is not unset:
            kwargs["ref"] = ref
        super().__init__(kwargs)
