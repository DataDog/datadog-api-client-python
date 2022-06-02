# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
)


class SyntheticsAssertionJSONPathTargetTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "json_path": (str,),
            "operator": (str,),
            "target_value": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                none_type,
            ),
        }

    attribute_map = {
        "json_path": "jsonPath",
        "operator": "operator",
        "target_value": "targetValue",
    }

    def __init__(self, *args, **kwargs):
        """
        Composed target for ``validatesJSONPath`` operator.

        :param json_path: The JSON path to assert.
        :type json_path: str, optional

        :param operator: The specific operator to use on the path.
        :type operator: str, optional

        :param target_value: The path target value to compare to.
        :type target_value: bool, date, datetime, dict, float, int, list, str, none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsAssertionJSONPathTargetTarget, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
