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


class SampleLogGenerationBulkSubscriptionItemMeta(ModelNormal):
    validations = {
        "status": {
            "inclusive_maximum": 599,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "error": (str,),
            "status": (int,),
        }

    attribute_map = {
        "error": "error",
        "status": "status",
    }

    def __init__(self_, status: int, error: Union[str, UnsetType] = unset, **kwargs):
        """
        Per-item status returned for a bulk subscription request.

        :param error: A description of the error encountered for this content pack, if the subscription could not be created.
        :type error: str, optional

        :param status: The HTTP status code that resulted from creating the subscription for this content pack.
        :type status: int
        """
        if error is not unset:
            kwargs["error"] = error
        super().__init__(kwargs)

        self_.status = status
