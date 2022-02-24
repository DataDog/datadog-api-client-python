# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.incident_response_meta_pagination import IncidentResponseMetaPagination

    globals()["IncidentResponseMetaPagination"] = IncidentResponseMetaPagination


class IncidentResponseMeta(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "pagination": (IncidentResponseMetaPagination,),
        }

    attribute_map = {
        "pagination": "pagination",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        The metadata object containing pagination metadata.

        :param pagination: Pagination properties.
        :type pagination: IncidentResponseMetaPagination, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentResponseMeta, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
