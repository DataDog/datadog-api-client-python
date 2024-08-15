# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class LeakedKeyAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "date": (datetime,),
            "leak_source": (str,),
        }

    attribute_map = {
        "date": "date",
        "leak_source": "leak_source",
    }

    def __init__(self_, date: datetime, leak_source: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of LeakedKeyAttributes object.

        :param date: The LeakedKeyAttributes date.
        :type date: datetime

        :param leak_source: The LeakedKeyAttributes leak_source.
        :type leak_source: str, optional
        """
        if leak_source is not unset:
            kwargs["leak_source"] = leak_source
        super().__init__(kwargs)

        self_.date = date
