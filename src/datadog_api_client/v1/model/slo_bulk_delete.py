# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOBulkDelete(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        from datadog_api_client.v1.model.slo_timeframe import SLOTimeframe

        return ([SLOTimeframe],)

    def __init__(self, *args, **kwargs):
        """
        A map of service level objective object IDs to arrays of timeframes,
        which indicate the thresholds to delete for each ID.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOBulkDelete, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
