# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CheckCanDeleteMonitorResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ok": ([int],),
        }

    attribute_map = {
        "ok": "ok",
    }

    def __init__(self, *args, **kwargs):
        """
        Wrapper object with the list of monitor IDs.

        :param ok: An array of of Monitor IDs that can be safely deleted.
        :type ok: [int], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(CheckCanDeleteMonitorResponseData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
