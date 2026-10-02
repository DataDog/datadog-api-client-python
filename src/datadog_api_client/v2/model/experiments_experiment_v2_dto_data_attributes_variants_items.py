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
)


class ExperimentsExperimentV2DTODataAttributesVariantsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "feature_flag_variant_id": (str,),
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
        is_active: bool,
        is_control: bool,
        key: str,
        weight: float,
        feature_flag_variant_id: Union[str, UnsetType] = unset,
        name: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Variant in an experiment, with its identity and traffic allocation.

        :param feature_flag_variant_id: Backing feature flag variant ID. Present for Datadog feature flag experiments and omitted for Warehouse experiments.
        :type feature_flag_variant_id: str, optional

        :param is_active: Whether this variant participates in the experiment.
        :type is_active: bool

        :param is_control: Whether this is the single control variant.
        :type is_control: bool

        :param key: Value recorded in exposure data for this variant.
        :type key: str

        :param name: Display name of the experiment variant.
        :type name: str, none_type, optional

        :param weight: Traffic allocation percentage.
        :type weight: float
        """
        if feature_flag_variant_id is not unset:
            kwargs["feature_flag_variant_id"] = feature_flag_variant_id
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.is_active = is_active
        self_.is_control = is_control
        self_.key = key
        self_.weight = weight
