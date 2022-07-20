# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
)


class SyntheticsAPITestResultData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_ssl_certificate import SyntheticsSSLCertificate
        from datadog_api_client.v1.model.synthetics_test_process_status import SyntheticsTestProcessStatus
        from datadog_api_client.v1.model.synthetics_api_test_result_failure import SyntheticsApiTestResultFailure
        from datadog_api_client.v1.model.synthetics_timing import SyntheticsTiming

        return {
            "cert": (SyntheticsSSLCertificate,),
            "event_type": (SyntheticsTestProcessStatus,),
            "failure": (SyntheticsApiTestResultFailure,),
            "http_status_code": (int,),
            "request_headers": ({str: (dict,)},),
            "response_body": (str,),
            "response_headers": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        none_type,
                    )
                },
            ),
            "response_size": (int,),
            "timings": (SyntheticsTiming,),
        }

    attribute_map = {
        "cert": "cert",
        "event_type": "eventType",
        "failure": "failure",
        "http_status_code": "httpStatusCode",
        "request_headers": "requestHeaders",
        "response_body": "responseBody",
        "response_headers": "responseHeaders",
        "response_size": "responseSize",
        "timings": "timings",
    }

    def __init__(self, *args, **kwargs):
        """
        Object containing results for your Synthetic API test.

        :param cert: Object describing the SSL certificate used for a Synthetic test.
        :type cert: SyntheticsSSLCertificate, optional

        :param event_type: Status of a Synthetic test.
        :type event_type: SyntheticsTestProcessStatus, optional

        :param failure: The API test failure details.
        :type failure: SyntheticsApiTestResultFailure, optional

        :param http_status_code: The API test HTTP status code.
        :type http_status_code: int, optional

        :param request_headers: Request header object used for the API test.
        :type request_headers: {str: (dict,)}, optional

        :param response_body: Response body returned for the API test.
        :type response_body: str, optional

        :param response_headers: Response headers returned for the API test.
        :type response_headers: {str: (bool, date, datetime, dict, float, int, list, str, none_type,)}, optional

        :param response_size: Global size in byte of the API test response.
        :type response_size: int, optional

        :param timings: Object containing all metrics and their values collected for a Synthetic API test.
            Learn more about those metrics in `Synthetics documentation <https://docs.datadoghq.com/synthetics/#metrics>`_.
        :type timings: SyntheticsTiming, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsAPITestResultData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
