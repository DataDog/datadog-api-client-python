# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RUMResponseMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_response_page import RUMResponsePage
        from datadog_api_client.v2.model.rum_response_status import RUMResponseStatus
        from datadog_api_client.v2.model.rum_warning import RUMWarning

        return {
            "elapsed": (int,),
            "page": (RUMResponsePage,),
            "request_id": (str,),
            "status": (RUMResponseStatus,),
            "warnings": ([RUMWarning],),
        }

    attribute_map = {
        "elapsed": "elapsed",
        "page": "page",
        "request_id": "request_id",
        "status": "status",
        "warnings": "warnings",
    }

    def __init__(self, *args, **kwargs):
        """
        The metadata associated with a request.

        :param elapsed: The time elapsed in milliseconds.
        :type elapsed: int, optional

        :param page: Paging attributes.
        :type page: RUMResponsePage, optional

        :param request_id: The identifier of the request.
        :type request_id: str, optional

        :param status: The status of the response.
        :type status: RUMResponseStatus, optional

        :param warnings: A list of warnings (non-fatal errors) encountered. Partial results may return if
            warnings are present in the response.
        :type warnings: [RUMWarning], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RUMResponseMetadata, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
