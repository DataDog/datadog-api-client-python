# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_response_data import IncidentResponseData
        from datadog_api_client.v2.model.incident_response_included_item import IncidentResponseIncludedItem

        return {
            "data": (IncidentResponseData,),
            "included": ([IncidentResponseIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }
    read_only_vars = {
        "included",
    }

    def __init__(self_, data, *args, **kwargs):
        """
        Response with an incident.

        :param data: Incident data from a response.
        :type data: IncidentResponseData

        :param included: Included related resources that the user requested.
        :type included: [IncidentResponseIncludedItem], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.data = data
