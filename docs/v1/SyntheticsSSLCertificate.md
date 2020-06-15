# synthetics_ssl_certificate.SyntheticsSSLCertificate

Object describing the SSL certificate used for a Synthetic test.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cipher** | **str** | Cipher used for the connection. | [optional] 
**exponent** | **float** | Exponent associated to the certificate. | [optional] 
**ext_key_usage** | **[str]** | Array of extensions and details used for the certificate. | [optional] 
**fingerprint** | **str** | MD5 digest of the DER-encoded Certificate information. | [optional] 
**fingerprint256** | **str** | SHA-1 digest of the DER-encoded Certificate information. | [optional] 
**issuer** | [**synthetics_ssl_certificate_issuer.SyntheticsSSLCertificateIssuer**](SyntheticsSSLCertificateIssuer.md) |  | [optional] 
**modulus** | **str** | Modulus associated to the SSL certificate private key. | [optional] 
**protocol** | **str** | TLS protocol used for the test. | [optional] 
**serial_number** | **str** | Serial Number assigned by Symantec to the SSL certificate. | [optional] 
**subject** | [**synthetics_ssl_certificate_subject.SyntheticsSSLCertificateSubject**](SyntheticsSSLCertificateSubject.md) |  | [optional] 
**valid_from** | **datetime** | Date from which the SSL certificate is valid. | [optional] 
**valid_to** | **datetime** | Date until which the SSL certificate is valid. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


