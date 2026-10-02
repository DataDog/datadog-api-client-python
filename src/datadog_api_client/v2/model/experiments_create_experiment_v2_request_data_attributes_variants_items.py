# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class ExperimentsCreateExperimentV2RequestDataAttributesVariantsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "feature_flag_variant_id": (UUID,),
            "is_active": (bool,),
            "is_control": (bool,),
            "key": (str,),
            "name": (str, none_type),
            "weight": (float,),
        }

    attribute_map = {
        "feature_flag_variant_id": "feature_flag_variant_id",
        "is_active": "is_active",
        "is_control": "is_control",
        "key": "key",
        "name": "name",
        "weight": "weight",
    }

    def __init__(
        self_,
        is_control: bool,
        key: str,
        weight: float,
        feature_flag_variant_id: Union[UUID, UnsetType] = unset,
        is_active: Union[bool, UnsetType] = unset,
        name: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Variant selected for an experiment, with its identity and traffic allocation.

        :param feature_flag_variant_id: Stable backing flag variant ID. Required for Datadog-backed experiments and omitted for Warehouse-only experiments.
        :type feature_flag_variant_id: UUID, optional

        :param is_active: Whether this variant participates in the experiment. Responses always include this field. On writes an included variant defaults to active; omit its row to remove or unselect it. Explicit false supports sending an unchanged response back.
        :type is_active: bool, optional

        :param is_control: Whether this is the single control variant.
        :type is_control: bool

        :param key: Assignment value. Datadog flag variant keys are server-owned.
        :type key: str

        :param name: Display name. Datadog flag variant names are server-owned.
        :type name: str, none_type, optional

        :param weight: Traffic allocation percentage. Existing variant weights cannot change through the public API after the experiment starts.
        :type weight: float
        """
        if feature_flag_variant_id is not unset:
            kwargs["feature_flag_variant_id"] = feature_flag_variant_id
        if is_active is not unset:
            kwargs["is_active"] = is_active
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.is_control = is_control
        self_.key = key
        self_.weight = weight
