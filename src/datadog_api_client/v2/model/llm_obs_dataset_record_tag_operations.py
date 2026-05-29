# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class LLMObsDatasetRecordTagOperations(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "add": ([str],),
            "remove": ([str],),
            "set": ([str],),
        }

    attribute_map = {
        "add": "add",
        "remove": "remove",
        "set": "set",
    }

    def __init__(
        self_,
        add: Union[List[str], UnsetType] = unset,
        remove: Union[List[str], UnsetType] = unset,
        set: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Explicit tag operations for updating records. Operations are applied in order, Remove then Add then Set. ``set`` is the final override; if specified, the result of ``remove`` and ``add`` is discarded.

        :param add: List of tag strings.
        :type add: [str], optional

        :param remove: List of tag strings.
        :type remove: [str], optional

        :param set: List of tag strings.
        :type set: [str], optional
        """
        if add is not unset:
            kwargs["add"] = add
        if remove is not unset:
            kwargs["remove"] = remove
        if set is not unset:
            kwargs["set"] = set
        super().__init__(kwargs)
