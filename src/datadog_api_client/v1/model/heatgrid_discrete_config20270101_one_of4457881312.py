# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class HeatgridDiscreteConfig20270101OneOf4457881312(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "mode": (HeatgridDiscreteConfigAnyOfAnyOfItemMode4447618848,),
            "preset_name": (HeatgridPresetName,),
            "source": (HeatgridDiscreteConfigAnyOfAnyOfItemSource4447619168,),
        }

    attribute_map = {
        "mode": "mode",
        "preset_name": "preset_name",
        "source": "source",
    }

    def __init__(
        self_,
        mode: HeatgridDiscreteConfigAnyOfAnyOfItemMode4447618848,
        preset_name: HeatgridPresetName,
        source: HeatgridDiscreteConfigAnyOfAnyOfItemSource4447619168,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type mode: HeatgridDiscreteConfigAnyOfAnyOfItemMode4447618848

        :param preset_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type preset_name: HeatgridPresetName

        :param source: Test-only generated schema for the dashboard versioning proof of concept.
        :type source: HeatgridDiscreteConfigAnyOfAnyOfItemSource4447619168
        """
        super().__init__(kwargs)

        self_.mode = mode
        self_.preset_name = preset_name
        self_.source = source
