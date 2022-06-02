# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AuthNMappingResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.authn_mapping import AuthNMapping
        from datadog_api_client.v2.model.authn_mapping_included import AuthNMappingIncluded

        return {
            "data": (AuthNMapping,),
            "included": ([AuthNMappingIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(self, *args, **kwargs):
        """
        AuthN Mapping response from the API.

        :param data: The AuthN Mapping object returned by API.
        :type data: AuthNMapping, optional

        :param included: Included data in the AuthN Mapping response.
        :type included: [AuthNMappingIncluded], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AuthNMappingResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
