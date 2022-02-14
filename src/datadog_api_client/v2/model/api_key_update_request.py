# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.

from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.api_key_update_data import APIKeyUpdateData

    globals()["APIKeyUpdateData"] = APIKeyUpdateData


class APIKeyUpdateRequest(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "data": (APIKeyUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    read_only_vars = {}

    def __init__(self, data, *args, **kwargs):
        """
        Request used to update an API key.

        :param data: Object used to update an API key.
        :type data: APIKeyUpdateData
        """
        super().__init__(kwargs)

        self._check_pos_args(args)
        self.data = data

    @classmethod
    def _from_openapi_data(cls, data, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(APIKeyUpdateRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)
        self.data = data

        return self
