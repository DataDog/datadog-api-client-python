# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.spans_aggregate_bucket_value import SpansAggregateBucketValue
    from datadog_api_client.v2.model.spans_aggregate_bucket_value_timeseries_point import (
        SpansAggregateBucketValueTimeseriesPoint,
    )


class SpansAggregateBucketAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spans_aggregate_bucket_value import SpansAggregateBucketValue

        return {
            "by": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "compute": (dict,),
            "computes": ({str: (SpansAggregateBucketValue,)},),
        }

    attribute_map = {
        "by": "by",
        "compute": "compute",
        "computes": "computes",
    }

    def __init__(
        self_,
        by: Union[Dict[str, Any], UnsetType] = unset,
        compute: Union[dict, UnsetType] = unset,
        computes: Union[
            Dict[str, Union[SpansAggregateBucketValue, str, float, List[SpansAggregateBucketValueTimeseriesPoint]]],
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        A bucket values.

        :param by: The key, value pairs for each group by.
        :type by: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param compute: The compute data.
        :type compute: dict, optional

        :param computes: A map of the metric name -> value for regular compute or list of values for a timeseries.
        :type computes: {str: (SpansAggregateBucketValue,)}, optional
        """
        if by is not unset:
            kwargs["by"] = by
        if compute is not unset:
            kwargs["compute"] = compute
        if computes is not unset:
            kwargs["computes"] = computes
        super().__init__(kwargs)
