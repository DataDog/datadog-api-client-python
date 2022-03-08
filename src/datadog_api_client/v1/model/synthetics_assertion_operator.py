# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class SyntheticsAssertionOperator(ModelSimple):

    allowed_values = {
        "value": {
            "CONTAINS": "contains",
            "DOES_NOT_CONTAIN": "doesNotContain",
            "IS": "is",
            "IS_NOT": "isNot",
            "LESS_THAN": "lessThan",
            "LESS_THAN_OR_EQUAL": "lessThanOrEqual",
            "MORE_THAN": "moreThan",
            "MORE_THAN_OR_EQUAL": "moreThanOrEqual",
            "MATCHES": "matches",
            "DOES_NOT_MATCH": "doesNotMatch",
            "VALIDATES": "validates",
            "IS_IN_MORE_DAYS_THAN": "isInMoreThan",
            "IS_IN_LESS_DAYS_THAN": "isInLessThan",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        Assertion operator to apply.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of ["contains", "doesNotContain", "is", "isNot", "lessThan", "lessThanOrEqual", "moreThan", "moreThanOrEqual", "matches", "doesNotMatch", "validates", "isInMoreThan", "isInLessThan"].
        :type value: str
        """
        super().__init__(kwargs)

        if "value" in kwargs:
            value = kwargs.pop("value")
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=self._path_to_item,
                valid_classes=(self.__class__,),
            )

        self._check_pos_args(args)

        self.value = value

        self._check_kw_args(kwargs)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""
        return cls(*args, **kwargs)
