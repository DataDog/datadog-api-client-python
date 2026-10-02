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


class ExperimentsUpdateExposureSQLModelV2ResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "removed_property_names": ([str],),
            "removed_subject_type_ids": ([str],),
        }

    attribute_map = {
        "removed_property_names": "removed_property_names",
        "removed_subject_type_ids": "removed_subject_type_ids",
    }

    def __init__(
        self_,
        removed_property_names: Union[List[str], UnsetType] = unset,
        removed_subject_type_ids: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Removed model entries. Present only when the update removes an entry.

        :param removed_property_names: Property names removed from the model.
        :type removed_property_names: [str], optional

        :param removed_subject_type_ids: Subject type IDs removed from the model.
        :type removed_subject_type_ids: [str], optional
        """
        if removed_property_names is not unset:
            kwargs["removed_property_names"] = removed_property_names
        if removed_subject_type_ids is not unset:
            kwargs["removed_subject_type_ids"] = removed_subject_type_ids
        super().__init__(kwargs)
