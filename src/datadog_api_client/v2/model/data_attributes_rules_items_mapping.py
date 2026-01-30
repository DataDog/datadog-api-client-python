# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.data_attributes_rules_items_if_tag_exists import (
        DataAttributesRulesItemsIfTagExists,
    )


class DataAttributesRulesItemsMapping(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.data_attributes_rules_items_if_tag_exists import (
            DataAttributesRulesItemsIfTagExists,
        )

        return {
            "destination_key": (str,),
            "if_not_exists": (bool,),
            "if_tag_exists": (DataAttributesRulesItemsIfTagExists,),
            "source_keys": ([str],),
        }

    attribute_map = {
        "destination_key": "destination_key",
        "if_not_exists": "if_not_exists",
        "if_tag_exists": "if_tag_exists",
        "source_keys": "source_keys",
    }

    def __init__(
        self_,
        destination_key: str,
        source_keys: List[str],
        if_not_exists: Union[bool, UnsetType] = unset,
        if_tag_exists: Union[DataAttributesRulesItemsIfTagExists, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``DataAttributesRulesItemsMapping`` object.

        :param destination_key: The ``mapping`` ``destination_key``.
        :type destination_key: str

        :param if_not_exists: Deprecated. Use ``if_tag_exists`` instead. The ``mapping`` ``if_not_exists``. **Deprecated**.
        :type if_not_exists: bool, optional

        :param if_tag_exists: The behavior when the tag already exists.
        :type if_tag_exists: DataAttributesRulesItemsIfTagExists, optional

        :param source_keys: The ``mapping`` ``source_keys``.
        :type source_keys: [str]
        """
        if if_not_exists is not unset:
            kwargs["if_not_exists"] = if_not_exists
        if if_tag_exists is not unset:
            kwargs["if_tag_exists"] = if_tag_exists
        super().__init__(kwargs)

        self_.destination_key = destination_key
        self_.source_keys = source_keys
