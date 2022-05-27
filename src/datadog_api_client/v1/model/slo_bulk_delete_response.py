# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOBulkDeleteResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_bulk_delete_response_data import SLOBulkDeleteResponseData
        from datadog_api_client.v1.model.slo_bulk_delete_error import SLOBulkDeleteError

        return {
            "data": (SLOBulkDeleteResponseData,),
            "errors": ([SLOBulkDeleteError],),
        }

    attribute_map = {
        "data": "data",
        "errors": "errors",
    }

    def __init__(self, *args, **kwargs):
        """
        The bulk partial delete service level objective object endpoint
        response.

        This endpoint operates on multiple service level objective objects, so
        it may be partially successful. In such cases, the "data" and "error"
        fields in this response indicate which deletions succeeded and failed.

        :param data: An array of service level objective objects.
        :type data: SLOBulkDeleteResponseData, optional

        :param errors: Array of errors object returned.
        :type errors: [SLOBulkDeleteError], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOBulkDeleteResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
