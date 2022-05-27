# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class IncidentFieldAttributesMultipleValue(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_field_attributes_value_type import IncidentFieldAttributesValueType

        return {
            "type": (IncidentFieldAttributesValueType,),
            "value": ([str], none_type),
        }

    attribute_map = {
        "type": "type",
        "value": "value",
    }

    def __init__(self, *args, **kwargs):
        """
        A field with potentially multiple values selected.

        :param type: Type of the multiple value field definitions.
        :type type: IncidentFieldAttributesValueType, optional

        :param value: The multiple values selected for this field.
        :type value: [str], none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentFieldAttributesMultipleValue, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
