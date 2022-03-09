# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class FormulaAndFunctionApmDependencyStatName(ModelSimple):

    allowed_values = {
        "value": {
            "AVG_DURATION": "avg_duration",
            "AVG_ROOT_DURATION": "avg_root_duration",
            "AVG_SPANS_PER_TRACE": "avg_spans_per_trace",
            "ERROR_RATE": "error_rate",
            "PCT_EXEC_TIME": "pct_exec_time",
            "PCT_OF_TRACES": "pct_of_traces",
            "TOTAL_TRACES_COUNT": "total_traces_count",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        APM statistic.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of ["avg_duration", "avg_root_duration", "avg_spans_per_trace", "error_rate", "pct_exec_time", "pct_of_traces", "total_traces_count"].
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
