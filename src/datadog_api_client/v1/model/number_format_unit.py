# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class NumberFormatUnit(ModelComposed):
    def __init__(self, **kwargs):
        """
        Number format unit.

        :param per_unit_name: The name of the unit per item.
        :type per_unit_name: str, optional

        :param type: The type of unit scale.
        :type type: NumberFormatUnitScaleType, optional

        :param unit_name: The name of the unit.
        :type unit_name: str, optional

        :param label: The label for the custom unit.
        :type label: str, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1.model.number_format_unit_canonical import NumberFormatUnitCanonical
        from datadog_api_client.v1.model.number_format_unit_custom import NumberFormatUnitCustom

        return {
            "oneOf": [
                NumberFormatUnitCanonical,
                NumberFormatUnitCustom,
            ],
        }
