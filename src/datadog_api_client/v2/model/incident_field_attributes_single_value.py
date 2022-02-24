# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


def lazy_import():
    from datadog_api_client.v2.model.incident_field_attributes_single_value_type import (
        IncidentFieldAttributesSingleValueType,
    )

    globals()["IncidentFieldAttributesSingleValueType"] = IncidentFieldAttributesSingleValueType


class IncidentFieldAttributesSingleValue(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "type": (IncidentFieldAttributesSingleValueType,),
            "value": (str, none_type),
        }

    attribute_map = {
        "type": "type",
        "value": "value",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        A field with a single value selected.

        :param type: Type of the single value field definitions.
        :type type: IncidentFieldAttributesSingleValueType, optional

        :param value: The single value selected for this field.
        :type value: str, none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentFieldAttributesSingleValue, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
