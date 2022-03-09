# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.incident_service_response_data import IncidentServiceResponseData
    from datadog_api_client.v2.model.incident_service_included_items import IncidentServiceIncludedItems

    globals()["IncidentServiceResponseData"] = IncidentServiceResponseData
    globals()["IncidentServiceIncludedItems"] = IncidentServiceIncludedItems


class IncidentServiceResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "data": (IncidentServiceResponseData,),
            "included": ([IncidentServiceIncludedItems],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }
    read_only_vars = {
        "included",
    }

    def __init__(self, data, *args, **kwargs):
        """
        Response with an incident service payload.

        :param data: Incident Service data from responses.
        :type data: IncidentServiceResponseData

        :param included: Included objects from relationships.
        :type included: [IncidentServiceIncludedItems], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.data = data

    @classmethod
    def _from_openapi_data(cls, data, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentServiceResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.data = data
        return self
