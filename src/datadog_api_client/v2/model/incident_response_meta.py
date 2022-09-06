# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_response_meta_pagination import IncidentResponseMetaPagination

        return {
            "pagination": (IncidentResponseMetaPagination,),
        }

    attribute_map = {
        "pagination": "pagination",
    }

    def __init__(self_, *args, **kwargs):
        """
        The metadata object containing pagination metadata.

        :param pagination: Pagination properties.
        :type pagination: IncidentResponseMetaPagination, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
